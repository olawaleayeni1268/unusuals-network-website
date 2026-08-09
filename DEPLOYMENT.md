# Unusuals Network Corporate Website — Deployment Gate

## Current state

- Source build: PASS
- Desktop render: PASS
- Mobile render: PASS
- Internal-link audit: PASS
- Static security headers: PASS
- Cloudflare Pages project: CONNECTED
- Preview deployment: TRIGGERED FROM FEATURE BRANCH
- Production merge: NOT YET APPROVED
- Custom domain: NOT YET ATTACHED
- PDS/DNS change: NONE

## Target

- Repository: `olawaleayeni1268/unusuals-network-website`
- Production branch: `main`
- Preview branch: `feat/corporate-website-v1-photo-hero`
- Hosting: Cloudflare Pages
- Production hostname: `www.unusuals.worldofchampionsnetwork.com.ng`

## Cloudflare Pages configuration

1. Pages project is connected to the website repository.
2. Production branch is `main`.
3. Framework preset is `None`.
4. Build command is blank.
5. Build output directory is `.` (repository root).
6. The feature branch is used for owner preview before merge.
7. Do not attach `www.unusuals.worldofchampionsnetwork.com.ng` until owner visual acceptance.
8. Do not alter the existing `unusuals.worldofchampionsnetwork.com.ng` PDS host.

## Post-deployment verification

- HTTPS valid
- Home/About/Unusu@ls/Contact/Privacy/Terms return 200
- Approved photo hero renders correctly
- Mobile navigation works
- `robots.txt` and `sitemap.xml` return 200
- Security headers are present
- Admin/support/privacy/safety/legal mailto links are correct
- Business address matches the CAC-submitted address: Amuyo Area, Offa, Kwara State, Nigeria
