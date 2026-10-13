# Lab 7 - Turn Dashboard Evidence into a Management Story

**C27 | v2.0 | Topic 4 | 45 minutes**

[Instruction PDF](Lab-07-Instructions.pdf) · [Copy-ready prompts](sample-prompts.txt) · [Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md#lab-7)

## Goal

Northstar_Presentation_Brief.docx, Northstar_Management_Draft.pptx and a slide-by-slide evidence register tied to the 120-row dashboard snapshot.

## What you will build

Northstar_Presentation_Brief.docx, Northstar_Management_Draft.pptx and a slide-by-slide evidence register tied to the 120-row dashboard snapshot.

Continue the baseline dashboard from Topic 3. Build a slide evidence register and a Word presentation brief before asking PowerPoint Copilot for an eight-slide management deck. The story connects work-order status, site backlog, service delivery and assignment proposals to a specific decision; it does not introduce unsupported savings or causes.

## Prerequisites

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Verified Lab 6 baseline dashboard and frozen evidence snapshot.

## Files

- [Mock workbook](data/Northstar_Work_Orders.xlsx): raw 122-row input in Lab 1, clean 120-row input elsewhere.
- [Clean CSV reference](data/Northstar_Work_Orders.csv) and [expected controls](data/verified-controls.json).
- [Rejoin workbook](checkpoints/Northstar_Verified_Checkpoint.xlsx) and [snapshot](checkpoints/Northstar_Verified_Snapshot.docx).
- [Templates](templates/) for the brief, slide deck, evidence and handoff.

## Steps

### 1. Step 1

Open the untouched baseline Northstar_Dashboard.xlsx from Lab 6; confirm All selectors, total120 and report date2026-09-30. Do not use the 122-row sandbox. If needed use this lab’s checkpoint and record rejoin. Copy verified metric/chart values to templates/Slide_Evidence_Register.csv with source sheet/table, scope and date.
### 2. Step 2

Open templates/Northstar_Presentation_Brief_Template.docx in Word. Add the verified summary and chart values plus the OneDrive workbook link. Save as Northstar_Presentation_Brief.docx. Copilot must see selected files or pasted evidence; the link alone and the Excel conversation do not guarantee accessible context.

```text
WORD COPILOT:
Using this verified 120-row Northstar maintenance snapshot, draft an eight-slide management presentation brief. For each slide give one claim headline, supporting measure/chart, source/date/scope, limitation and speaker note. Structure: overview, portfolio, site backlog, status/category mix, SLA/overdue, assignment/capacity, proposed actions/trade-offs, decision/next review. Do not invent causes, savings, approval or future dates; use UNKNOWN when absent.
```

### 3. Step 3

Review the brief against source values. A bar showing counts by site is not a severity index; if you want backlog by site, count only nonterminal statuses. Correct any misleading headline and fill the slide evidence register. Suggested actions must cite a finding and say proposed.
### 4. Step 4

Open the supplied PowerPoint template, save as Northstar_Management_Draft.pptx and open Copilot. Choose Create presentation from file if offered, or reference the Word brief while editing the existing deck. Select your reviewed OneDrive Word brief; direct workbook-to-deck creation is not assumed. Invoke @maintenance-reporting if available.

```text
POWERPOINT COPILOT:
@maintenance-reporting Create or update an eight-slide management presentation from the selected Northstar_Presentation_Brief.docx. Follow the existing white/navy/blue template. One evidence-based message per slide, short visible text, charts or tables for numerical evidence, source/as-at/scope in notes, and a final decision request. Keep values exact, and label all next actions as proposed. Do not add extra slides or invented facts.
```

### 5. Step 5

Replace approximate or invented charts with your reviewed Excel charts: copy chart in Excel, then PowerPoint Home > Paste > Paste Special > Microsoft Excel Chart Object for an editable embedded chart when supported; otherwise paste a static image and label it snapshot. Embedded copies and images do not automatically follow the original workbook. Use direct verified values if a chart object is unsupported.
### 6. Step 6

Inspect all eight slides and notes. Check chart title, axis, unit, status definition, date and scope. Each numeric headline must match one register row. Confirm the deck uses baseline120, not refresh122. Save for Lab 8; do not represent the draft as an approved plan.

## Test it

- Evidence continuity: Every deck figure maps to the 120-row Lab 6 baseline and slide evidence register.
- Eight-slide narrative: Observation -> implication -> proposed action -> decision; no invented cause/savings.
- Chart semantics: Backlog charts exclude Closed/Cancelled; embedded/image copies labelled snapshot.

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
