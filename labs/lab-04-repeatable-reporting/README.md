# Lab 4 - Use and Improve the Skill in Excel and PowerPoint

**C27 | v2.0 | Topic 2 | 40 minutes**

[Instruction PDF](Lab-04-Instructions.pdf) · [Copy-ready prompts](sample-prompts.txt) · [Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md#lab-4)

## Goal

Northstar_Skill_Report.xlsx with Maintenance_Summary and Assignment_Proposals, Northstar_Skill_Update.pptx, SKILL.md v2 and a before/after improvement log.

## What you will build

Northstar_Skill_Report.xlsx with Maintenance_Summary and Assignment_Proposals, Northstar_Skill_Update.pptx, SKILL.md v2 and a before/after improvement log.

Use the Lab 3 skill to create a verified summary and improve the initial PowerPoint update. Then deliberately test missing inputs and a rerun, tighten the skill to v2, and compare before/after evidence. The target is consistent reporting, not a longer prompt or an unsupported promise of autonomous approval.

## Prerequisites

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Lab 3 skill v1 and test record; Lab 2 update, or named supplied checkpoints.

## Files

- [Mock workbook](data/Northstar_Work_Orders.xlsx): raw 122-row input in Lab 1, clean 120-row input elsewhere.
- [Clean CSV reference](data/Northstar_Work_Orders.csv) and [expected controls](data/verified-controls.json).
- [Rejoin workbook](checkpoints/Northstar_Verified_Checkpoint.xlsx) and [snapshot](checkpoints/Northstar_Verified_Snapshot.docx).
- [Templates](templates/) for the brief, slide deck, evidence and handoff.

## Steps

### 1. Step 1

Copy the Lab 3 reviewed SKILL.md to your output folder and retain v1. Open this lab’s clean workbook or your Lab 1 cleaned workbook. Save as Northstar_Skill_Report.xlsx. Read Technicians: primary category and available hours are synthetic planning inputs, not approvals. Check that your skill is enabled in Excel.
### 2. Step 2

Invoke the skill in Plan or Chat only, review its proposed output boundaries, then allow editing. Inspect the resulting formulas and charts. Summary counts must reconcile to Control, and the source table must remain 120 unique records.

```text
EXCEL - PLAN:
@maintenance-reporting Build Maintenance_Summary for tblWorkOrders at 2026-09-30 with all filters All. Include total, closed, cancelled, backlog, overdue, on-time closed rate and recorded cost; show formulas and source scope. Plan first. Preserve source records.

EXCEL - ALLOW EDITING:
Apply that reviewed summary plan. Add Assignment_Proposals for unassigned backlog only. Use tblTechnicians primary category and available hours as planning inputs; show category/capacity checks, current owner and proposed owner separately. Leave manager decision UNKNOWN. Do not change Assigned_To.
```

### 3. Step 3

Check the unassigned backlog count against Control. A technician with the same category may still lack usable capacity: use available hours minus known proposed hours, flag conflicts, and do not convert a suggestion into confirmed assignment. Export your verified summary into the Word snapshot template, preserving measures and date.
### 4. Step 4

Open the four-slide initial update from Lab 2, or use checkpoints/Northstar_Initial_Update_Checkpoint.pptx, a four-slide rejoin example explicitly labelled as a checkpoint. Save as Northstar_Skill_Update.pptx. Select the reviewed snapshot in PowerPoint and invoke your installed skill.

```text
POWERPOINT COPILOT:
@maintenance-reporting Improve this existing initial maintenance update from the selected verified snapshot. Retain four slides and accurate values; strengthen claim headlines, simplify text, improve source notes and use the current design. Do not duplicate slides or imply live links to Excel. Label suggested reassignment as proposed.
```

### 5. Step 5

Create a new EMPTY workbook with no table, open a fresh Copilot chat and run a missing-input test for a different reporting period with no source selected. A proper skill asks for source/date/scope rather than inventing metrics. If it guesses, record the failure and revise the skill’s input guard. Return to Northstar_Skill_Report.xlsx and Save As Northstar_Skill_Rerun_Test.xlsx. Run the second summary request in this copy of the report workbook, not in the empty workbook; only named outputs may be replaced after review, with no duplicated source or output sheets. Compare a before/after copy of Work_Orders sorted by Work_Order_ID for status, owner, dates and cost; every original source value must match.

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Prepare my next maintenance report. I need a DIFFERENT reporting period from the course example and have not supplied any source, date or scope. This empty workbook contains no work orders. Tell me what you need; do not invent data.

EXCEL - PLAN:
@maintenance-reporting Rebuild the existing Maintenance_Summary for the same table, date and scope. Describe what will be replaced, ask before replacement and keep source/unrelated sheets. Do not duplicate outputs.
```

### 6. Step 6

In a plain text editor improve SKILL.md: require an input guard, category/capacity evidence, source provenance per claim and a clear rerun rule. Retain YAML name maintenance-reporting and add a body version note v2. Re-upload/Refresh in BOTH Excel and PowerPoint. Record actual before/after changes, or already present - retained for safeguards that your v1 already contains. Do not fabricate differences. Rerun the smoke tests and compare values. If using the manual route, replace the pasted instructions in both apps.

## Test it

- Source preserved: 120 unique orders; current owner/status unchanged.
- Skill outputs: Backlog 60; overdue 50; on-time closed 30/48; cost S$35,827.50.
- Improvement evidence: Input guard and rerun tested; v1/v2 retained; PowerPoint four-slide output accurate.

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
