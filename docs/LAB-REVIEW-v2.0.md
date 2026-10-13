# C027 maintenance labs: independent review

Reviewed on 13 October 2026. Content reviewed without modification. All identified blocking defects have been corrected in the current sources. This review covers lab instructions, controls and continuity; the final release also requires rendered courseware QA and the separate spreadsheet-engine checks.

## Files reviewed

- `.agents/skills/non-wsq-courseware-build/build/maintenance_labs.py`
- `.agents/skills/non-wsq-courseware-build/build/mock_data.py`
- `.agents/skills/non-wsq-courseware-build/build/build_labs.py`
- All eight `labs/lab-*/README.md`, instruction PDFs, prompt TXT files, data workbooks, controls and rejoin checkpoints.

## Findings resolved

1. Dashboard total now includes the `tblWorkOrders[Work_Order_ID]` row array. The All selection no longer leaves the total expression with only scalar factors. Rebuilt dashboard checkpoints contain the correction.
2. The no-row test now specifies Site = Woodlands Hub, Job_Category = HVAC, Assigned_To = Daniel Lee, Status = All. An independent source-row check confirms zero records; category and technician alone did not provide an empty combination.
3. The shared skill respects four slides for the initial update and eight for the management report. `Assignment_Proposals` is explicitly permitted alongside the summary and chart output sheets.
4. The missing-input test uses a new empty workbook and a different unspecified reporting period. The rerun step explicitly returns to `Northstar_Skill_Report.xlsx` and saves `Northstar_Skill_Rerun_Test.xlsx` before rebuilding existing outputs.
5. Excel's working input and manual skill route are named. Excel and PowerPoint installation evidence is checked separately. Retained safeguards may be logged honestly instead of inventing v1/v2 changes.
6. The Word snapshot handoff names the supplied template and output file. A four-slide checkpoint supports the earlier PowerPoint rejoin. Source comparisons cover original IDs, status, owner, dates and cost after editing and refresh.
7. Synthetic descriptions now use the same category as `Job_Category`. All current clean source records have unique IDs and category-consistent descriptions.

## Independently calculated controls

Calculated directly from the generated Lab 6 workbook, independently of the source `metrics()` helper. Reporting date: 30 September 2026.

| Scope | Orders | Closed | Backlog | Overdue | On-time closure | Recorded cost |
|---|---:|---:|---:|---:|---:|---:|
| Baseline, all filters All | 120 | 48 | 60 | 50 | 30/48 = 62.5% | S$35,827.50 |
| Woodlands Hub, other filters All | 24 | 16 | 8 | 7 | 10/16 = 62.5% | S$6,668.50 |
| Status = New, other filters All | 18 | 0 | 18 | 14 | N/A | S$5,454.00 |
| Woodlands Hub + HVAC + Daniel Lee | 0 | 0 | 0 | 0 | N/A | S$0.00 |
| Sandbox after the two supplied append rows | 122 | 49 | 61 | 51 | 31/49 = 63.3% | S$36,227.50 |

Baseline also contains 12 Cancelled records and six unassigned backlog records. Every generated `verified-controls.json` matches the current deterministic controls. The 122-row sandbox is explicitly excluded from the baseline presentation.

## Review conclusions

Prerequisites identify accounts, app availability, OneDrive working copies and synthetic inputs. Each lab has bounded actions, named outputs, verification, troubleshooting, prompts and a rejoin checkpoint. All eight folders have instruction PDFs, prompt TXT files, mock data and templates; local README links resolve. Cross-app context is supplied through selected files or pasted verified evidence, with manual logging for other app chats.

The sequence carries cleaned work orders into a Word brief, initial PowerPoint update and unsent Outlook draft, then a custom skill, interactive dashboard, frozen presentation evidence and final handoff. Counts, units, date and scope remain explicit. Proposed assignments remain separate from current owners; training drafts use `example.invalid` and are never sent. Source preservation and evidence registers provide observable review actions.

Current Microsoft documentation supports the named native skill and editing-mode routes: [Excel custom skills](https://support.microsoft.com/en-us/Excel/copilot/copilot-in-excel-skills), [PowerPoint custom skills](https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills), and [Excel Chat only, Plan and Allow editing](https://support.microsoft.com/en-gb/excel/copilot/get-started-with-copilot-in-excel).

Native Copilot conversations were not executed during this review. Tenant-specific menu availability must therefore be recorded during delivery, with the supplied manual route used honestly where needed. Spreadsheet-engine recalculation and the final rendered package review are separate release evidence.
