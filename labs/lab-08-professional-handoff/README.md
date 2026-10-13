# Lab 8 - Refine and Present the Maintenance Decision Deck

**C27 | v2.0 | Topic 4 | 45 minutes**

[Instruction PDF](Lab-08-Instructions.pdf) · [Copy-ready prompts](sample-prompts.txt) · [Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md#lab-8)

## Goal

Northstar_Management_Final.pptx/PDF, a rehearsal record, final evidence register and unsent Outlook handoff draft with accurate artifact links.

## What you will build

Northstar_Management_Final.pptx/PDF, a rehearsal record, final evidence register and unsent Outlook handoff draft with accurate artifact links.

Refine the management deck using the same custom skill and reviewed dashboard evidence. Improve hierarchy, consistency and speaker notes, test the story in a short rehearsal, and prepare a reviewed Outlook handoff draft. The final pack preserves the distinction between a static presentation snapshot, a refreshable dashboard and a manager’s unmade decision.

## Prerequisites

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Lab 7 management draft, reviewed presentation brief and evidence register.

## Files

- [Mock workbook](data/Northstar_Work_Orders.xlsx): raw 122-row input in Lab 1, clean 120-row input elsewhere.
- [Clean CSV reference](data/Northstar_Work_Orders.csv) and [expected controls](data/verified-controls.json).
- [Rejoin workbook](checkpoints/Northstar_Verified_Checkpoint.xlsx) and [snapshot](checkpoints/Northstar_Verified_Snapshot.docx).
- [Templates](templates/) for the brief, slide deck, evidence and handoff.

## Steps

### 1. Step 1

Open your Lab 7 draft and save as Northstar_Management_Final.pptx. Rejoin only if necessary using checkpoints/Northstar_Management_Example.pptx and snapshot; review and adapt its supplied example charts and narrative against the verified snapshot. Open the same reviewed brief in the file picker; confirm native skill or label manual practice.
### 2. Step 2

Ask the skill to audit before editing. It should report crowded slides, weak evidence, missing labels and inconsistent scope. Review the list yourself against the evidence register; styling changes must never change values.

```text
POWERPOINT COPILOT:
@maintenance-reporting Audit this eight-slide deck against the selected verified Northstar brief. List inaccurate figures, ambiguous units, date/scope omissions, unsupported causal or approval wording, dense text and weak hierarchy. Propose corrections; do not change values or source facts.
```

### 3. Step 3

Apply only the reviewed corrections. Keep white/navy/blue with teal highlights, one main message, readable labels, consistent chart formats and source notes. Ask for concise speaker notes; check that notes do not introduce new numbers or promise assignment approvals.

```text
POWERPOINT COPILOT:
@maintenance-reporting Apply the reviewed design and wording corrections to the existing eight slides. Improve hierarchy and whitespace, make titles claim-led, retain accurate figures and charts, and add 45-second speaker notes per slide. Separate observed findings from proposed actions and end with the decision requested. Preserve the baseline date/scope; do not duplicate slides.
```

### 4. Step 4

Use Slide Show to inspect at presentation size. Run a five-minute rehearsal with a partner or PowerPoint Rehearse with Coach if available. Ask the partner to identify the reporting date, highest-priority evidence and decision requested. Record one actual change in templates/Rehearsal_Log.csv; do not fabricate feedback.
### 5. Step 5

Export File > Export or Save As > PDF. Open the PDF and verify eight pages, readable charts and all visible values. Compare PPTX, PDF, Word brief and dashboard against the evidence register. Keep the source workbook with All filters and the archived refresh-test copy separately.
### 6. Step 6

Open Outlook and create a draft to operations.manager@example.invalid. Provide the reviewed brief and the actual OneDrive links to the dashboard/deck. Ask Copilot to draft a handoff email; it may not invent shared links or claim a sent attachment. Keep the email unsent and save a local reviewed TXT copy.

```text
OUTLOOK COPILOT:
Draft a short Northstar management handoff email using this verified brief and the links I provide. State the 30 September 2026 baseline scope, headline findings, proposed actions and decision required. Explain that the PowerPoint/PDF is a static snapshot while the Excel dashboard is interactive. Leave missing links UNKNOWN. Do not claim approval or send the draft.
```

### 7. Step 7

Complete templates/Final_Handoff_Checklist.csv: workbook source and controls, working filters, sandbox refresh proof, skillv2 installation/manual record, eight-slide PPTX/PDF, reviewed notes, evidence register and unsent draft. Record the exact filenames and your actual checks. Save the final pack in work-c027.

## Test it

- Presentation integrity: Eight slides and eight PDF pages; visible figures agree with verified register.
- Professional delivery: Readable chart labels, consistent design, evidence-specific notes and actual rehearsal improvement.
- Final continuity: Baseline dashboard, brief, deck and unsent draft agree; static snapshot stated.
- Decision boundary: No real email sent or work order reassigned; proposed actions remain proposed.

## Checkpoint

If you fell behind, use checkpoints/Northstar_Verified_Checkpoint.xlsx and checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

## Troubleshooting

- Copilot cannot find the source: Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app.
- A total disagrees with Control: Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing.
- The named feature is missing: Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran.

## Challenge

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

## Reflection

Which evidence proves the output is correct, and which decision still needs a person?

Northstar Facilities, all sites, staff and work orders are fictional. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.
