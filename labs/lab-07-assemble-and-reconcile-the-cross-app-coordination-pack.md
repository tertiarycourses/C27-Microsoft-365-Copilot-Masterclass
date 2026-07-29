# Lab 7 — Assemble and Reconcile the Cross-App Coordination Pack

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Copilot Across Your Everyday Work Apps  
**Maps to:** LO4: connect approved outputs across Microsoft 365 apps using handoff contracts and reconcile repeated facts, owners, measures and release states  
**Duration:** 45 minutes  
**Tools:** Microsoft 365 Copilot Chat · Word · Excel · PowerPoint · Outlook · Teams

---

## Goal

Create a cross-app manifest and concise coordination pack in which every repeated fact agrees with the governing artifact.

## What You Will Do

You will register the Chat, Word, PowerPoint, Excel, Outlook and Teams outputs, declare which artifact governs each type of information, then use Copilot to draft a coordination update. A consistency matrix will expose any date, owner, number or status that drifted during an app handoff.

## What You Will Build

work-c027/C027-Asteron-Cross-App-Manifest.xlsx and C027-Asteron-Coordination-Pack.docx with authoritative-source links, a consistency matrix and an Approved internal handoff state

## Prerequisites

- Labs 1-6 outputs are saved in work-c027 with their stated release records; if one is unavailable, use the versioned trainer-validated labs/assets/asteron-capstone-rejoin-pack.txt and record the substitution.
- Do not use an artifact that remains REVISE; HOLD artifacts can be registered but cannot govern released facts.
- Open the partially populated asteron-cross-app-manifest-template.csv and asteron-consistency-matrix-template.csv.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Open asteron-cross-app-manifest-template.csv in Excel and save as C027-Asteron-Cross-App-Manifest.xlsx. Enter one row for the source register, Word brief, PowerPoint deck, Excel readiness workbook, Outlook review and draft, and Teams action register. Record file link, version, owner, purpose, source authority, state and next use. Complete Source_Coverage as Learner-created checkpoint or Trainer-validated practice fallback. Timebox: 5 minutes; fill placeholders in the six pre-populated rows rather than rebuilding the table.

```text
Required artifacts = 6
Allowed states = Draft | Reviewed | Approved | Hold
No blank owner, purpose or next use
Outlook draft remains Hold
```

### 2. Create an Authority sheet. Declare that the source register governs confirmed launch facts, the Word brief governs the narrative, Excel governs cohort measures, Teams governs meeting actions and the Outlook thread governs email history. PowerPoint may communicate facts but does not replace its sources. Timebox: 5 minutes.

```text
Authority map:
Launch facts -> Source register
Narrative -> Approved Word brief
Readiness measures -> Verified Excel workbook
Meeting actions -> Teams action register
Email history -> Outlook thread review
```

### 3. In Microsoft 365 Copilot Chat, reference the approved Word brief, C027-Asteron-Verified-Readiness-Summary.txt and C027-Asteron-Verified-Actions.txt. If any normal input is missing, reference asteron-capstone-rejoin-pack.txt instead and name only the applicable WORD BRIEF, EXCEL READINESS or TEAMS substitute section. Ask for the bounded draft below; review it, then paste the accepted text into C027-Asteron-Coordination-Pack.docx with sections Executive position, Readiness, Confirmed actions, Open questions and Artifact links. Do not ask Copilot in Word to read Excel workbooks, and do not use the held Outlook draft as a factual source. Timebox: 12 minutes.

```text
GOAL: Draft a two-page internal coordination update.
CONTEXT: Asteron department heads need the launch position, readiness measures, actions and open questions.
SOURCE: Use the approved Word brief and the two referenced verified TXT exports only.
EXPECTATIONS: Preserve ISO dates and owners; cite the governing artifact after every section; distinguish Confirmed, Proposed and Open; include 14/16 attendance, 12/16 training completion and four high-priority participants.
```

### 4. Copy the nine pre-populated rows from asteron-consistency-matrix-template.csv into a Consistency sheet. Fill only the applicable artifact cells and compare the source register, Word brief, deck, Excel workbook, Outlook review, Teams register and coordination pack. Use N/A where a fact does not belong. Timebox: 15 minutes.

```text
Required consistency rows:
Launch 2026-08-18 | Cohort 20 / five departments
FAQ Nisha Rao / 2026-08-11 | Export Leon Wu / 2026-08-13
Privacy sign-off before external announcement | Clinic proposed / room open
Attendance 14/16 (87.5%) | Training 12/16 (75.0%) | High priority 4
```

### 5. Correct every mismatch in the downstream artifact, not in the governing source. Update the manifest with the reviewed version and state. In the coordination pack add a release table with Source coverage, Fact consistency, Permissions, Audience, Owner and Decision. Set the pack to Approved internal handoff only when all consistency rows agree. Timebox: 8 minutes.

```text
Final conditions:
Consistency_Result = MATCH for every required row
Coordination pack = Approved internal handoff
Outlook draft = Hold until Lab 8 release review
No artifact is marked Approved without a named reviewer
```

## Test It

The manifest must contain six artifact rows with links, owners, versions and states. The authority map must name one governing artifact for each information type. Every required consistency row must show MATCH across all artifacts where the fact appears. The coordination pack must be no more than two pages, cite its source artifacts and be Approved internal handoff; the Outlook draft must remain Hold. Any substituted prior output must be visibly marked REJOIN-PACK-v1.0 and Trainer-validated practice fallback.

## Checkpoint and Rejoin Point

Save the manifest and coordination pack. Lab 8 applies the final responsible-use and privacy review before the workflow is considered ready for controlled internal use. If an earlier artifact is missing or still blocked, copy the relevant section from asteron-capstone-rejoin-pack.txt, set its manifest Link to REJOIN-PACK-v1.0, record Trainer-validated practice fallback as coverage and continue; replace it later when the learner-created artifact passes its checkpoint.

## Troubleshooting

| If this happens | Fix |
|---|---|
| A downstream artifact contains an older date. | Confirm the governing source, correct the downstream file, update its version and rerun the consistency row. |
| Copilot cannot reference all three source files at once. | Draft one section per supported Word/TXT reference in Microsoft 365 Copilot Chat, then assemble and reconcile manually. Record actual source coverage; never imply an Excel workbook was read when it was not. |
| Two files appear to govern the same fact. | Choose the artifact closest to the approved source of that information and record the decision in the Authority sheet. |

## Challenge

Draw a simple lineage diagram from source register and raw cohort through each downstream artifact. Mark where an error could propagate to three or more outputs and add one preventive check at that handoff.

## Reflection

Which handoff carried the greatest risk of multiplying an early error, and which checkpoint contained it?

---

[← Lab 6](lab-06-validate-a-teams-recap-and-create-the-action-register.md) · [Lab 8 →](lab-08-run-the-responsible-use-and-privacy-release-gate.md)
