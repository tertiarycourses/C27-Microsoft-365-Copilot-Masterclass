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


## Lab 3: Personalise Copilot in Excel for Consistent Service Reports

[Instruction PDF](../../labs/lab-03-personalisation/Lab-03-Instructions.pdf) · [Data folder](../../labs/lab-03-personalisation/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-3)

### Step 1

```text
EXCEL - CHAT ONLY:
Inspect tblWorkOrders and Control for Northstar Water Services. State the clean row count, reporting date and recorded cost. Explain why display preferences should not change source values or reporting definitions. Do not edit.
```

### Step 3

```text
EXCEL - PLAN:
Plan a Preference_Check sheet showing Control!B2 reporting date, total work orders and recorded Cost_SGD from tblWorkOrders for Northstar Water Services. Use my saved display and explanation preferences. Preserve Work_Orders, IDs, owners and exact values.

EXCEL - ALLOW EDITING:
Apply the reviewed Preference_Check plan with structured-reference formulas. Show a short explanation first and leave the source unchanged.
```

### Step 4

```text
EXCEL - ALLOW EDITING:
In this second Northstar workbook, create Preference_Check with formula-backed Control!B2 reporting date, total work orders and recorded Cost_SGD. Follow my saved preferences, preserve source records and explain the result briefly.
```

### Step 5

```text
EXCEL - ALLOW EDITING:
For this task only, display the recorded cost result in Preference_Check with four decimal places. Keep its formula and exact numeric value unchanged. Do not modify source cells or my saved preferences.
```

### Step 6

```text
EXCEL - CHAT ONLY:
Explain which choices in this exercise belong to my account, which belong to this Northstar workbook and which apply only to one prompt. Use the results I actually observed. Do not claim my preferences are shared with another person or added to the workbook.
```


## Lab 4: Create and Test Workbook .Rules for Water Service Reporting

[Instruction PDF](../../labs/lab-04-workbook-rules/Lab-04-Instructions.pdf) · [Data folder](../../labs/lab-04-workbook-rules/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-4)

### Step 1

```text
EXCEL - CHAT ONLY:
Inspect this Northstar workbook. Identify the source table, fixed reporting date, status vocabulary and current owners. List workbook-specific conventions that belong in .Rules rather than account Personalisation. Do not edit.
```

### Step 2

```text
EXCEL - PLAN:
Review the visible .Rules column A for this Northstar workbook. Identify ambiguous instructions or conflicts with the actual source and Control. Propose concise corrections, keeping one idea per cell. Do not edit the source or invent precedence between rules, preferences and Skills.
```

### Step 3

```text
EXCEL - ALLOW EDITING:
Apply only my reviewed .Rules corrections. Keep the sheet visible, one instruction per column-A cell, and retain the reporting-date formula. Preserve source data, Control and unrelated sheets.
```

### Step 4

```text
EXCEL - ALLOW EDITING:
Create Rules_Test for Northstar Water Services from tblWorkOrders using the visible workbook .Rules. Include total, backlog, overdue, on-time Closed rate and recorded cost with formula/source evidence. Show date and All scope. Keep source owners and values unchanged.
```

### Step 5

```text
EXCEL - CHAT ONLY:
In this copied Northstar workbook, identify the visible .Rules instructions and reporting-date formula result. Explain which guidance travels with the workbook and which account preferences do not. Verify Rules_Test against Control without changing records.
```

### Step 6

```text
EXCEL - CHAT ONLY:
Compare Personalisation, .Rules and a reusable Skill for Northstar reporting. Place currency preferences, this workbook’s backlog/date rules and the repeatable Pareto workflow in the right scope. Identify conflicts requiring clarification and the checks a person still must perform.
```


## Lab 5: Create a Custom Pareto Chart Skill and Apply It

[Instruction PDF](../../labs/lab-05-custom-pareto-chart-skill/Lab-05-Instructions.pdf) · [Data folder](../../labs/lab-05-custom-pareto-chart-skill/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-5)

### Step 1

```text
EXCEL - CHAT ONLY:
For tblWorkOrders at Control!B2, All sites, count overdue backlog by Job_Category: Status neither Closed nor Cancelled and Due_Date strictly before the reporting date. Show category counts and total before charting. Preserve all records.
```

### Step 2

