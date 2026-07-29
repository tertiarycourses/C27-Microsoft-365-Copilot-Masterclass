# Lab 4 — Analyse Pilot Readiness and Verify Copilot Formulas in Excel

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Copilot Across Your Everyday Work Apps  
**Maps to:** LO3: analyse a bounded Excel table, generate formula columns and reconcile every headline measure to independent controls  
**Duration:** 45 minutes  
**Tools:** Excel for Microsoft 365 · Copilot in Excel · asteron-pilot-readiness.csv

---

## Goal

Create a verified readiness workbook with explicit grain, inspectable formulas, control totals and a short evidence-backed management summary.

## What You Will Do

You will import a 20-row synthetic pilot cohort, preserve the raw source and ask Copilot to create a priority formula and readiness summary. You will inspect the logic, correct denominator rules and reconcile counts, rates and averages before writing three decision-relevant observations.

## What You Will Build

work-c027/C027-Asteron-Pilot-Readiness.xlsx with Raw_Cohort, Analysis, Control and Prompt_Log sheets, a verified priority column and an Approved internal readiness summary, plus work-c027/C027-Asteron-Verified-Readiness-Summary.txt

## Prerequisites

- Download labs/assets/asteron-pilot-readiness.csv and asteron-excel-controls.md.
- Sign in to Excel with Copilot available; record the actual experience label if it differs.
- Use the supplied synthetic cohort only and keep the original CSV unchanged.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Open asteron-pilot-readiness.csv in Excel and save it as work-c027/C027-Asteron-Pilot-Readiness.xlsx. Rename the first sheet Raw_Cohort. Copy the sheet to Analysis, format the data as table tblReadiness and create empty Control and Prompt_Log sheets.

```text
Grain: one row = one synthetic pilot participant
Key: Participant_ID
Raw_Cohort must remain unchanged
Working table: tblReadiness
```

### 2. On Control, enter these metric labels in A2:A10 and exact formulas in B2:B10. State that attendance rate uses Confirmed registrations as its denominator and counts only Attended as its numerator.

```text
B2 Rows: =ROWS(tblReadiness[Participant_ID])
B3 Unique Participant_ID: =COUNTA(UNIQUE(tblReadiness[Participant_ID]))
B4 Confirmed: =COUNTIF(tblReadiness[Registration_Status],"Confirmed")
B5 Attended among Confirmed: =COUNTIFS(tblReadiness[Registration_Status],"Confirmed",tblReadiness[Attendance_Status],"Attended")
B6 Attendance rate: =B5/B4
B7 Training complete among Confirmed: =COUNTIFS(tblReadiness[Registration_Status],"Confirmed",tblReadiness[Training_Complete],"Yes")
B8 Training completion rate: =B7/B4
B9 Average readiness among Confirmed: =AVERAGEIF(tblReadiness[Registration_Status],"Confirmed",tblReadiness[Readiness_Score])
B10 Support tickets among Confirmed: =SUMIFS(tblReadiness[Support_Tickets],tblReadiness[Registration_Status],"Confirmed")
Expected values: 20 | 20 | 16 | 14 | 87.5% | 12 | 75.0% | 80.0625 | 9
```

### 3. Ask Copilot to add a Priority column using the rule below. Require a formula explanation before applying it. Inspect the structured references and verify rows P004, P008, P010, P015 and P017. Non-confirmed rows must be Not in cohort rather than High.

```text
GOAL: Add an editable Priority column to tblReadiness.
CONTEXT: Asteron uses the column to plan support for confirmed pilot participants.
SOURCE: Use Registration_Status, Training_Complete, Readiness_Score and Support_Tickets in tblReadiness only.
EXPECTATIONS: If Registration_Status is not Confirmed, return 'Not in cohort'. Otherwise return 'High' when Training_Complete is No OR Readiness_Score is below 70 OR Support_Tickets is 2 or more; else 'Standard'. Explain the formula, then apply it without changing Raw_Cohort.
```

### 4. Ask Copilot for a summary table of confirmed participants by Department with count, attended count, training-complete count, average readiness and support tickets. Build an independent PivotTable from tblReadiness filtered to Confirmed and reconcile every department row—not only the grand total—against labs/assets/asteron-department-controls.csv. Do not accept a summary whose denominator includes Waitlist or Withdrawn rows.

```text
Summarise confirmed participants in tblReadiness by Department. Return Count, Attended, Training_Complete, Average_Readiness and Support_Tickets. Include grand totals and state the filters and denominator.
```

### 5. Write three observations in a Summary area: one about attendance, one about training completion and one about high-priority support. Label each OBSERVED and cite the control cells. Add a Limitations line noting that readiness scores are synthetic and do not prove future performance. Record prompt, formula, checks and release decision in Prompt_Log. Export the verified headline measures as plain text to work-c027/C027-Asteron-Verified-Readiness-Summary.txt for the supported Copilot Chat handoff in Lab 7.

```text
Required summary facts:
Attendance = 14 of 16 confirmed (87.5%)
Training complete = 12 of 16 confirmed (75.0%)
High priority = 4 confirmed participants: P004, P008, P010, P015
Release state = Approved for internal workflow lab
```

## Test It

Raw_Cohort must match the CSV and tblReadiness must contain 20 rows with 20 unique IDs. Control values must match asteron-excel-controls.md exactly. Priority must show High only for P004, P008, P010 and P015 among confirmed participants, and Not in cohort for P017-P020. Every department row and the grand total must tie to asteron-department-controls.csv, every summary sentence must cite a control cell, and the verified TXT export must contain the three headline measures.

## Checkpoint and Rejoin Point

Save the approved readiness workbook and verified-readiness TXT. Lab 7 uses the supported TXT export for its three verified headline measures. If any tie-out fails, keep the workbook in REVISE and do not copy its numbers to another app.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Copilot uses all 20 rows as the attendance denominator. | Restate the Confirmed filter explicitly and compare the formula with COUNTIF(tblReadiness[Registration_Status],"Confirmed"). |
| Priority marks waitlisted or withdrawn rows High. | Place the Registration_Status condition first so non-confirmed rows return Not in cohort before other tests. |
| The average differs from 80.0625. | Check that AVERAGEIF uses Confirmed as the criterion and Readiness_Score as the average range; do not round before reconciliation. |

## Challenge

Create a PivotTable of confirmed participants by Department and Preferred_Session. Reconcile the grand total to 16 and explain why the table supports capacity planning but not employee performance decisions.

## Reflection

Which denominator choice most changed the meaning of a readiness measure, and how did you make it visible?

---

[← Lab 3](lab-03-generate-and-refine-the-asteron-decision-deck-in-powerpoint.md) · [Lab 5 →](lab-05-summarise-the-launch-thread-and-prepare-a-reviewed-outlook-draft.md)
