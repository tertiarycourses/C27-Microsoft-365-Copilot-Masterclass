# Lab 5 - Build Maintenance Dashboard Measures and Charts

**C27 | v2.0 | Topic 3 | 50 minutes**

[Instruction PDF](Lab-05-Instructions.pdf) · [Copy-ready prompts](sample-prompts.txt) · [Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md#lab-5)

## Goal

Northstar_Dashboard.xlsx with a Dashboard layout, six verified measures, three labelled charts and a measure dictionary ready for Lab 6 filters.

## What you will build

Northstar_Dashboard.xlsx with a Dashboard layout, six verified measures, three labelled charts and a measure dictionary ready for Lab 6 filters.

Use Excel Copilot to plan a maintenance dashboard for operations managers. Define the measures before designing the charts, then build source-linked KPI cards and a status, category and site chart. You will distinguish stock measures such as current backlog from flows such as closures, and avoid calling category frequency a root cause.

## Prerequisites

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Verified clean table from earlier labs or supplied clean checkpoint.

## Files

- [Mock workbook](data/Northstar_Work_Orders.xlsx): raw 122-row input in Lab 1, clean 120-row input elsewhere.
- [Clean CSV reference](data/Northstar_Work_Orders.csv) and [expected controls](data/verified-controls.json).
- [Rejoin workbook](checkpoints/Northstar_Verified_Checkpoint.xlsx) and [snapshot](checkpoints/Northstar_Verified_Snapshot.docx).
- [Templates](templates/) for the brief, slide deck, evidence and handoff.

## Steps

### 1. Step 1

Open templates/Northstar_Dashboard_Starter.xlsx and save as Northstar_Dashboard.xlsx in OneDrive. If continuing your own workbook, copy its CLEAN tblWorkOrders into the starter, keeping exact headers and table name; do not create a second table. The starter has a labelled blank Dashboard and four selection cells B2:B5, initially All.
### 2. Step 2

Read Control and confirm the fixed reporting date. Ask for a visual plan before edits. Keep source, Checks and Prompt_Log separate from the Dashboard view. A dashboard is a decision interface: each visual should answer a maintenance question rather than decorate the page.

```text
EXCEL - PLAN:
Plan Dashboard for Northstar maintenance at 2026-09-30. Use selection cells B2:B5 for Site, Job_Category, Status, Assigned_To, all initially All. Reserve B7 total orders, B8 backlog, B9 overdue backlog, B10 closed, B11 on-time closure rate, B12 Cost_SGD. Place three charts for status, category and site with labels, units and scope. Preserve source data.
```

### 3. Step 3

Ask Copilot to insert formulas for the six measures using structured table references. For now all selectors are All; in Lab 6 the same formulas must honour the four filters. Verify the denominator and use N/A, not 0%, if no Closed rows remain.

```text
EXCEL - ALLOW EDITING:
Build the planned six KPI formulas from tblWorkOrders. Backlog excludes Closed/Cancelled. Overdue also requires Due_Date < Control!B2. On-time rate counts Closed_Date <= Due_Date among Closed rows only, and shows N/A when none. Recorded cost sums Cost_SGD of all included statuses. Link to table columns, never a fixed 120-row range. Keep source data unchanged.
```

### 4. Step 4

Add formula-backed chart summaries for the six statuses, five categories and five sites. Use bar/column charts: category and site are nominal groups; a line chart would imply an order that is not present. Label count axes and avoid 3-D effects. Ask the skill for consistent style if available.

```text
EXCEL - ALLOW EDITING:
Create three editable bar or column charts using formula-backed summaries: work-order count by Status, by Job_Category and by Site. Each summary must reconcile to the total selected orders. Use white background, navy titles, blue/teal accents, readable labels and a visible reporting date. Do not use category counts as evidence of causes or use colour alone for status.
```

### 5. Step 5

In Checks confirm sum of each chart’s categories equals 120 with All filters. Compare six KPIs to Control and record the on-time numerator/denominator. Add templates/Evidence_Register.csv entries for each chart and metric. If Copilot has used hard-coded numbers, replace them with formulas before Lab 6.
### 6. Step 6

Create a measure dictionary on a new Measures sheet: metric, business definition, formula, source fields, date rule, scope and limitation. Ask Copilot to explain formulas, then read one overdue example and one closed example from the source table yourself. Save the baseline dashboard with all filters All.

```text
EXCEL - CHAT ONLY:
Explain each Dashboard measure in plain English, including terminal statuses, strict overdue date rule, closed-only SLA denominator and meaning of recorded cost. Give one source-row example for overdue and one for on-time closure; cite Work_Order_ID. Do not guess a root cause or financial saving.
```


## Test it

- Baseline: Total 120; backlog 60; overdue 50; closed 48.
- SLA and cost: 30/48 = 62.5%; S$35,827.50.
- Chart reconciliation: Three count summaries each total 120; formulas reference tblWorkOrders.
- Decision design: Measures dictionary and source/date visible; no unsupported cause claims.

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