```text
MICROSOFT 365 COPILOT WEB:
Write a complete SKILL.md named water-service-pareto for a recurring water-pipe service report. Require YAML name and description, actual source table, reporting date, scope, count metric and grouping column. Source tblWorkOrders has Work_Order_ID, Job_Category, Site, Status and Due_Date. Overdue backlog excludes Closed/Cancelled and has Due_Date before the supplied date. Read visible workbook .Rules; preserve source IDs/statuses/owners and unrelated sheets. Count by grouping, sort count descending then label alphabetically for ties, and create formula-backed count, cumulative count, share and cumulative percentage. Build an editable combo chart: count columns and cumulative line on a 0%-100% right axis. Output only Pareto_<grouping column>; ask before replacing the matching output, rerun without duplicates, and leave zero-total percentages N/A. Verify counts, stable ties and final 100%; do not infer causes or force 80/20. Return the entire file.
```

### Step 4

```text
EXCEL - PLAN:
@water-service-pareto Plan an overdue-backlog Pareto Chart by Job_Category from tblWorkOrders at 2026-09-30, All sites. Follow visible .Rules. Explain summary formulas, descending counts, alphabetical ties, cumulative percentages and the named output to create. Do not edit yet.

EXCEL - ALLOW EDITING:
@water-service-pareto Apply the reviewed Job_Category Pareto plan. Create Pareto_Job_Category with a formula-backed summary and editable count-column/cumulative-percent-line combo chart. Keep source data and unrelated sheets unchanged.
```

### Step 5

```text
EXCEL - CHAT ONLY:
Verify Pareto_Job_Category against eligible source rows. Check total 50, descending counts, alphabetical tie order, cumulative percentages 36/60/76/92/100%, final 100% and labelled dual axes. State which category set first reaches 80%, and why this is contribution rather than a causal diagnosis.
```

### Step 6

```text
EXCEL - PLAN:
@water-service-pareto Refresh the existing Pareto_Job_Category for the same source, date and All scope. Identify exactly what will be replaced and ask before replacement. Preserve every unrelated sheet and do not duplicate charts.

EXCEL - ALLOW EDITING:
@water-service-pareto After the approved category rerun, create a separate overdue-backlog Pareto_Site for the same source/date/scope. Preserve Pareto_Job_Category and reconcile the new summary to 50 overdue orders.
```


## Lab 6: Create, Use and Improve the Maintenance Reporting Skill

[Instruction PDF](../../labs/lab-06-reporting-skill/Lab-06-Instructions.pdf) · [Data folder](../../labs/lab-06-reporting-skill/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-6)

### Step 1

```text
MICROSOFT 365 COPILOT WEB:
Write complete maintenance-reporting SKILL.md with YAML name/description. Require actual tblWorkOrders or a verified Word snapshot, report date and filter scope. Respect visible .Rules. Define backlog, overdue and Closed-only on-time rate. Preserve IDs/statuses/current owners; keep assignment proposals separate and approvals UNKNOWN. Create a verified Excel summary and improve a supplied four- or eight-slide PowerPoint report from selected evidence. Ask for missing inputs and before replacing only named outputs; rerun without duplicates or source changes. Keep the existing design and source/date notes. Never send email or approve assignments. Return the entire file.
```

### Step 3

```text
EXCEL - PLAN:
@maintenance-reporting Build Maintenance_Summary for tblWorkOrders at 2026-09-30 with all filters All. Include total, closed, cancelled, backlog, overdue, on-time closed rate and recorded cost; show formulas and source scope. Plan first. Preserve source records.

EXCEL - ALLOW EDITING:
Apply that reviewed summary plan. Add Assignment_Proposals for unassigned backlog only. Use tblTechnicians primary category and available hours as planning inputs; show category/capacity checks, current owner and proposed owner separately. Leave manager decision UNKNOWN. Do not change Assigned_To.
```

### Step 4

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Review Assignment_Proposals against tblWorkOrders and tblTechnicians. Check each suggested owner has the matching water-service job category, capacity limitations are visible and original Assigned_To values are unchanged. Leave manager approval UNKNOWN; do not assign or schedule a technician.
```

### Step 5

```text
POWERPOINT COPILOT:
@maintenance-reporting Improve this existing four-slide Northstar update from the selected verified Word snapshot. Preserve slide count, all values and source/date/scope notes; use clear claim headlines and the existing design. Keep assignment suggestions explicitly proposed and do not assume access to Excel chat.
```

### Step 6

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Prepare my next maintenance report. I need a DIFFERENT reporting period from the course example and have not supplied any source, date or scope. This empty workbook contains no work orders. Tell me what you need; do not invent data.

EXCEL - PLAN:
@maintenance-reporting Rebuild the existing Maintenance_Summary for the same table, date and scope. Describe what will be replaced, ask before replacement and keep source/unrelated sheets. Do not duplicate outputs.
```

