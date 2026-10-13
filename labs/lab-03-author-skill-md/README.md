# Lab 3 - Create a Custom Maintenance Reporting Skill

**C27 | v2.0 | Topic 2 | 40 minutes**

[Instruction PDF](Lab-03-Instructions.pdf) · [Copy-ready prompts](sample-prompts.txt) · [Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md#lab-3)

## Goal

A reviewed maintenance-reporting/SKILL.md v1, a smoke-test record, and a native-skill or explicitly labelled manual-practice route for each app.

## What you will build

A reviewed maintenance-reporting/SKILL.md v1, a smoke-test record, and a native-skill or explicitly labelled manual-practice route for each app.

Capture the maintenance definitions and reporting style as one custom skill. You will ask Microsoft 365 Copilot on the web to write SKILL.md, compare it with a supplied complete template, install it in each app’s own supported skills location, and perform a small smoke test. A skill is reusable instructions, while a prompt is one request and workbook rules govern one file.

## Prerequisites

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.

## Files

- [Mock workbook](data/Northstar_Work_Orders.xlsx): raw 122-row input in Lab 1, clean 120-row input elsewhere.
- [Clean CSV reference](data/Northstar_Work_Orders.csv) and [expected controls](data/verified-controls.json).
- [Rejoin workbook](checkpoints/Northstar_Verified_Checkpoint.xlsx) and [snapshot](checkpoints/Northstar_Verified_Snapshot.docx).
- [Templates](templates/) for the brief, slide deck, evidence and handoff.

## Steps

### 1. Step 1

Read templates/maintenance-reporting/SKILL.md and data/Northstar_Maintenance_Context.txt. Open Microsoft 365 Copilot at https://copilot.cloud.microsoft in your assigned account. Provide the skill requirements as prompt context. Do not upload private work data.

```text
MICROSOFT 365 COPILOT WEB:
Write a complete SKILL.md for maintenance-reporting. Require YAML name and description, input table or verified Word snapshot, report date and filter scope. Define backlog, overdue and on-time closed rate. Preserve IDs/status/current owners. Put assignment suggestions in a separate proposals sheet. Support Excel outputs and PowerPoint storytelling with source notes, existing white/navy/blue style, no invented facts and safe reruns. Never send email or approve assignments. Ask for missing inputs. Return the entire Markdown file.
```

### 2. Step 2

Copy the complete returned file into a plain text editor, save UTF-8 as SKILL.md in a folder named maintenance-reporting, not SKILL.md.txt. Check the opening --- name/description --- block. Compare every definition and boundary with the supplied template. Edit missing instructions and retain your own version as v1 in templates or work-c027.
### 3. Step 3

Open data/Northstar_Work_Orders.xlsx in Excel and save a working copy first. Then open Copilot > ... > Manage skills (or Manage plugins & skills) > Custom skills > Create OneDrive folder (if needed) > Open skills folder. Put the maintenance-reporting folder containing SKILL.md inside that app-created folder. Return to Custom skills and select Refresh. Enable the skill and verify the exact name; do not guess the OneDrive folder path.
### 4. Step 4

In that Lab 3 workbook invoke the skill from Add work content > Choose skills (or Choose plugins & skills) or @mention. Inspect the proposed plan before editing; keep the source table unchanged. Save the result as Northstar_Skill_Smoke_Test.xlsx. If the Excel skills menu is absent, paste the complete reviewed SKILL.md as instructions before the test prompt, omit @mention, and record Manual practice - native skill unavailable.

```text
EXCEL - CHAT ONLY:
@maintenance-reporting Explain the reporting definitions for tblWorkOrders at 2026-09-30, all filters All. State which sheets you may change, how missing owners are handled, and what you need before producing a PowerPoint update. Do not edit yet.
```

### 5. Step 5

Open PowerPoint template > Copilot > + > Choose skills > Manage skills > Add skill. Upload your SKILL.md or paste it in Add skill as supported; verify it appears and is enabled. Alternatively use Manage skills > Custom skills > Open skills folder and copy the correctly named folder there. The PowerPoint location is app-created; installing in Excel alone is not proof it is available in PowerPoint.
### 6. Step 6

Run a PowerPoint smoke test with the verified snapshot selected as a file reference. Record the actual app name, selected skill name and response. If a skills menu is absent, paste the complete reviewed skill as instructions alongside the snapshot and mark Manual practice - native skill unavailable. Do not claim a native invocation.

```text
POWERPOINT COPILOT:
@maintenance-reporting Using the selected Northstar_Verified_Snapshot.docx, propose an eight-slide maintenance report outline. Explain how every claim will be grounded and which actions remain proposals. Keep the reporting date and scope visible; do not edit slides yet.
```

### 7. Step 7

Log the web authoring prompt and PowerPoint test manually in workbook Prompt_Log. For Excel log the actual response and your check. Keep the v1 file and test notes for Lab 4; no app can automatically read the other app’s chat.

## Test it

- Skill format: maintenance-reporting folder; matching name in YAML; nonempty description; UTF-8 SKILL.md.
- Metric controls: Backlog excludes two terminal statuses; due-today not overdue; zero closed -> N/A.
- Installation evidence: Excel and PowerPoint names verified separately, or manual route honestly recorded.

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
