# BF-01 — Bluesky-first policy benchmark (structure baseline)

**Date:** 11 Oct 2026  
**Owner policy:** Reference Bluesky's established policy **framework first**; do not redesign Unusu@ls policies on intuition. Map and evidence differences only after the baseline is locked.  
**State:** Reference audit only; **not legal text, not approved for publication**. Keep PR #3 draft and unmerged.

Bluesky's policy text is third-party content. This benchmark reproduces only **section names, subject coverage, reference URLs and independent audit findings**, not Bluesky's complete copyrighted expression. Any Unusu@ls legal text must be written independently and verified against our actual systems and jurisdiction.

## Canonical Bluesky sources (view full original text at links)

| Reference | Official URL | Displayed update date |
| --- | --- | --- |
| Terms of Service | https://bsky.social/about/support/tos | 14 Aug 2025 |
| Privacy Policy | https://bsky.social/about/support/privacy-policy | 14 Aug 2025 |
| Community Guidelines | https://bsky.social/about/support/community-guidelines | 19 Sep 2025 |
| Copyright and IP | https://www.bsky.social/about/support/copyright | 29 Jan 2026 |
| Support/legal request portal | https://bsky.social/about/support | no update date confirmed |
| AT Protocol Network Services Privacy | https://bsky.social/about/support/network-services-privacy-policy | 22 May 2024 |

## 1. Terms reference structure (all 18 official section titles)

1. Eligibility and Age Verification
2. Account Registration and Responsibilities
3. User Content
4. Proactive Moderation and Illegal Content
5. Discover Feed and Recommender Systems
6. Complaints and Appeals
7. Termination
8. Third-Party Services
9. Open Source Software
10. Warranty Disclaimer
11. Indemnification
12. Limitation of Liability
13. Governing Law, Jurisdiction, Venue, Dispute Resolution, and Arbitration
14. Updates to Terms
15. Intellectual Property
16. General Terms
17. Contact Us
18. Apple App Store and Google Play Required Terms

**Current Repo4 source to compare:** `docs/google-play/policies/UNUSUALS_TERMS_OF_SERVICE_PUBLICATION_CANDIDATE_V1.md` (17 locally numbered sections, different taxonomy). Notable reference areas not separately surfaced: recommender systems, proactive moderation methods, appeals mechanism, platform-specific terms. Some US arbitration provisions cannot be presented as facts for a Nigerian business without legal review.

## 2. Privacy reference structure (all 18 official section titles)

1. Introduction
2. What is Personal Data?
3. Informing us of changes
4. Applicability of this Policy
5. Third-party Services
6. If you do not want to provide Personal Data
7. Updates to this Policy
8. Personal Data We Collect
9. Cookies
10. How We Use Personal Data
11. How We Share your Personal Data
12. International data transfers
13. Your Privacy Choices and Rights
14. Retention of Personal Data
15. Supplemental Notice for Certain Jurisdictions
16. Security
17. Children's Personal Information
18. Contact Us

**Current Repo4 source:** `docs/google-play/policies/UNUSUALS_PRIVACY_POLICY_PUBLICATION_CANDIDATE_V1.md` (14 sections with different taxonomy). Missing or less granular compared to reference: standalone cookies section, detailed cross-border transfer disclosures, third-party and communications choices, jurisdiction-specific rights. **Do not copy Bluesky's statements about DMs, location, payments, tracking, age assurance, retention or named suppliers unless our exact app and data inventory confirms them.**

## 3. Community Guidelines reference structure

**Underlying editorial principles:** Safety First; Respect Others; Be Authentic; Follow the Rules. An additional major section addresses **Protected Expression**.

- Safety First: public safety, threatening conduct, child safety, adult content, mental health, privacy, animal safety.
- Respect Others: discrimination, harassment and abuse.
- Be Authentic: spam/manipulation, authentic accounts and civic information integrity.
- Follow the Rules: restricted commerce, intellectual property, platform security, bans and evasion.
- Protected Expression: journalism, education, advocacy, recovery, public records and legitimate public-interest context.

**Current Repo4 source:** `docs/google-play/policies/UNUSUALS_COMMUNITY_GUIDELINES_AND_SAFETY_STANDARDS_V1.md`; substantive areas overlap, but editorial organisation and protected-expression balancing do not fully match.

## 4. Copyright and IP reference (7-section standalone policy)

1. Defined Terms
2. Submission type
3. Counter-Notification and Appeals Process
4. Repeat Infringer and Abusive Reporting Policy
5. Transparency and Compliance
6. Use of Your Copyrighted or Trademarked Content
7. Contact

**Gap:** Original Unusu@ls policy manifest includes no comparable standalone copyright/IP page; references exist in terms/safety. Proposed private design path: `/unusuals/copyright/` **only after owner approval**. Do not claim US DMCA agent status, DSA reporting, or a form/appeal process we have not built.

## 5. Support and account deletion

Bluesky's support page provides policy links, support contact and legal/government request pathways. Its Terms describe in-app deletion and AT Protocol federation limitations. Our Unusu@ls Play-bound application needs an externally usable account-deletion request page as well as an in-app process. The UI and processing procedures must be independently certified; don't substitute a mock page for a working deletion workflow.

## Benchmark fidelity and publication controls

- **Baseline-first:** lock source set, version dates, section order and subject coverage.
- **Difference register next:** identify missing/partial/unsupported clauses and why.
- **Unusu@ls adaptations last:** company identity, real operators, real functionality, AT Protocol topology, Nigeria and other applicable law, Google Play compliance; each change traceable and evidenced.
- **Preview only:** no `main` merge or Cloudflare production deployment. Corporate `/privacy/` and `/terms/` remain unchanged; app content stays under `/unusuals/`.
- **No fabrication:** don't state that Unusu@ls has Bluesky's moderators, hash-matching systems, appeals SLAs, government portals, US representatives, direct messages, account deletion capabilities, payments or tracking without actual verified evidence.
- **Final gates:** owner approval, qualified privacy/legal review, secure email intake and deletion/moderation process verification, exact Android build reconciliation.

**Corresponding owner-controlled source-of-truth document:** https://docs.google.com/document/d/1HkrvhnSQRFPg7C4b9jAZAaVTEo_fc2qAVSRFPzqaqAI/edit