### Step 7

```text
MICROSOFT 365 COPILOT WEB:
Improve this supplied maintenance-reporting skill to v2 using only my actual smoke-test and rerun findings pasted here. Add explicit missing-input and no-duplicate-output guards. Keep Excel source and current owners protected. Return the complete revised SKILL.md and a short before/after change log; do not fabricate test evidence.
```


## Lab 7: Create and Apply a Custom Interactive Dashboard Skill

[Instruction PDF](../../labs/lab-07-custom-dashboard-skill/Lab-07-Instructions.pdf) · [Data folder](../../labs/lab-07-custom-dashboard-skill/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-7)

### Step 1

```text
MICROSOFT 365 COPILOT WEB:
Write complete water-service-dashboard SKILL.md with YAML name/description. Require actual tblWorkOrders and report date in Control!B2; read visible .Rules. Preserve source IDs/statuses/owners, Technicians, Control, .Rules, Prompt_Log, Pareto_* and unrelated sheets. Plan first and ask before replacing only named dashboard outputs; rerun without duplicated charts. Dashboard B2:B5 select Site, Job_Category, Status, Assigned_To with All bypasses and AND logic. B7 total, B8 backlog excluding Closed/Cancelled, B9 backlog Due_Date before Control!B2, B10 Closed, B11 on-time Closed_Date<=Due_Date among Closed only with N/A if none, B12 recorded Cost_SGD across selected statuses. Create three formula-backed editable status/category/site charts sharing the exact filter scope. Use structured references, not fixed120-row ranges, and white/navy/blue/teal workbook design. Baseline check at 2026-09-30 All:120 total,48 Closed,12 Cancelled,60 backlog,50 overdue,30/48 on-time,35827.50 cost. Verify site/no-Closed/no-row tests, source preservation and a separate two-row append sandbox with 122 total,49 Closed,61 backlog,51 overdue,31/49 on-time and 36227.50 cost. These are snapshot tests, not universal future figures. Ask for missing inputs; never approve assignments, infer causes/savings or send email. Return the entire file.
```

### Step 3

```text
EXCEL - CHAT ONLY:
@water-service-dashboard Inspect this Northstar Water Services dashboard starter. Confirm tblWorkOrders, 120 unique IDs, reporting date 2026-09-30 and selection cells B2:B5 initially All. Explain which source and control sheets must remain intact. Report discrepancies before any edits.
```

### Step 4

```text
EXCEL - PLAN:
@water-service-dashboard Plan Dashboard for Northstar maintenance at 2026-09-30. Use selection cells B2:B5 for Site, Job_Category, Status, Assigned_To, all initially All. Reserve B7 total orders, B8 backlog, B9 overdue backlog, B10 closed, B11 on-time closure rate, B12 Cost_SGD. Place three charts for status, category and site with labels, units and scope. Preserve source data.
```

### Step 5

```text
EXCEL - ALLOW EDITING:
@water-service-dashboard Build the planned six KPI formulas from tblWorkOrders. Backlog excludes Closed/Cancelled. Overdue also requires Due_Date < Control!B2. On-time rate counts Closed_Date <= Due_Date among Closed rows only, and shows N/A when none. Recorded cost sums Cost_SGD of all included statuses. Link to table columns, never a fixed 120-row range. Keep source data unchanged.
```

### Step 6

```text
EXCEL - ALLOW EDITING:
@water-service-dashboard Create three editable bar or column charts using formula-backed summaries: work-order count by Status, by Job_Category and by Site. Each summary must reconcile to the total selected orders. Use white background, navy titles, blue/teal accents, readable labels and a visible reporting date. Do not use category counts as evidence of causes or use colour alone for status.
```

### Step 7

```text
EXCEL - CHAT ONLY:
@water-service-dashboard Reconcile the Northstar Water Services dashboard with Control at All selections. Compare all six KPIs and totals of the Status, Job_Category and Site charts. Flag hard-coded values, fixed row ranges, inconsistent scopes and any interpretation that treats job-category frequency as a cause. Do not edit.
```

