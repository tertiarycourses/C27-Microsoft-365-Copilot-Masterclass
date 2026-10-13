# Microsoft 365 Copilot Masterclass - Prompt Library

Each prompt states its app. Copy one block at a time. Provide the actual selected file or pasted verified evidence; another app chat is not shared context.


## Lab 1

**Prepare Work Orders and Draft the Operations Brief** · [Lab folder](../../labs/lab-01-excel-to-word/README.md)

### Step 2

```text
EXCEL - CHAT ONLY:
Inspect tblWorkOrders. Report row count, duplicate Work_Order_ID values, category spelling variants and missing Assigned_To. Do not edit. Treat 2026-09-30 as the fixed reporting date.
```

### Step 3

```text
EXCEL - PLAN:
Plan to retain an untouched Raw_Export copy, remove only exact duplicate records by Work_Order_ID, and standardise category spelling in tblWorkOrders. Keep dates, statuses and assignments. Ask if two records with one ID differ.

EXCEL - ALLOW EDITING:
Apply the reviewed plan. Keep one identical record per repeated ID. Do not guess missing owners. Reconcile the cleaned table against Control.
```

### Step 4

```text
EXCEL - ALLOW EDITING:
In Checks calculate total rows, closed, cancelled, backlog, overdue backlog, unassigned backlog and total Cost_SGD for tblWorkOrders. Use Control!B2 as reporting date. Define backlog as Status neither Closed nor Cancelled. Add the identity total = closed + cancelled + backlog. Do not change source data.
```

### Step 5

```text
WORD COPILOT:
Draft a one-page Northstar operations brief from the verified evidence supplied here. Include reporting scope/date, backlog and overdue findings, current assignment issues, proposed next actions and open questions. Keep observed facts separate from proposals. Preserve numbers and definitions. Use UNKNOWN for causes, approvals or capacity decisions not evidenced.
```


## Lab 2

**Create the Cross-App Maintenance Update** · [Lab folder](../../labs/lab-02-word-to-powerpoint-and-outlook/README.md)

### Step 2

```text
POWERPOINT COPILOT:
Using this verified Northstar Word brief, create a four-slide initial update: scope and portfolio; backlog and overdue work; current assignments and proposed actions; decision required. Use the existing white/navy/blue design. Preserve all verified metrics. Add source/date notes. Do not invent completed work, savings or approved reassignment.
```

### Step 4

```text
OUTLOOK COPILOT:
Draft a concise reply to the synthetic thread quoted below, using the verified Northstar brief and these checked metrics. State the 30 September 2026 scope, backlog/overdue findings, proposed next actions and the decision requested. Explain that assignments are unapproved proposals. Do not claim the attachments have been sent. Keep as a draft.
```

### Step 6

```text
WORD COPILOT:
Compare these pasted PowerPoint and Outlook summaries with this verified Word brief. List inconsistent figures, status definitions, dates, owner claims or approved-action wording. Do not resolve a conflict by guessing. Return a discrepancy table with source and correction needed.
```


## Lab 3

**Create a Custom Maintenance Reporting Skill** · [Lab folder](../../labs/lab-03-author-skill-md/README.md)

### Step 1

```text
MICROSOFT 365 COPILOT WEB:
Write a complete SKILL.md for maintenance-reporting. Require YAML name and description, input table or verified Word snapshot, report date and filter scope. Define backlog, overdue and on-time closed rate. Preserve IDs/status/current owners. Put assignment suggestions in a separate proposals sheet. Support Excel outputs and PowerPoint storytelling with source notes, existing white/navy/blue style, no invented facts and safe reruns. Never send email or approve assignments. Ask for missing inputs. Return the entire Markdown file.
```

### Step 4

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Explain the reporting definitions for tblWorkOrders at 2026-09-30, all filters All. State which sheets you may change, how missing owners are handled, and what you need before producing a PowerPoint update. Do not edit yet.
```

### Step 6

```text
POWERPOINT COPILOT:
@maintenance-reporting Using the selected Northstar_Verified_Snapshot.docx, propose an eight-slide maintenance report outline. Explain how every claim will be grounded and which actions remain proposals. Keep the reporting date and scope visible; do not edit slides yet.
```


## Lab 4

**Use and Improve the Skill in Excel and PowerPoint** · [Lab folder](../../labs/lab-04-repeatable-reporting/README.md)

### Step 2

```text
EXCEL - PLAN:
@maintenance-reporting Build Maintenance_Summary for tblWorkOrders at 2026-09-30 with all filters All. Include total, closed, cancelled, backlog, overdue, on-time closed rate and recorded cost; show formulas and source scope. Plan first. Preserve source records.

EXCEL - ALLOW EDITING:
Apply that reviewed summary plan. Add Assignment_Proposals for unassigned backlog only. Use tblTechnicians primary category and available hours as planning inputs; show category/capacity checks, current owner and proposed owner separately. Leave manager decision UNKNOWN. Do not change Assigned_To.
```

### Step 4

```text
POWERPOINT COPILOT:
@maintenance-reporting Improve this existing initial maintenance update from the selected verified snapshot. Retain four slides and accurate values; strengthen claim headlines, simplify text, improve source notes and use the current design. Do not duplicate slides or imply live links to Excel. Label suggested reassignment as proposed.
```

### Step 5

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Prepare my next maintenance report. I need a DIFFERENT reporting period from the course example and have not supplied any source, date or scope. This empty workbook contains no work orders. Tell me what you need; do not invent data.

EXCEL - PLAN:
@maintenance-reporting Rebuild the existing Maintenance_Summary for the same table, date and scope. Describe what will be replaced, ask before replacement and keep source/unrelated sheets. Do not duplicate outputs.
```


