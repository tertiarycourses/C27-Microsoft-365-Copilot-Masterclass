# Microsoft 365 Copilot Masterclass - Prompt Library

[Open the prompts page with Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/)


## Lab 1: Prepare Work Orders and Draft the Operations Brief

[Instruction PDF](../../labs/lab-01-excel-to-word/Lab-01-Instructions.pdf) · [Data folder](../../labs/lab-01-excel-to-word/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-1)

### Step 1

```text
EXCEL - CHAT ONLY:
Read About_This_Data and Control for Northstar Water Services. Explain what one water-pipe service work order represents, the reporting date, the five job categories and how current owners differ from proposed owners. Do not edit or infer customer impacts.
```

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

### Step 6

```text
WORD COPILOT:
Audit this Northstar Water Services operations brief against the verified evidence table I supply. Return a discrepancy list for counts, cost, reporting scope, overdue definition and assignment claims. Identify missing source links as UNKNOWN. Do not change facts or approve work.
```


## Lab 2: Create the Cross-App Maintenance Update

[Instruction PDF](../../labs/lab-02-word-to-powerpoint-and-outlook/Lab-02-Instructions.pdf) · [Data folder](../../labs/lab-02-word-to-powerpoint-and-outlook/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-2)

### Step 1

```text
WORD COPILOT:
From this selected verified Northstar Water Services operations brief, extract a handoff table with reporting date, filter scope, total, closed, cancelled, backlog, overdue, unassigned backlog and recorded cost. Separate facts, proposed next actions and open decisions. Keep every value traceable to the supplied brief.
```

### Step 2

```text
POWERPOINT COPILOT:
Using this verified Northstar Word brief, create a four-slide initial update: scope and portfolio; backlog and overdue work; current assignments and proposed actions; decision required. Use the existing white/navy/blue design. Preserve all verified metrics. Add source/date notes. Do not invent completed work, savings or approved reassignment.
```

### Step 3

```text
POWERPOINT COPILOT:
Audit these four Northstar Water Services slides against the selected verified operations brief. For each numeric claim give the source, date and scope; flag unsupported service-restoration, safety, customer-impact or approval claims. Propose corrections without changing the checked values.
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


## Lab 3: Create a Custom Maintenance Reporting Skill

[Instruction PDF](../../labs/lab-03-author-skill-md/Lab-03-Instructions.pdf) · [Data folder](../../labs/lab-03-author-skill-md/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-3)

### Step 1

```text
MICROSOFT 365 COPILOT WEB:
Write a complete SKILL.md for maintenance-reporting. Require YAML name and description, input table or verified Word snapshot, report date and filter scope. Define backlog, overdue and on-time closed rate. Preserve IDs/status/current owners. Put assignment suggestions in a separate proposals sheet. Support Excel outputs and PowerPoint storytelling with source notes, existing white/navy/blue style, no invented facts and safe reruns. Never send email or approve assignments. Ask for missing inputs. Return the entire Markdown file.
```

### Step 2

```text
MICROSOFT 365 COPILOT WEB:
Review this supplied maintenance-reporting SKILL.md for Northstar Water Services. Check YAML name/description, required source/date/scope, backlog and overdue definitions, source preservation, assignment proposal boundaries, app-specific context and safe reruns. Return exact corrections and then the complete revised file; do not invent missing data.
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

### Step 7

```text
EXCEL - CHAT ONLY:
Using only the web and PowerPoint smoke-test responses I paste here and this workbook test response, prepare a Prompt_Log comparison. Record the app, source, scope, actual behaviour and my verification. Leave missing responses UNKNOWN. Do not claim access to another app chat or a successful test without evidence.
```


## Lab 4: Use and Improve the Skill in Excel and PowerPoint

[Instruction PDF](../../labs/lab-04-repeatable-reporting/Lab-04-Instructions.pdf) · [Data folder](../../labs/lab-04-repeatable-reporting/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-4)

### Step 2

```text
EXCEL - PLAN:
@maintenance-reporting Build Maintenance_Summary for tblWorkOrders at 2026-09-30 with all filters All. Include total, closed, cancelled, backlog, overdue, on-time closed rate and recorded cost; show formulas and source scope. Plan first. Preserve source records.

EXCEL - ALLOW EDITING:
Apply that reviewed summary plan. Add Assignment_Proposals for unassigned backlog only. Use tblTechnicians primary category and available hours as planning inputs; show category/capacity checks, current owner and proposed owner separately. Leave manager decision UNKNOWN. Do not change Assigned_To.
```

### Step 3

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Review Assignment_Proposals against tblWorkOrders and tblTechnicians. Check each suggested owner has the matching water-service job category, capacity limitations are visible and original Assigned_To values are unchanged. Leave manager approval UNKNOWN; do not assign or schedule a technician.
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

### Step 6

```text
MICROSOFT 365 COPILOT WEB:
Improve this supplied maintenance-reporting skill to v2 using only my actual smoke-test and rerun findings pasted here. Add explicit missing-input and no-duplicate-output guards. Keep Excel source and current owners protected. Return the complete revised SKILL.md and a short before/after change log; do not fabricate test evidence.
```


## Lab 5: Build Maintenance Dashboard Measures and Charts

[Instruction PDF](../../labs/lab-05-design-and-build/Lab-05-Instructions.pdf) · [Data folder](../../labs/lab-05-design-and-build/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-5)

### Step 1

```text
EXCEL - CHAT ONLY:
Inspect this Northstar Water Services dashboard starter. Confirm tblWorkOrders, 120 unique IDs, reporting date 2026-09-30 and selection cells B2:B5 initially All. Explain which source and control sheets must remain intact. Report discrepancies before any edits.
```

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

### Step 5