### Step 8

```text
EXCEL - CHAT ONLY:
@water-service-dashboard Explain each Dashboard measure in plain English, including terminal statuses, strict overdue date rule, closed-only SLA denominator and meaning of recorded cost. Give one source-row example for overdue and one for on-time closure; cite Work_Order_ID. Do not guess a root cause or financial saving.
```


## Lab 8: Use the Dashboard Skill for Filters, Refresh and Safe Reruns

[Instruction PDF](../../labs/lab-08-interactive-filters-and-refresh/Lab-08-Instructions.pdf) · [Data folder](../../labs/lab-08-interactive-filters-and-refresh/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-8)

### Step 1

```text
EXCEL - CHAT ONLY:
@water-service-dashboard Before testing filters, report the baseline Northstar Water Services dashboard source, date and scope. Confirm 120 unique work orders and all four selectors All. Identify the baseline file that must remain untouched when making the refresh-test copy.
```

### Step 2

```text
EXCEL - PLAN:
@water-service-dashboard Make Dashboard B2:B5 control all six KPIs and three chart summaries with AND logic. All bypasses its dimension. Use COUNTIFS/SUMIFS or SUMPRODUCT with structured table references. Blank owner means unassigned and must not disappear from All. Keep N/A for no closed jobs.

EXCEL - ALLOW EDITING:
@water-service-dashboard Apply the reviewed filter plan and dropdown lists. Keep existing source rows and chart positions. Show the selected scope beside the reporting date and make all charts recalculate from the same selected rows.
```

### Step 3

```text
EXCEL - CHAT ONLY:
@water-service-dashboard For the dashboard selection Site = Woodlands Hub and all other dimensions All, list the expected six KPI values from tblWorkOrders and verify each chart sum matches the selected total. Do not infer that filtering the worksheet automatically changes formula measures.
```

### Step 4

```text
EXCEL - CHAT ONLY:
@water-service-dashboard Check two dashboard edge cases without changing source data: Status New with other selectors All; then Site Woodlands Hub, Job_Category Leak Repair, Assigned_To Daniel Lee, Status All. Verify zero closed gives N/A and no selected rows gives zero count/cost with N/A rate. Show how all charts follow the same selection. Restore all selectors to All.
```

### Step 6

```text
EXCEL - CHAT ONLY:
@water-service-dashboard Verify the sandbox append test for the two new work orders. Reconcile total 122, closed 49, backlog 61, overdue increased by 1, cost increased by S$400 and on-time numerator increased by 1. Confirm no original source record changed and all three charts total 122 with All selections. Compare original IDs, statuses, owners, dates and costs to the saved baseline; all original 120 rows must match.
```

### Step 7

```text
EXCEL - PLAN:
@water-service-dashboard Refresh the existing dashboard for the sandbox 122-row table and same reporting date. Preserve all original source records, both new rows, .Rules, Pareto_* and unrelated sheets. Identify named output replacements and ask before editing; keep one dashboard and three charts.

EXCEL - ALLOW EDITING:
@water-service-dashboard Apply only the reviewed sandbox dashboard rerun. Retain the chosen source/date and make every KPI and chart follow the four filters; reconcile 122 total,61 backlog,51 overdue,49 Closed,31/49 on-time and S$36,227.50. Do not alter the untouched baseline workbook.
```

### Step 8

```text
WORD COPILOT:
Using only the verified baseline dashboard evidence I paste here, prepare the frozen Northstar Water Services presentation snapshot. Include reporting date, All scope, 120-row baseline, six KPIs, chart values, source workbook link and limitations. Exclude the 122-row sandbox. Keep proposed priorities separate from observed facts.
```


## Lab 9: Turn Dashboard Evidence into a Management Story

[Instruction PDF](../../labs/lab-09-dashboard-to-presentation/Lab-09-Instructions.pdf) · [Data folder](../../labs/lab-09-dashboard-to-presentation/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-9)

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


## Lab 10: Refine and Present the Maintenance Decision Deck

[Instruction PDF](../../labs/lab-10-professional-handoff/Lab-10-Instructions.pdf) · [Data folder](../../labs/lab-10-professional-handoff/data/) · [Copy buttons](https://tertiarycourses.github.io/C27-Microsoft-365-Copilot-Masterclass/prompts/#lab-10)

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
