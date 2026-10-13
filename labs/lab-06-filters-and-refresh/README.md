# Lab 6 - Make the Dashboard Interactive and Prove Refresh

**C27 | v2.0 | Topic 3 | 50 minutes**

[Instruction PDF](Lab-06-Instructions.pdf) · [Copy-ready prompts](sample-prompts.txt) · [Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md#lab-6)

## Goal

Northstar_Dashboard.xlsx with four working filters plus Northstar_Dashboard_Refresh_Test.xlsx, filter evidence and a verified baseline snapshot for PowerPoint.

## What you will build

Northstar_Dashboard.xlsx with four working filters plus Northstar_Dashboard_Refresh_Test.xlsx, filter evidence and a verified baseline snapshot for PowerPoint.

Continue Lab 5 by making four dropdown selectors control every KPI and chart. Test a single site, a zero-denominator selection and a combined category/owner filter. Then append two synthetic work orders in a sandbox copy and prove the dashboard expands. Optional PivotTable slicers use one source and shared connections; the portable dropdown route is the required working dashboard.

## Prerequisites

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Lab 5 dashboard or supplied formula checkpoint.

## Files

- [Mock workbook](data/Northstar_Work_Orders.xlsx): raw 122-row input in Lab 1, clean 120-row input elsewhere.
- [Clean CSV reference](data/Northstar_Work_Orders.csv) and [expected controls](data/verified-controls.json).
- [Rejoin workbook](checkpoints/Northstar_Verified_Checkpoint.xlsx) and [snapshot](checkpoints/Northstar_Verified_Snapshot.docx).
- [Templates](templates/) for the brief, slide deck, evidence and handoff.

## Steps

### 1. Step 1

Open your Lab 5 baseline dashboard. Rejoin using checkpoints/Northstar_Verified_Checkpoint.xlsx only if needed; record that it is an example formula dashboard. Set all four selections B2:B5 to All and confirm 120. Save baseline before creating any refresh-test copy.
### 2. Step 2

Use Data > Data Validation > Allow List to set dropdowns on B2 Site, B3 Job_Category, B4 Status and B5 Assigned_To. Include All plus the source values, using Filter_Lists if supplied. Ask Copilot to apply all four selections to EVERY KPI and chart summary. A selection of All bypasses only that filter; selected dimensions combine with AND.

```text
EXCEL - PLAN:
Make Dashboard B2:B5 control all six KPIs and three chart summaries with AND logic. All bypasses its dimension. Use COUNTIFS/SUMIFS or SUMPRODUCT with structured table references. Blank owner means unassigned and must not disappear from All. Keep N/A for no closed jobs.

EXCEL - ALLOW EDITING:
Apply the reviewed filter plan and dropdown lists. Keep existing source rows and chart positions. Show the selected scope beside the reporting date and make all charts recalculate from the same selected rows.
```

### 3. Step 3

Choose Woodlands Hub in B2 and leave other selectors All. Filter the source table to the same site and compare rows, backlog, overdue and cost. Use Data > Clear on source table afterwards; dashboard selectors and source AutoFilter are distinct mechanisms. Record evidence in templates/Filter_Test_Log.csv.

```text
EXCEL - CHAT ONLY:
For the dashboard selection Site = Woodlands Hub and all other dimensions All, list the expected six KPI values from tblWorkOrders and verify each chart sum matches the selected total. Do not infer that filtering the worksheet automatically changes formula measures.
```

### 4. Step 4

Set Status to New with other selectors All. Confirm zero closed -> N/A. Then set Site = Woodlands Hub, Job_Category = HVAC, Assigned_To = Daniel Lee, Status = All, a combination with no rows; total, backlog, overdue, closed and cost must be 0 and rate N/A. Reset all four to All and verify baseline controls. Optional: create PivotTables from one tblWorkOrders source, insert slicers, and use Slicer > Report Connections for every PivotTable; unconnected KPI cells are a defect.
### 5. Step 5

Save a COPY as Northstar_Dashboard_Refresh_Test.xlsx. In the last row of tblWorkOrders press Tab to append, then enter the two rows from data/Refresh_Test_Rows.csv with real Excel dates (YYYY-MM-DD). WO-2026-0121 is Assigned, due 2026-09-29 and cost 150; WO-2026-0122 is Closed on time and cost 250. No existing IDs are edited.
### 6. Step 6

Recalculate with all selections All. If using PivotTables also Data > Refresh All and inspect source extent. Verify total122, closed49, backlog61, overdue baseline+1, cost baseline+400 and on-time numerator baseline+1 over49. If formulas do not expand, fix structured references/table extent. Keep this sandbox copy as refresh evidence; do not use its figures in the baseline presentation.

```text
EXCEL - CHAT ONLY:
Verify the sandbox append test for the two new work orders. Reconcile total 122, closed 49, backlog 61, overdue increased by 1, cost increased by S$400 and on-time numerator increased by 1. Confirm no original source record changed and all three charts total 122 with All selections. Compare original IDs, statuses, owners, dates and costs to the saved baseline; all original 120 rows must match.
```

### 7. Step 7

Return to the untouched 120-row Northstar_Dashboard.xlsx. Set selectors All and record a frozen evidence snapshot dated 2026-09-30 for Lab 7. Copy templates/Northstar_Operations_Brief_Template.docx to Northstar_Verified_Snapshot.docx in Word and insert the reviewed summary and chart values. Save chart images if needed with right-click chart > Save as Picture; the slide copy will be a static snapshot, not a live dashboard.

## Test it

- Woodlands control: Total 24; backlog 8; overdue 7; closed 16; cost S$6,668.50; on-time 10/16.
- Interactive scope: Changing any of four filters affects all six KPI measures and all chart counts.
- Edge case: No Closed -> N/A; no rows -> zero count/cost and N/A rate.
- Refresh sandbox: 122 total;49 closed;61 backlog;51 overdue;S$36,227.50;31/49 on-time.
- Handoff baseline: Return to 120-row untouched baseline; date and All scope recorded.

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
