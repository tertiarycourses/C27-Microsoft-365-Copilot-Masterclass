# Lab 6 — Validate a Teams Recap and Create the Action Register

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Copilot Across Your Everyday Work Apps  
**Maps to:** LO4: validate a Teams recap against transcript evidence and convert confirmed follow-up work into an action register with owners, due dates and release status  
**Duration:** 35 minutes  
**Tools:** Microsoft Teams · Copilot or intelligent recap · asteron-teams-transcript.md · Excel

---

## Goal

Create a transcript-backed action register that distinguishes decisions, actions, proposals and open questions.

## What You Will Do

You will use a trainer-provided synthetic Teams meeting recap or the supplied transcript in Copilot Chat inside Teams. You will compare generated decisions and actions with the evidence, correct attribution and dates, and create a durable action register for the cross-app workflow.

## What You Will Build

work-c027/C027-Teams-Action-Register.xlsx with Decisions, Actions, Proposals and Open_Questions sheets, transcript references and a Reviewed internal coordination state, plus work-c027/C027-Asteron-Verified-Actions.txt

## Prerequisites

- Use the trainer-provided Asteron synthetic meeting if available; follow organisational policy for transcription.
- If a live recap is unavailable, open asteron-teams-transcript.md in Copilot Chat within Teams and record the fallback.
- Open labs/assets/asteron-action-register-template.csv and asteron-teams-register-schemas.md.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Open the trainer-provided Asteron launch stand-up in Teams and select Recap and Copilot when available. If no permitted recap exists, upload or reference asteron-teams-transcript.md in Copilot Chat inside Teams. Record which path you used and the source date.

```text
Evidence path:
A = Teams recap from permitted synthetic meeting
B = Supplied synthetic transcript in Copilot Chat inside Teams
Never claim A when you used B
```

### 2. Ask Copilot to return four separate sections: Decisions, Actions, Proposals and Open questions. For Actions require Owner, Deliverable, Due_Date and Transcript_Evidence. Do not ask for a blended summary.

```text
Using only this meeting evidence, return Decisions | Actions | Proposals | Open questions. For each action give one named owner, one deliverable, one ISO due date and the exact transcript line or timestamp. Do not infer ownership or dates.
```

### 3. Open the transcript and verify every generated row. Correct the privacy sign-off owner, distinguish the proposed support clinic from confirmed launch work, and keep the room question open. Mark any row without exact evidence HOLD.

```text
Required evidence:
Nisha Rao - FAQ - 2026-08-11
Leon Wu - data export - 2026-08-13
Priya Menon - readiness dashboard - 2026-08-14 12:00
Farah Lim - privacy sign-off - 2026-08-15
Mei Tan - confirm support-clinic room - 2026-08-12
Pilot launch remains 2026-08-18 subject to privacy sign-off
```

### 4. Open asteron-action-register-template.csv in Excel and save as C027-Teams-Action-Register.xlsx. Create tables tblDecisions, tblActions, tblProposals and tblOpenQuestions on the four separate sheets specified in asteron-teams-register-schemas.md. Copy only verified rows, retain the evidence reference and set Status to Confirmed, Proposed or Open.

```text
Decisions: Decision_ID | Decision | Evidence | Status | Reviewer | Release_State
Actions: Action_ID | Deliverable | Owner | Due_Date | Evidence | Status | Reviewer | Release_State
Proposals: Proposal_ID | Proposal | Proposed_By | Target_Date | Evidence | Resolution_Owner | Status
Open Questions: Question_ID | Question | Resolution_Owner | Due_Date | Evidence | Status
```

### 5. Run a completeness check: every Confirmed action has one owner, one deliverable, one due date and evidence; Proposed items are not in the confirmed count; Open questions have an owner for resolution. Record reviewer, review date and state Reviewed for internal coordination. Export the confirmed action rows with owner, deliverable, due date and evidence to work-c027/C027-Asteron-Verified-Actions.txt for Lab 7.

```text
Expected confirmed work items = 5
Expected unresolved item = support-clinic room availability
Release state = Reviewed for internal coordination
```

## Test It

The register must contain all four required sheets/tables, the five required work items with exact owners and dates, plus one proposed clinic and one open room question. Every confirmed action must include transcript evidence, and the file must record whether the source was a Teams recap or the supplied transcript fallback. The release state must be Reviewed for internal coordination, and the verified-actions TXT export must contain only confirmed actions.

## Checkpoint and Rejoin Point

Save the action register and verified-actions TXT in work-c027. Lab 7 uses the supported TXT export plus the open question. Do not remove the evidence column when copying information into another app.

## Troubleshooting

| If this happens | Fix |
|---|---|
| The recap assigns an action to the wrong speaker. | Use the transcript speaker label and surrounding lines; correct the owner and record the generated attribution as REVISE. |
| A due date is missing from the evidence. | Set the action to HOLD and create an open question for the owner instead of inventing a date. |
| The live meeting cannot be transcribed. | Use the supplied synthetic transcript inside Teams and record the fallback. Do not change tenant policy or record without permission. |

## Challenge

Ask Copilot to identify two risks implied by the action register. Label them HYPOTHESIS and state which additional evidence would be required before they could become confirmed risks.

## Reflection

Which recap error would have caused the greatest coordination cost if it had entered the action register?

---

[← Lab 5](lab-05-summarise-the-launch-thread-and-prepare-a-reviewed-outlook-draft.md) · [Lab 7 →](lab-07-assemble-and-reconcile-the-cross-app-coordination-pack.md)
