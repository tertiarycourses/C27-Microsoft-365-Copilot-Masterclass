# Asteron Excel Control Values

## Source controls

| Control | Expected |
|---|---:|
| Rows | 20 |
| Unique Participant ID values | 20 |
| Confirmed registrations | 16 |
| Waitlist | 2 |
| Withdrawn | 2 |

## Confirmed-cohort measures

| Measure | Expected |
|---|---:|
| Attended | 14 |
| Attendance rate | 87.5% |
| Training complete | 12 |
| Training completion rate | 75.0% |
| Average readiness score | 80.0625 |
| Support tickets | 9 |
| High-priority participants | 4 |

High-priority confirmed participants are `P004`, `P008`, `P010` and `P015`.

`P017` to `P020` are not in the confirmed cohort and must return `Not in cohort` in the Priority formula.

## Exact Control formulas

Enter labels in `A2:A10` and formulas in `B2:B10`.

| Cell | Control | Formula |
|---|---|---|
| B2 | Rows | `=ROWS(tblReadiness[Participant_ID])` |
| B3 | Unique Participant ID | `=COUNTA(UNIQUE(tblReadiness[Participant_ID]))` |
| B4 | Confirmed | `=COUNTIF(tblReadiness[Registration_Status],"Confirmed")` |
| B5 | Attended among Confirmed | `=COUNTIFS(tblReadiness[Registration_Status],"Confirmed",tblReadiness[Attendance_Status],"Attended")` |
| B6 | Attendance rate | `=B5/B4` |
| B7 | Training complete among Confirmed | `=COUNTIFS(tblReadiness[Registration_Status],"Confirmed",tblReadiness[Training_Complete],"Yes")` |
| B8 | Training completion rate | `=B7/B4` |
| B9 | Average readiness among Confirmed | `=AVERAGEIF(tblReadiness[Registration_Status],"Confirmed",tblReadiness[Readiness_Score])` |
| B10 | Support tickets among Confirmed | `=SUMIFS(tblReadiness[Support_Tickets],tblReadiness[Registration_Status],"Confirmed")` |

Reconcile every department row to `asteron-department-controls.csv` using an independent PivotTable filtered to Confirmed.

## Required interpretations

- Attendance is `14 of 16 confirmed`, not `14 of 20`.
- Training completion is `12 of 16 confirmed`, not `12 of 20`.
- Readiness scores are synthetic training values and do not prove future performance.