```text
EXCEL - CHAT ONLY:
Reconcile the Northstar Water Services dashboard with Control at All selections. Compare all six KPIs and totals of the Status, Job_Category and Site charts. Flag hard-coded values, fixed row ranges, inconsistent scopes and any interpretation that treats job-category frequency as a cause. Do not edit.
```

### Step 6

```text
EXCEL - CHAT ONLY:
Explain each Dashboard measure in plain English, including terminal statuses, strict overdue date rule, closed-only SLA denominator and meaning of recorded cost. Give one source-row example for overdue and one for on-time closure; cite Work_Order_ID. Do not guess a root cause or financial saving.
```


## Lab 6: Make the Dashboard Interactive and Prove Refresh

[Instruction PDF](../../labs/lab-06-filters-and-refresh/Lab-06-Instructions.pdf) · [Data folder](../../labs/lab-06-filters-and-refresh/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-6)

### Step 1

```text
EXCEL - CHAT ONLY:
Before testing filters, report the baseline Northstar Water Services dashboard source, date and scope. Confirm 120 unique work orders and all four selectors All. Identify the baseline file that must remain untouched when making the refresh-test copy.
```

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

### Step 4

```text
EXCEL - CHAT ONLY:
Check two dashboard edge cases without changing source data: Status New with other selectors All; then Site Woodlands Hub, Job_Category Leak Repair, Assigned_To Daniel Lee, Status All. Verify zero closed gives N/A and no selected rows gives zero count/cost with N/A rate. Show how all charts follow the same selection. Restore all selectors to All.
```

### Step 6

```text
EXCEL - CHAT ONLY:
Verify the sandbox append test for the two new work orders. Reconcile total 122, closed 49, backlog 61, overdue increased by 1, cost increased by S$400 and on-time numerator increased by 1. Confirm no original source record changed and all three charts total 122 with All selections. Compare original IDs, statuses, owners, dates and costs to the saved baseline; all original 120 rows must match.
```

### Step 7

```text
WORD COPILOT:
Using only the verified baseline dashboard evidence I paste here, prepare the frozen Northstar Water Services presentation snapshot. Include reporting date, All scope, 120-row baseline, six KPIs, chart values, source workbook link and limitations. Exclude the 122-row sandbox. Keep proposed priorities separate from observed facts.
```


## Lab 7: Turn Dashboard Evidence into a Management Story

[Instruction PDF](../../labs/lab-07-dashboard-to-presentation/Lab-07-Instructions.pdf) · [Data folder](../../labs/lab-07-dashboard-to-presentation/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-7)

### Step 1

```text
EXCEL - CHAT ONLY:
For the untouched 120-row Northstar Water Services baseline dashboard at 2026-09-30, All selectors, return a presentation evidence table: six KPIs, backlog by site, status and job-category counts, unassigned backlog and relevant source references. Do not use the refresh-test copy or infer service disruption, safety risk, causes or savings.
```

### Step 2

```text
WORD COPILOT:
Using this verified 120-row Northstar maintenance snapshot, draft an eight-slide management presentation brief. For each slide give one claim headline, supporting measure/chart, source/date/scope, limitation and speaker note. Structure: overview, portfolio, site backlog, status/category mix, SLA/overdue, assignment/capacity, proposed actions/trade-offs, decision/next review. Do not invent causes, savings, approval or future dates; use UNKNOWN when absent.
```

### Step 3

```text
WORD COPILOT:
Review this eight-slide Northstar Water Services brief against the supplied baseline evidence. Check each headline has a supporting value, correct units, source/date/scope and an explicit limitation. Rewrite unsupported claims as questions or proposed actions. Do not change verified figures or invent approvals.
```

### Step 4

```text
POWERPOINT COPILOT:
@maintenance-reporting Create or update an eight-slide management presentation from the selected Northstar_Presentation_Brief.docx. Follow the existing white/navy/blue template. One evidence-based message per slide, short visible text, charts or tables for numerical evidence, source/as-at/scope in notes, and a final decision request. Keep values exact, and label all next actions as proposed. Do not add extra slides or invented facts.
```

### Step 6

```text
POWERPOINT COPILOT:
Audit the eight-slide Northstar Water Services management draft against the selected presentation brief and evidence register. Confirm baseline 120, source notes, chart labels and units, correct backlog exclusions and proposed-action wording. List needed corrections and preserve slide count; do not claim Excel charts update automatically.
```


## Lab 8: Refine and Present the Maintenance Decision Deck

[Instruction PDF](../../labs/lab-08-professional-handoff/Lab-08-Instructions.pdf) · [Data folder](../../labs/lab-08-professional-handoff/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-8)

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

### Step 4

```text
POWERPOINT COPILOT:
Using only this Northstar Water Services decision deck, propose three rehearsal questions a service operations manager could ask about overdue jobs, technician capacity and proposed priorities. Suggest where the existing evidence supports an answer and where it remains UNKNOWN. Do not invent partner feedback or alter the evidence.
```

### Step 6

```text
OUTLOOK COPILOT:
Draft a short Northstar management handoff email using this verified brief and the links I provide. State the 30 September 2026 baseline scope, headline findings, proposed actions and decision required. Explain that the PowerPoint/PDF is a static snapshot while the Excel dashboard is interactive. Leave missing links UNKNOWN. Do not claim approval or send the draft.
```

### Step 7

```text
WORD COPILOT:
Review the final Northstar Water Services handoff evidence I supply: baseline workbook, refresh-test record, skill v2, eight-slide deck and PDF, brief, source register and unsent email draft. Return a completeness checklist with verified evidence and missing items UNKNOWN. Confirm every artifact uses the same baseline date/scope; never claim approval, submission or sending.
```
