# Lab 5 prompts

## Step 2

```text
EXCEL - PLAN:
Plan Dashboard for Northstar maintenance at 2026-09-30. Use selection cells B2:B5 for Site, Job_Category, Status, Assigned_To, all initially All. Reserve B7 total orders, B8 backlog, B9 overdue backlog, B10 closed, B11 on-time closure rate, B12 Cost_SGD. Place three charts for status, category and site with labels, units and scope. Preserve source data.
```

## Step 3

```text
EXCEL - ALLOW EDITING:
Build the planned six KPI formulas from tblWorkOrders. Backlog excludes Closed/Cancelled. Overdue also requires Due_Date < Control!B2. On-time rate counts Closed_Date <= Due_Date among Closed rows only, and shows N/A when none. Recorded cost sums Cost_SGD of all included statuses. Link to table columns, never a fixed 120-row range. Keep source data unchanged.
```

## Step 4

```text
EXCEL - ALLOW EDITING:
Create three editable bar or column charts using formula-backed summaries: work-order count by Status, by Job_Category and by Site. Each summary must reconcile to the total selected orders. Use white background, navy titles, blue/teal accents, readable labels and a visible reporting date. Do not use category counts as evidence of causes or use colour alone for status.
```

## Step 6

```text
EXCEL - CHAT ONLY:
Explain each Dashboard measure in plain English, including terminal statuses, strict overdue date rule, closed-only SLA denominator and meaning of recorded cost. Give one source-row example for overdue and one for on-time closure; cite Work_Order_ID. Do not guess a root cause or financial saving.
```