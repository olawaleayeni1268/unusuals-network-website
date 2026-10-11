# BF-02 — Bluesky-first preview coverage register

**Date:** 11 October 2026  
**Status:** Draft PR preview only — not public legal policy.  

## Official reference structure matched

- Terms: **18 of 18** Bluesky major section topics represented in the same order. Source: https://bsky.social/about/support/tos (updated 14 Aug 2025).
- Privacy: **18 of 18** major topics in the same order. Source: https://bsky.social/about/support/privacy-policy (updated 14 Aug 2025).
- Community Guidelines: **four principles** (Safety First, Respect Others, Be Authentic, Follow the Rules), plus **Protected Expression**, and reporting/enforcement process. Source: https://bsky.social/about/support/community-guidelines (updated 19 Sep 2025).
- Copyright/IP: separate **seven-section** page. Source: https://www.bsky.social/about/support/copyright (updated 29 Jan 2026).
- Support, legal intake and account deletion: present as distinct help pages; aligned in coverage but independent procedures are not fully evidenced. Source: https://bsky.social/about/support

## Difference register — do not silently assert these operational facts

| Topic | Bluesky reference | Unusu@ls draft disposition | Evidence gate |
|---|---|---|---|
| Exact legal text | Third-party policy expression | Reworded independently | Qualified counsel |
| Moderation detection, hashes, staffing | Specific active workflows | Not claimed | Moderation audit |
| Appeals deadline/portal | Bluesky mechanisms and EU appeals | Email route draft; no SLA promised | Appeal operations + legal |
| Algorithms & opt out | Bluesky Discover controls | Describe only evidenced feeds | Exact app test |
| Direct messages, age assurance, contacts, payment | Bluesky data processing cases | Not presumed present | Exact release data-flow inventory |
| Cookie/diagnostic collection | Bluesky-specific | Placeholder for verified host/SDK disclosure | Runtime and SDK review |
| Privacy rights / transfers | Multiple US/EU/UK/Brazil provisions | Nigeria-first assessment, foreign rights subject to scope | Nigerian privacy counsel and data transfer register |
| Retention periods | Bluesky-specific implementation | Repo4 proposed 90d/24mo — NOT guaranteed | Backend, backup and mail audit |
| Arbitration, monetary liability cap | US-specific private dispute scheme | Not borrowed | Qualified Nigeria counsel |
| Copyright takedown/counter notice | Dedicated form + specific statutory process | Draft legal mailbox only | IP intake, legal & moderation procedures |
| Government / law enforcement portal | Bluesky portal and DSA response | No such portal claimed | Legal & operating decision |
| Actual account deletion | In-app and external requirements | External email route draft, in-app unverified | End-to-end deletion test |
| App Store clauses | Apple and Google terms | Play planned; Apple unverified | Release-store contracts |
| AT Protocol network services notice | Distinct operator notices | Scope to be determined | Network topology and data controller audit |

## Production safety and review gates

1. Pages remain under `/unusuals/` without touching corporate `/privacy/` or `/terms/`.
2. All pages retain `noindex,nofollow`, a conspicuous preview banner, and proposed effective dates.
3. Draft PR only; do not merge or enable the Android policy-pages-live flag.
4. Owner approval of design and exact policy wording; qualified legal/privacy review; verified support, moderation and deletion; then a separately authorised production deployment.
5. A matching topic heading is not evidence that a particular procedure exists.
