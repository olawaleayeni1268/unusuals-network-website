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
