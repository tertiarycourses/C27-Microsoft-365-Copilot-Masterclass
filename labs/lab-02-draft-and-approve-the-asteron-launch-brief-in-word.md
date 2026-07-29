# Lab 2 — Draft and Approve the Asteron Launch Brief in Word

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Microsoft 365 Copilot  
**Maps to:** LO2: draft a source-grounded business document in Word, apply a bounded rewrite and validate the final version against the source register and audience brief  
**Duration:** 40 minutes  
**Tools:** Word for Microsoft 365 · Copilot in Word · C027-Asteron-Verified-Claims.txt · C027-Asteron-Source-Register.xlsx

---

## Goal

Produce an approved launch brief of no more than two pages whose facts, open questions and call to action agree with the verified source register.

## What You Will Do

You will create a Word document for Asteron department heads, use the supported verified-claims TXT export as the Copilot reference, then review the generated draft against the source register and project brief line by line. You will use Copilot to rewrite one selected passage without changing scope, commitments or unresolved items.

## What You Will Build

work-c027/C027-Asteron-Launch-Brief-v1.0.docx with five required sections, source notes, an Open Questions box and an Approved for deck handoff record

## Prerequisites

- Completed Lab 1 workbook and C027-Asteron-Verified-Claims.txt export.
- Open labs/assets/asteron-word-brief-spec.md and labs/assets/asteron-style-guide.md.
- Keep the support-clinic room as an open question; no source approves it.
- For this simulation, the learner is the document owner and supplies the owner review; trainer feedback may supplement it.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Create a blank Word document in work-c027 and save it as C027-Asteron-Launch-Brief-v1.0.docx. Add a title, document owner, version, date and a status line set to Draft. Insert the five required headings from the brief specification before generating any body text.

```text
Required headings:
1. Purpose and Audience
2. Confirmed Launch Position
3. Readiness and Dependencies
4. Decisions and Owners
5. Open Questions and Next Actions
```

### 2. Open Copilot in Word and reference C027-Asteron-Verified-Claims.txt from Lab 1. Submit the prompt below. Word's referenced drafting accepts this supported TXT handoff; do not cite the Excel workbook as if Copilot in Word read it. Use the workbook and project brief for the manual source review in Step 3.

```text
GOAL: Draft an Asteron client portal pilot launch brief of no more than two pages.
CONTEXT: Department heads need the confirmed position, named owners and decisions needed before 2026-08-18.
SOURCE: Use only the referenced C027-Asteron-Verified-Claims.txt export. Preserve items explicitly labelled Proposed or Open; the export contains no unsupported HOLD rows.
EXPECTATIONS: Use the five existing headings, concise professional language, bullets for owners, ISO dates, and source notes in [Source_ID] form. Do not add market claims or present proposals as confirmed.
```

### 3. Review the draft against the source register. Highlight every date, number, owner and commitment. Add a Word comment containing the governing Source_ID, then set the review decision to Keep, Change or Remove. Correct any unsupported language before continuing.

```text
Required trace points:
2026-08-18 launch date
20 internal participants
five departments
Nisha Rao / FAQ / 2026-08-11
Leon Wu / export / 2026-08-13
privacy sign-off before external announcement
```

### 4. Select the Readiness and Dependencies section only. Ask Copilot to make it more concise for senior leaders while preserving every fact and the distinction between confirmed and proposed. Compare the before and after text and reject any change to scope, date, owner or status.

```text
Rewrite this selected section to no more than 90 words for department heads. Preserve all dates, owners, scope and status labels exactly. Keep the support clinic room as an open question. Do not introduce new commitments.
```

### 5. Insert a two-column release table at the end with Check and Result. Complete Source fidelity, Audience fit, Scope, Open questions, Privacy, Accessibility and Owner approval. As the lab document owner, enter your name and review date for Owner approval. Change the document status to Approved for deck handoff only when all required checks are complete; this is a simulated workflow state, not organisational approval. Save and close the file.

```text
Release states:
APPROVED = evidence and audience checks complete
REVISE = correctable content or format gap
HOLD = unsupported fact, unsafe disclosure or unresolved release decision
```

## Test It

The Word file must contain exactly the five required headings and remain within two pages including the release table. Every material date, number, owner and commitment must trace to a Source_ID. The launch date must be 2026-08-18, the data export 2026-08-13 and the support-clinic room must remain open. The title block must show v1.0 and Approved for deck handoff.

## Checkpoint and Rejoin Point

Save the approved Word brief in work-c027. Lab 3 uses this exact version as the governing PowerPoint source. If the status is REVISE or HOLD, correct the document before continuing.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Copilot changes a confirmed fact during rewrite. | Reject the rewrite, narrow the selected text and state which terms, dates and statuses must remain exact. |
| The document is longer than two pages. | Remove duplication, convert owner details to a compact table and shorten explanation without removing evidence or open questions. |
| A source note points to the wrong file. | Return to tblClaims, identify the governing Source_ID and correct both the note and any affected wording. |

## Challenge

Ask Copilot in Chat-only mode to pressure-test the brief from a department head's perspective. Add only questions that expose a genuine evidence gap; do not let speculative questions become new facts.

## Reflection

What is the difference between improving a sentence and changing the commitment expressed by that sentence?

---

[← Lab 1](lab-01-research-the-asteron-launch-and-build-a-verified-source-register.md) · [Lab 3 →](lab-03-generate-and-refine-the-asteron-decision-deck-in-powerpoint.md)
