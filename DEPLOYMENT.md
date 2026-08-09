# Unusuals Network Corporate Website — Deployment Gate

## Current state

- Source build: PASS
- Desktop render: PASS
- Mobile render: PASS
- Internal-link audit: PASS
- Static security headers: PASS
- Public deployment: NOT YET CONNECTED — owner review and Cloudflare setup remain pending
- PDS/DNS change: NONE

## Target

- Repository: `olawaleayeni1268/unusuals-network-website`
- Production branch: `main`
- Hosting: Cloudflare Pages
- Production hostname: `www.unusuals.worldofchampionsnetwork.com.ng`

## GitHub import

Create an empty GitHub repository named `unusuals-network-website` under `olawaleayeni1268`. Do not add starter files if importing this source as-is.

After the repository exists, push this source tree to `main` or create an initial review branch and pull request.

## Cloudflare Pages

After owner review and explicit deployment approval:

1. Create a Pages project connected to the website repository.
2. Use `main` as the production branch.
3. No framework preset is required.
4. No build command is required.
5. Use the repository root as the static output.
6. Add the custom domain `www.unusuals.worldofchampionsnetwork.com.ng` through the Pages custom-domain workflow.
7. Do not alter the existing `unusuals.worldofchampionsnetwork.com.ng` PDS host.

## Post-deployment verification

- HTTPS valid
- Home/About/Unusu@ls/Contact/Privacy/Terms return 200
- Mobile navigation works
- `robots.txt` and `sitemap.xml` return 200
- Security headers are present
- Admin/support/privacy/safety/legal mailto links are correct
- Business address matches the CAC-submitted address: Amuyo Area, Offa, Kwara State, Nigeria
