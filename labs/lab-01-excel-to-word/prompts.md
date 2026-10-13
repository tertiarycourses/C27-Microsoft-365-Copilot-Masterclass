# Lab 1 prompts

## Step 2

```text
EXCEL - CHAT ONLY:
Inspect tblWorkOrders. Report row count, duplicate Work_Order_ID values, category spelling variants and missing Assigned_To. Do not edit. Treat 2026-09-30 as the fixed reporting date.
```

## Step 3

```text
EXCEL - PLAN:
Plan to retain an untouched Raw_Export copy, remove only exact duplicate records by Work_Order_ID, and standardise category spelling in tblWorkOrders. Keep dates, statuses and assignments. Ask if two records with one ID differ.

EXCEL - ALLOW EDITING:
Apply the reviewed plan. Keep one identical record per repeated ID. Do not guess missing owners. Reconcile the cleaned table against Control.
```

## Step 4

```text
EXCEL - ALLOW EDITING:
In Checks calculate total rows, closed, cancelled, backlog, overdue backlog, unassigned backlog and total Cost_SGD for tblWorkOrders. Use Control!B2 as reporting date. Define backlog as Status neither Closed nor Cancelled. Add the identity total = closed + cancelled + backlog. Do not change source data.
```

## Step 5

```text
WORD COPILOT:
Draft a one-page Northstar operations brief from the verified evidence supplied here. Include reporting scope/date, backlog and overdue findings, current assignment issues, proposed next actions and open questions. Keep observed facts separate from proposals. Preserve numbers and definitions. Use UNKNOWN for causes, approvals or capacity decisions not evidenced.
```