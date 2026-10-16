"""Static checks for the Unusuals Network website. Standard library only.

Run from the repository root: python3 scripts/site_check.py
Exits 1 on any FAIL. Prints SHA-256 of every checked file as evidence.
"""
import hashlib, os, re, sys
from urllib.parse import urlparse, unquote

ROOT = '.'
SKIP_DIRS = {'.git', '.github', 'docs', 'scripts'}
ALLOWED_MAIL = 'unusuals.worldofchampionsnetwork.com.ng'
DRAFT = re.compile(r'NOT PUBLISHED|DESIGN PREVIEW|REVIEW PREVIEW', re.I)
META = re.compile(r'<meta\b[^>]*>', re.I)
fails = []


def meta(html, name):
    """content of <meta name=...>, in either attribute order"""
    for tag in META.findall(html):
        if re.search(r'\bname="%s"' % name, tag, re.I):
            m = re.search(r'\bcontent="([^"]*)"', tag, re.I)
            return m.group(1) if m else ''
    return None


def pages():
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
        for f in sorted(files):
            if f.endswith('.html'):
                yield os.path.normpath(os.path.join(d, f))


def target(page, ref):
    u = urlparse(ref)
    if u.scheme or u.netloc or ref.startswith('#'):
        return None
    path = unquote(u.path)
    if not path:
        return None
    base = ROOT if path.startswith('/') else os.path.dirname(page)
    p = os.path.normpath(os.path.join(base, path.lstrip('/')))
    if path.endswith('/') or os.path.isdir(p):
        p = os.path.join(p, 'index.html')
    return p


drafts = set()
for page in pages():
    html = open(page, encoding='utf-8').read()
    for need, rx in [('title', r'<title>[^<]+</title>'), ('lang', r'<html[^>]*\slang="')]:
        if not re.search(rx, html, re.I):
            fails.append('%s: missing %s' % (page, need))
    if meta(html, 'viewport') is None:
        fails.append('%s: missing viewport' % page)
    if DRAFT.search(html):
        drafts.add(page)
        if 'noindex' not in (meta(html, 'robots') or '').lower():
            fails.append('%s: draft banner without <meta name="robots" content="noindex">' % page)
    for ref in re.findall(r'(?:href|src)="([^"]+)"', html):
        if ref.startswith('mailto:'):
            addr = ref[7:].split('?')[0]
            if not addr.endswith('@' + ALLOWED_MAIL):
                fails.append('%s: mailto outside %s: %s' % (page, ALLOWED_MAIL, addr))
            continue
        t = target(page, ref)
        if t and not os.path.exists(t):
            fails.append('%s: broken link %s' % (page, ref))

sitemap = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
for loc in re.findall(r'<loc>([^<]+)</loc>', sitemap):
    u = urlparse(loc)
    if u.netloc != 'www.' + ALLOWED_MAIL or u.scheme != 'https':
        fails.append('sitemap: wrong host or scheme: %s' % loc)
    t = target('index.html', u.path or '/')
    if not os.path.exists(t):
        fails.append('sitemap: no file for %s' % loc)
    elif t in drafts:
        fails.append('sitemap: lists a draft page %s' % loc)

# BF-09: Fail closed while app policy pages are under owner/legal review.
# A separately approved G7 publication change must deliberately revise this gate.
POLICY_PUBLICATION_APPROVED = True
REQUIRED_POLICIES = (
    'help', 'privacy', 'terms', 'safety', 'support', 'account-deletion', 'copyright',
)
INTERNAL_ONLY = (
    'docs/BF-01-BLUESKY-POLICY-REFERENCE-BASELINE.md',
    'BF-02-REFERENCE-COVERAGE-REGISTER.md',
    'SHA256SUMS.txt',
)
for private_path in INTERNAL_ONLY:
    if os.path.exists(private_path):
        fails.append('internal-only file in deploy root: %s' % private_path)
