# Lab 1 — Research the Asteron Launch and Build a Verified Source Register

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Microsoft 365 Copilot  
**Maps to:** LO1: use G-C-S-E to research a bounded source pack in Copilot Chat, trace material claims to evidence and record unresolved questions  
**Duration:** 35 minutes  
**Tools:** Microsoft 365 Copilot Chat · Excel · asteron-project-brief.md · asteron-decision-log.csv · asteron-stakeholder-notes.md

---

## Goal

Create a source register and verified claim ledger that can safely govern the Word brief and every later Asteron artifact.

## What You Will Do

You will inspect three synthetic Asteron source files, register their purpose and status, then ask Copilot Chat to synthesise the launch facts. You will open the sources, verify dates, owners, decisions and open questions, and keep unsupported statements out of the approved ledger.

## What You Will Build

work-c027/C027-Asteron-Source-Register.xlsx with Sources, Claim_Ledger and Review_Log tables, plus work-c027/C027-Asteron-Verified-Claims.txt and a Reviewed release record

## Prerequisites

- Download the repository and keep every file in labs/assets together.
- Sign in to an eligible Microsoft 365 account and open Copilot Chat.
- Create work-c027 in an approved OneDrive location; use only the supplied synthetic Asteron sources.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Open labs/assets/asteron-project-brief.md, asteron-decision-log.csv and asteron-stakeholder-notes.md. For each file, note its title, owner, effective date, purpose, governing facts and limitations. Do not ask Copilot to summarise the files yet.

```text
Required pre-read questions:
1. Which source governs the launch date?
2. Which source governs named decisions and owners?
3. Which notes are observations rather than approved decisions?
4. Which question remains unresolved?
```

### 2. Open labs/assets/asteron-source-register-template.csv in Excel and save it as work-c027/C027-Asteron-Source-Register.xlsx. Rename the first sheet Sources, format the data as table tblSources and enter one row per source. Add a second sheet named Claim_Ledger and copy in the headers from asteron-claim-ledger-template.csv as table tblClaims. Add a third sheet named Review_Log and copy asteron-review-log-template.csv as table tblReviewLog.

```text
Required tables:
tblSources: Source_ID | File | Owner | Effective_Date | Purpose | Governs | Limitation | Status
tblClaims: Claim_ID | Claim | Source_ID | Evidence | Confidence | Check | Reviewer_Note | Release_State
tblReviewLog: Artifact | Prompt | Sources_Used | Source_Coverage | Reviewer | Review_Date | Open_Question | Release_State | Next_Use
```

### 3. Attach or reference only the three files in the permitted source pack in Copilot Chat. Submit the G-C-S-E prompt below. If your experience cannot reference all three files, process one file at a time and record that limitation in Sources; do not imply that an unavailable source was used. Preserve each source's true authority and status; stakeholder notes remain working observations, not decisions.

```text
GOAL: Build a claim ledger for the Asteron client portal pilot launch.
CONTEXT: Department heads need confirmed dates, owners, decisions, dependencies and open questions.
SOURCE: Use only the attached project brief, decision log and stakeholder notes. Name the Source_ID for every row.
EXPECTATIONS: Return Claim_ID | Claim | Source_ID | Evidence | Confidence | Check. Use ISO dates. Do not turn a proposal into a decision. Mark contradictions and missing evidence as HOLD. Do not add web facts.
```

### 4. Copy the proposed rows into tblClaims. Open the governing source for each material date, number, owner and decision. Set Check to VERIFIED only when the source supports the statement. Use REVISE for a correctable wording issue and HOLD for an unresolved or unsupported statement.

```text
Material checks:
Launch date = 2026-08-18
Pilot scope = 20 internal participants across five departments
FAQ owner = Nisha Rao, due 2026-08-11
Data export owner = Leon Wu, current due date 2026-08-13
External announcement = not released before privacy sign-off
Support clinic date and room = proposed, not confirmed
```

### 5. Complete one row in tblReviewLog with the exact prompt, sources actually used, coverage, reviewer name, review date, remaining open question, release state and next use. Export only VERIFIED claim rows as plain text to work-c027/C027-Asteron-Verified-Claims.txt, including Claim_ID, Claim, Source_ID and Evidence. A source-supported claim may be explicitly labelled Confirmed, Proposed or Open; exclude all unsupported HOLD rows. Save the workbook and link both outputs in your work-c027 notes.

```text
Release record:
Artifact: C027-Asteron-Source-Register.xlsx
State: Reviewed
Open question: Is the 2026-08-19 support clinic room confirmed?
Next use: governing source for Lab 2 Word brief
```

## Test It

tblSources must contain exactly three permitted sources with their true authority/status and no web source. tblClaims must include the six material checks with Source_ID and evidence. The 2026-08-13 data-export date must supersede 2026-08-12, and the support clinic must remain proposed. Every unsupported statement must be REVISE or HOLD. tblReviewLog must contain every required review field, and the TXT export must contain only VERIFIED claims, including source-supported Proposed/Open items with those labels and no unsupported HOLD rows. The final release state must be Reviewed, not Approved, because one room question remains open.

## Checkpoint and Rejoin Point

Save the source register and verified-claims TXT in work-c027. Lab 2 references the supported TXT export and preserves the open support-clinic question. If you need to rejoin, use labs/assets/asteron-expected-facts.md to rebuild the ledger and TXT export.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Copilot cannot reference one or more local files. | Save the files to an approved OneDrive location or process them one at a time. Record the actual source coverage and merge the ledgers manually; never claim a missing file was reviewed. |
| A generated claim has no traceable source. | Set Release_State to HOLD, add 'No governing evidence found' and exclude the claim from the Word brief. |
| Copilot treats the earlier 2026-08-12 export date as current. | Open the decision log, use the latest dated decision and record 2026-08-13 as current while noting the superseded date. |

## Challenge

Ask Copilot to return a contradiction matrix by Source_ID. Verify it manually and explain why the latest dated statement is not automatically authoritative unless the source is allowed to govern that fact.

## Reflection

Which prompt element made it easiest to detect an unsupported or superseded claim, and why?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-draft-and-approve-the-asteron-launch-brief-in-word.md)