## Lab 5

**Build Maintenance Dashboard Measures and Charts** · [Lab folder](../../labs/lab-05-design-and-build/README.md)

### Step 2

```text
EXCEL - PLAN:
Plan Dashboard for Northstar maintenance at 2026-09-30. Use selection cells B2:B5 for Site, Job_Category, Status, Assigned_To, all initially All. Reserve B7 total orders, B8 backlog, B9 overdue backlog, B10 closed, B11 on-time closure rate, B12 Cost_SGD. Place three charts for status, category and site with labels, units and scope. Preserve source data.
```

### Step 3

```text
EXCEL - ALLOW EDITING:
Build the planned six KPI formulas from tblWorkOrders. Backlog excludes Closed/Cancelled. Overdue also requires Due_Date < Control!B2. On-time rate counts Closed_Date <= Due_Date among Closed rows only, and shows N/A when none. Recorded cost sums Cost_SGD of all included statuses. Link to table columns, never a fixed 120-row range. Keep source data unchanged.
```

### Step 4

```text
EXCEL - ALLOW EDITING:
Create three editable bar or column charts using formula-backed summaries: work-order count by Status, by Job_Category and by Site. Each summary must reconcile to the total selected orders. Use white background, navy titles, blue/teal accents, readable labels and a visible reporting date. Do not use category counts as evidence of causes or use colour alone for status.
```

### Step 6

```text
EXCEL - CHAT ONLY:
Explain each Dashboard measure in plain English, including terminal statuses, strict overdue date rule, closed-only SLA denominator and meaning of recorded cost. Give one source-row example for overdue and one for on-time closure; cite Work_Order_ID. Do not guess a root cause or financial saving.
```


## Lab 6

**Make the Dashboard Interactive and Prove Refresh** · [Lab folder](../../labs/lab-06-filters-and-refresh/README.md)

### Step 2

```text
EXCEL - PLAN:
Make Dashboard B2:B5 control all six KPIs and three chart summaries with AND logic. All bypasses its dimension. Use COUNTIFS/SUMIFS or SUMPRODUCT with structured table references. Blank owner means unassigned and must not disappear from All. Keep N/A for no closed jobs.

EXCEL - ALLOW EDITING:
Apply the reviewed filter plan and dropdown lists. Keep existing source rows and chart positions. Show the selected scope beside the reporting date and make all charts recalculate from the same selected rows.
```

### Step 3

```text
EXCEL - CHAT ONLY:
For the dashboard selection Site = Woodlands Hub and all other dimensions All, list the expected six KPI values from tblWorkOrders and verify each chart sum matches the selected total. Do not infer that filtering the worksheet automatically changes formula measures.
```

### Step 6

```text
EXCEL - CHAT ONLY:
Verify the sandbox append test for the two new work orders. Reconcile total 122, closed 49, backlog 61, overdue increased by 1, cost increased by S$400 and on-time numerator increased by 1. Confirm no original source record changed and all three charts total 122 with All selections. Compare original IDs, statuses, owners, dates and costs to the saved baseline; all original 120 rows must match.
```


## Lab 7

**Turn Dashboard Evidence into a Management Story** · [Lab folder](../../labs/lab-07-dashboard-to-presentation/README.md)

### Step 2

```text
WORD COPILOT:
Using this verified 120-row Northstar maintenance snapshot, draft an eight-slide management presentation brief. For each slide give one claim headline, supporting measure/chart, source/date/scope, limitation and speaker note. Structure: overview, portfolio, site backlog, status/category mix, SLA/overdue, assignment/capacity, proposed actions/trade-offs, decision/next review. Do not invent causes, savings, approval or future dates; use UNKNOWN when absent.
```

### Step 4

```text
POWERPOINT COPILOT:
@maintenance-reporting Create or update an eight-slide management presentation from the selected Northstar_Presentation_Brief.docx. Follow the existing white/navy/blue template. One evidence-based message per slide, short visible text, charts or tables for numerical evidence, source/as-at/scope in notes, and a final decision request. Keep values exact, and label all next actions as proposed. Do not add extra slides or invented facts.
```


## Lab 8

**Refine and Present the Maintenance Decision Deck** · [Lab folder](../../labs/lab-08-professional-handoff/README.md)

### Step 2

```text
POWERPOINT COPILOT:
@maintenance-reporting Audit this eight-slide deck against the selected verified Northstar brief. List inaccurate figures, ambiguous units, date/scope omissions, unsupported causal or approval wording, dense text and weak hierarchy. Propose corrections; do not change values or source facts.
```

### Step 3

```text
POWERPOINT COPILOT:
@maintenance-reporting Apply the reviewed design and wording corrections to the existing eight slides. Improve hierarchy and whitespace, make titles claim-led, retain accurate figures and charts, and add 45-second speaker notes per slide. Separate observed findings from proposed actions and end with the decision requested. Preserve the baseline date/scope; do not duplicate slides.
```

### Step 6

```text
OUTLOOK COPILOT:
Draft a short Northstar management handoff email using this verified brief and the links I provide. State the 30 September 2026 baseline scope, headline findings, proposed actions and decision required. Explain that the PowerPoint/PDF is a static snapshot while the Excel dashboard is interactive. Leave missing links UNKNOWN. Do not claim approval or send the draft.
```