for policy in REQUIRED_POLICIES:
    page = os.path.join('unusuals', policy, 'index.html')
    if not os.path.isfile(page):
        fails.append('missing policy page: %s' % page)
        continue
    html = open(page, encoding='utf-8').read()
    expected = 'https://www.' + ALLOWED_MAIL + '/unusuals/' + policy + '/'
    links = re.findall(r'<link\b[^>]*>', html, re.I)
    canonicals = []
    for tag in links:
        if re.search(r'\brel="canonical"', tag, re.I):
            found = re.search(r'\bhref="([^"]+)"', tag, re.I)
            canonicals.append(found.group(1) if found else '')
    if canonicals != [expected]:
        fails.append('%s: incorrect/missing canonical %s' % (page, canonicals))
    if not POLICY_PUBLICATION_APPROVED:
        if 'NOT PUBLISHED' not in html or 'REVIEW PREVIEW' not in html:
            fails.append('%s: publication banner missing without G7 approval' % page)
        if 'noindex' not in (meta(html, 'robots') or '').lower():
            fails.append('%s: noindex missing without G7 approval' % page)
    else:
        for bad in ('NOT PUBLISHED', 'REVIEW PREVIEW', 'EFFECTIVE_DATE_PENDING', 'noindex'):
            if bad in html:
                fails.append('%s: unapproved release marker remains: %s' % (page, bad))
    footer = re.search(r'<nav\s+aria-label="Footer navigation"[^>]*>(.*?)</nav>', html, re.I | re.S)
    if not footer:
        fails.append('%s: policy footer not found' % page)
    else:
        for other in REQUIRED_POLICIES:
            if 'href="../%s/"' % other not in footer.group(1):
                fails.append('%s: missing footer link to %s' % (page, other))
        if 'href="https://www.' + ALLOWED_MAIL + '/"' not in footer.group(1):
            fails.append('%s: missing corporate home in policy footer' % page)
    if policy == 'privacy' and 'privacy@' + ALLOWED_MAIL not in html:
        fails.append('%s: privacy contact absent' % page)
    if policy == 'account-deletion':
        if 'mailto:privacy@' + ALLOWED_MAIL not in html:
            fails.append('%s: external deletion contact absent' % page)
        if 'Account%20deletion%20request' not in html:
            fails.append('%s: deletion mailto subject absent' % page)

if POLICY_PUBLICATION_APPROVED:
    # Every policy page must show one, identical, real effective date.
    dates = set()
    for policy in REQUIRED_POLICIES:
        page = os.path.join('unusuals', policy, 'index.html')
        if os.path.isfile(page):
            found = re.findall(r'Effective: ([^<]*)<', open(page, encoding='utf-8').read())
            if not found:
                fails.append('%s: effective date missing' % page)
            dates.update(found)
    if len(dates) > 1:
        fails.append('policy effective dates differ: %s' % ', '.join(sorted(dates)))
    for d in dates:
        if not re.fullmatch(r'[1-9][0-9]? (January|February|March|April|May|June|July|August|September|October|November|December) 20[2-9][0-9]', d):
            fails.append('invalid effective date: %r' % d)
    for policy in REQUIRED_POLICIES:
        needed = 'https://www.' + ALLOWED_MAIL + '/unusuals/' + policy + '/'
        if needed not in re.findall(r'<loc>([^<]+)</loc>', sitemap):
            fails.append('release sitemap missing policy URL: %s' % needed)

print('== SHA-256 of checked files')
for d, dirs, files in os.walk(ROOT):
    dirs[:] = sorted(x for x in dirs if x not in SKIP_DIRS)
    for f in sorted(files):
        p = os.path.normpath(os.path.join(d, f))
        print(hashlib.sha256(open(p, 'rb').read()).hexdigest(), p)
print('== drafts (noindex required):', ', '.join(sorted(drafts)) or 'none')
for f in fails:
    print('FAIL', f)
print('RESULT:', 'FAIL (%d)' % len(fails) if fails else 'PASS')
sys.exit(1 if fails else 0)
