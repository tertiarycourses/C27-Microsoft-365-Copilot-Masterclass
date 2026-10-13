# Microsoft 365 Copilot Masterclass — Learner Guide

**Course Code:** C27  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v2.1 · 13 October 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 1 — Fundamentals of Microsoft 365 Copilot](#topic-1--fundamentals-of-microsoft-365-copilot)
  - [Grounding Across Microsoft 365](#grounding-across-microsoft-365)
  - [Work-Order Grain and Reporting Measures](#work-order-grain-and-reporting-measures)
  - [Lab 1 · Excel to Word — Prepare Work Orders and Draft the Operations Brief](#lab-1--excel-to-word--prepare-work-orders-and-draft-the-operations-brief)
  - [Prompts and Verified App Handoffs](#prompts-and-verified-app-handoffs)
  - [Outlook Drafting and Operational Decisions](#outlook-drafting-and-operational-decisions)
  - [Lab 2 · Word to PowerPoint and Outlook — Create the Cross-App Maintenance Update](#lab-2--word-to-powerpoint-and-outlook--create-the-cross-app-maintenance-update)
  - [Topic 1 Recap - Mapped to Learning Outcomes](#topic-1-recap---mapped-to-learning-outcomes)
- [Topic 2 — Create Skills for Microsoft 365 Copilot](#topic-2--create-skills-for-microsoft-365-copilot)
  - [Skills, Prompts and Workbook Rules](#skills-prompts-and-workbook-rules)
  - [Custom Skill Discovery in Each App](#custom-skill-discovery-in-each-app)
  - [Lab 3 · Author SKILL.md — Create a Custom Maintenance Reporting Skill](#lab-3--author-skillmd--create-a-custom-maintenance-reporting-skill)
  - [Repeatability and Safe Skill Reruns](#repeatability-and-safe-skill-reruns)
  - [Assignment Proposals and Capacity Evidence](#assignment-proposals-and-capacity-evidence)
  - [Lab 4 · Repeatable reporting — Use and Improve the Skill in Excel and PowerPoint](#lab-4--repeatable-reporting--use-and-improve-the-skill-in-excel-and-powerpoint)
  - [Topic 2 Recap - Mapped to Learning Outcomes](#topic-2-recap---mapped-to-learning-outcomes)
- [Topic 3 — Create an Interactive Dashboard with Excel Copilot](#topic-3--create-an-interactive-dashboard-with-excel-copilot)
  - [Dashboard Measures and Denominators](#dashboard-measures-and-denominators)
  - [Visual Dashboard Design for Maintenance](#visual-dashboard-design-for-maintenance)
  - [Lab 5 · Design and build — Build Maintenance Dashboard Measures and Charts](#lab-5--design-and-build--build-maintenance-dashboard-measures-and-charts)
  - [One Filter Scope for Every Visual](#one-filter-scope-for-every-visual)
  - [Refresh Tests and Static Snapshots](#refresh-tests-and-static-snapshots)
  - [Lab 6 · Filters and refresh — Make the Dashboard Interactive and Prove Refresh](#lab-6--filters-and-refresh--make-the-dashboard-interactive-and-prove-refresh)
  - [Topic 3 Recap - Mapped to Learning Outcomes](#topic-3-recap---mapped-to-learning-outcomes)
- [Topic 4 — Create a Professional Presentation with PowerPoint Copilot](#topic-4--create-a-professional-presentation-with-powerpoint-copilot)
  - [From Dashboard Evidence to a Decision Story](#from-dashboard-evidence-to-a-decision-story)
  - [Charts, Templates and Source Provenance](#charts-templates-and-source-provenance)
  - [Lab 7 · Dashboard to presentation — Turn Dashboard Evidence into a Management Story](#lab-7--dashboard-to-presentation--turn-dashboard-evidence-into-a-management-story)
  - [Professional Refinement and Rehearsal](#professional-refinement-and-rehearsal)
  - [Reviewed Handoff and Artifact Lifecycle](#reviewed-handoff-and-artifact-lifecycle)
  - [Lab 8 · Professional handoff — Refine and Present the Maintenance Decision Deck](#lab-8--professional-handoff--refine-and-present-the-maintenance-decision-deck)
  - [Topic 4 Recap - Mapped to Learning Outcomes](#topic-4-recap---mapped-to-learning-outcomes)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This masterclass follows Northstar Water Services, a fictional water-pipe maintenance and service company, from a dirty service-work-order export to a reviewed management decision pack. Work-order IDs, categories, sites, current assignments and status definitions stay consistent across every app. The purpose is to make evidence travel accurately through the workflow, while using Copilot for drafting, analysis, reusable instructions and visual communication.

Study each topic’s concepts before its two labs. Each lab has its own instruction PDF and a data folder containing synthetic inputs, templates and a deterministic checkpoint. Copy-ready prompts are on the linked web page. Carry your own verified outputs forward. A supplied checkpoint allows rejoining but is not evidence that you completed the earlier task. The detailed procedures are here and in labs; the slides teach concepts and show outcomes.


## Course Learning Outcomes

- LO1: Integrate Word, Excel, PowerPoint and Outlook Copilot in a coherent maintenance workflow with explicit source grounding and verified prompts.
- LO2: Create, install, apply and improve a custom maintenance-reporting skill in Excel and PowerPoint, preserving source records and testing reruns.
- LO3: Create an interactive maintenance dashboard with verified measures, common filter scope, meaningful charts and a demonstrated refresh test.
- LO4: Continue from the dashboard to a professional management presentation, with evidence-based headlines, source notes, rehearsal and a reviewed handoff draft.


## Before You Start — Preparation

**What you need**

- Assigned Microsoft 365 account with Copilot in Word, Excel, PowerPoint and Outlook; licence and tenant settings checked before class.
- Excel desktop Windows or Mac recommended; current apps, English display language for Excel custom skills, assigned OneDrive and AutoSave.
- Complete lab folder downloads and a personal work-c027 output folder; all sample data is synthetic.
- Copilot skills access in both Excel and PowerPoint. If unavailable, the lab supplies a clearly labelled manual-instruction practice route.

**Verify your setup**

Open one workbook and one Word/PowerPoint template; find each Copilot button. Confirm that the app can select the intended OneDrive reference file. Use the app-created custom skills folder rather than guessing a path. Keep Formulas > Calculation Options > Automatic. Never paste account passwords into a prompt.

**Conventions used in every lab**

- App-labelled prompts run in the named app; a prompt in one app is not automatically visible to another.
- Use Chat only for inspection, Plan for reviewed proposals, and Allow editing for authorised workbook changes when these modes are available.
- Log Word, Outlook, PowerPoint and web prompts manually in Prompt_Log.
- All comparisons use the same source table, reporting date and filter scope. Missing values remain UNKNOWN; zero closed denominator is N/A.


## Topic 1 — Fundamentals of Microsoft 365 Copilot

One verified maintenance workflow across four apps

**Key concepts**

- Grounding — Select actual sources in every app.
- Work orders — IDs, status, category, site and current assignment.
- Prompts — Goal, context, source and expectations.
- Handoffs — Reconcile Word, Excel, slides and draft email.

Concepts for Lab 1: Grounding Across Microsoft 365, Work-Order Grain and Reporting Measures.


### Grounding Across Microsoft 365

Grounding gives an AI request the specific evidence it should use. A work-grounded Copilot experience can use permitted organisational content; a file-grounded request uses selected files or supplied text. Neither makes an inaccessible file available merely because its local path is typed into a prompt. Word, Excel, PowerPoint and Outlook have different current-document and file-reference experiences. Treat each app handoff as a new grounding task.

A maintenance figure can be correct in Excel yet become wrong in an email when the source, reporting date or filter scope changes. Explicit grounding prevents unsupported owner assignments, stale reporting periods and invented approvals from entering the pack. A Copilot response is a draft or hypothesis until the underlying evidence has been checked.

**How it works**

- Identify the authoritative work-order table.
- Provide goal, context, source and expected output.
- Review against the named evidence.
- Pass a verified snapshot to the next app.

**Worked example**

- Excel analyses tblWorkOrders; Word receives the checked summary.
- PowerPoint receives the reviewed Word brief; Outlook receives the same checked values.
- An Excel chat transcript is not an automatic PowerPoint data source.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The source is accessible and the output has an explicit audience. | The prompt assumes access to another app chat or local path. |

**Authoritative references**

- https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot
- https://support.microsoft.com/en-gb/word/copilot/draft-and-add-content-with-copilot-in-word

---


### Work-Order Grain and Reporting Measures

A row represents one work order, identified by Work_Order_ID. Site, job category, priority, status and current assignment are dimensions used to group or filter records. Measures are defined calculations. The source is a snapshot at 30 September 2026: current backlog excludes Closed and Cancelled; overdue backlog also has a Due_Date before that date. Closed orders are counted separately from jobs still in the queue.

An exact duplicated export row changes counts and cost without representing new work. Normalising a category spelling must not change the business meaning or assign a missing owner. Named Excel tables and structured references let formulas expand when legitimate new rows are appended. Preserve the raw export so a cleaning decision can be traced.

**How it works**

- Define one ID per work order.
- Find exact repeated export records.
- Standardise labels without inventing facts.
- Reconcile cleaned counts and cost.

**Worked example**

- 122 raw rows contain 120 distinct work-order IDs.
- Total = Closed + Cancelled + Backlog after exact duplicate removal.
- Due on 30 September is not overdue at the 30 September snapshot.

**Decision guide**

| Use when | Avoid when |
|---|---|
| You have consistent IDs and a fixed reporting date. | Duplicate IDs contain conflicting records or reporting scope is unknown. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/create-and-share-a-dashboard-with-excel-and-microsoft-groups

---


### Lab 1 · Excel to Word — Prepare Work Orders and Draft the Operations Brief

Learning outcome: LO1: integrate verified Word, Excel, PowerPoint and Outlook outputs.

Goal: Northstar_Clean_Work_Orders.xlsx and Northstar_Operations_Brief.docx, with reconciled counts, reporting scope and a source register.

You are Northstar Water Services’ maintenance coordinator. A Q3 export contains repeated IDs and inconsistent category labels. You will clean a copy in Excel, reconcile its controls, and use the verified result to draft a Word operations brief. The same site, status and assignment definitions underpin every later report.

**What you'll build**

Northstar_Clean_Work_Orders.xlsx and Northstar_Operations_Brief.docx, with reconciled counts, reporting scope and a source register.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.

**Step-by-step**

1. Copy data/Northstar_Work_Orders.xlsx to your OneDrive work-c027 folder as Northstar_Clean_Work_Orders.xlsx. Open it in Excel, set Formulas > Calculation Options > Automatic, and read About_This_Data and Control. The workbook is the deliberately dirty 122-row input; the supplied CSV is a clean reference and must not replace the cleaning exercise. Open Copilot from Home > Copilot.

   ```text
   EXCEL - CHAT ONLY:
   Read About_This_Data and Control for Northstar Water Services. Explain what one water-pipe service work order represents, the reporting date, the five job categories and how current owners differ from proposed owners. Do not edit or infer customer impacts.
   ```

2. Use Chat only to inspect the named table before making changes. Record row count and the two exact repeated IDs. A Work_Order_ID is the row grain; do not count repeated export records twice.

   ```text
   EXCEL - CHAT ONLY:
   Inspect tblWorkOrders. Report row count, duplicate Work_Order_ID values, category spelling variants and missing Assigned_To. Do not edit. Treat 2026-09-30 as the fixed reporting date.
   ```

3. Choose Plan if available. Read the proposed cleaning plan before using Allow editing. The duplicates are exact repeated export records: keep one per ID. Trim and standardise category labels to Leak Repair, Valve Repair, Pipe Replacement, Pump Service, Meter Service; preserve missing owners and all unique source values. Save a copy of the raw sheet before the change.

   ```text
   EXCEL - PLAN:
   Plan to retain an untouched Raw_Export copy, remove only exact duplicate records by Work_Order_ID, and standardise category spelling in tblWorkOrders. Keep dates, statuses and assignments. Ask if two records with one ID differ.

   EXCEL - ALLOW EDITING:
   Apply the reviewed plan. Keep one identical record per repeated ID. Do not guess missing owners. Reconcile the cleaned table against Control.
   ```

4. Add a Checks sheet or use the supplied one. Ask for formulas, then inspect the table and formulas yourself. Overdue excludes Closed and Cancelled and uses strictly earlier than the fixed date, so a due-today job is not overdue. Copy verified values to data/templates/Evidence_Register.csv.

   ```text
   EXCEL - ALLOW EDITING:
   In Checks calculate total rows, closed, cancelled, backlog, overdue backlog, unassigned backlog and total Cost_SGD for tblWorkOrders. Use Control!B2 as reporting date. Define backlog as Status neither Closed nor Cancelled. Add the identity total = closed + cancelled + backlog. Do not change source data.
   ```

5. Open data/templates/Northstar_Operations_Brief_Template.docx in Word and save as Northstar_Operations_Brief.docx in OneDrive. In Copilot select the verified source file using Reference a file or /. If Word cannot use the workbook, copy your verified evidence table plus data/Northstar_Maintenance_Context.txt into the document and select that text; do not imply Word reads the Excel chat.

   ```text
   WORD COPILOT:
   Draft a one-page Northstar operations brief from the verified evidence supplied here. Include reporting scope/date, backlog and overdue findings, current assignment issues, proposed next actions and open questions. Keep observed facts separate from proposals. Preserve numbers and definitions. Use UNKNOWN for causes, approvals or capacity decisions not evidenced.
   ```

6. Compare every number and work-order ID in the Word brief to Checks and the evidence register. Add the OneDrive source link and all-filters scope. Log the Word prompt manually in Excel Prompt_Log because Excel cannot access the Word conversation. Save the cleaned workbook and brief for Lab 2.

   ```text
   WORD COPILOT:
   Audit this Northstar Water Services operations brief against the verified evidence table I supply. Return a discrepancy list for counts, cost, reporting scope, overdue definition and assignment claims. Identify missing source links as UNKNOWN. Do not change facts or approve work.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| Excel | Count unique work-order IDs and reconcile backlog using the fixed reporting date. |
| Word | Draft an operations brief from the checked evidence; label proposals and unknowns. |

**Test it**

| Check | Expected result |
|---|---|
| Clean table | 120 unique Work_Order_ID rows; five canonical job categories. |
| Portfolio identity | 120 = 48 Closed + 12 Cancelled + 60 backlog. |
| Evidence handoff | Overdue 50; unassigned backlog 6; total cost S$35,827.50. Word agrees with Excel. |
| No guessed owner | Blank assignments remain blank; proposals labelled unapproved. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-01-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---

Concepts for Lab 2: Prompts and Verified App Handoffs, Outlook Drafting and Operational Decisions.


### Prompts and Verified App Handoffs

A useful prompt combines the intended goal, operational context, named source and output expectations. The handoff object is a verified artifact, such as a Word brief with a checked metric table and source links. It is not an assumption that another app can remember the preceding conversation. For maintenance, expectations should specify exact dates, status vocabulary, current versus proposed assignments and missing-value behaviour.

The same number may have different meaning when a chart counts all work orders while an email calls it open backlog. A cross-app evidence register records the claim, value, source table, filter scope and date. This provides a small reproducible contract for each output and lets a reviewer identify a mismatch before it becomes a management decision.

**How it works**

- Write the goal and audience.
- Attach or select the actual source.
- Specify definitions and missing-value behaviour.
- Reconcile the returned claims.

**Worked example**

- Goal: draft a maintenance update for the operations manager.
- Source: reviewed Northstar operations brief, all filters All, 30 September.
- Expectation: label assignment suggestions as proposals and leave unknown approvals UNKNOWN.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A reviewed brief can be selected or its checked text pasted. | Only an unverified summary is available. |

**Authoritative references**

- https://support.microsoft.com/en-gb/word/copilot/draft-and-add-content-with-copilot-in-word
- https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint
- https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot

---


### Outlook Drafting and Operational Decisions

Copilot can help structure a draft email from supplied context. A synthetic text thread is quoted context, not a live Outlook conversation; the course explicitly uses it that way. The writer remains responsible for recipients, claims, attachments, tone and the distinction between a proposed action and an approved instruction. Saving a draft does not send it or authorise a work-order change.

An apparently routine update can accidentally promise technician reassignment or imply that a manager approved a recovery plan. Current assignment is recorded data; proposed assignment is a separate planning output. Available hours are one input to planning, not evidence of approval or guaranteed productivity. The final email should request the decision rather than claim it has happened.

**How it works**

- Provide the synthetic thread and checked facts.
- Draft a concise update.
- Review recipients, facts and action wording.
- Save the unsent draft and evidence.

**Worked example**

- Current owner blank; proposed owner Aisha remains unapproved.
- A draft addressed to example.invalid is a training artifact.
- The handoff says decision requested, not decision approved.

**Decision guide**

| Use when | Avoid when |
|---|---|
| You can check the evidence and review the draft before use. | The task would imply a real approval or send without review. |

**Authoritative references**

- https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot

---


### Lab 2 · Word to PowerPoint and Outlook — Create the Cross-App Maintenance Update

Learning outcome: LO1: integrate verified Word, Excel, PowerPoint and Outlook outputs.

Goal: Northstar_Initial_Update.pptx, an unsent Outlook draft and Northstar_Cross_App_Evidence.csv with Excel, Word, PowerPoint and Outlook figures reconciled.

Continue the verified operations brief from Lab 1. You will turn it into an initial PowerPoint update, then prepare an Outlook reply to a synthetic maintenance thread. You will test how grounding differs between an attached file, a chat transcript and a reviewed summary, and reconcile the same facts across all four apps.

**What you'll build**

Northstar_Initial_Update.pptx, an unsent Outlook draft and Northstar_Cross_App_Evidence.csv with Excel, Word, PowerPoint and Outlook figures reconciled.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Verified Lab 1 workbook and Word brief, or supplied checkpoint and snapshot.

**Step-by-step**

1. Open your Lab 1 Word brief and cleaned workbook. If needed use this lab’s verified checkpoint and snapshot, clearly recording rejoin. Read data/Northstar_Email_Thread.txt. It asks for a portfolio update, not authorisation to reassign technicians.

   ```text
   WORD COPILOT:
   From this selected verified Northstar Water Services operations brief, extract a handoff table with reporting date, filter scope, total, closed, cancelled, backlog, overdue, unassigned backlog and recorded cost. Separate facts, proposed next actions and open decisions. Keep every value traceable to the supplied brief.
   ```

2. Open data/templates/Northstar_Management_Deck_Template.pptx in PowerPoint and save as Northstar_Initial_Update.pptx. For this initial update use four slides by keeping the first four layout slides and deleting the remaining unused template slides. Open Copilot and select your Word brief with Reference a file; if the command is unavailable, paste the reviewed brief into the prompt.

   ```text
   POWERPOINT COPILOT:
   Using this verified Northstar Word brief, create a four-slide initial update: scope and portfolio; backlog and overdue work; current assignments and proposed actions; decision required. Use the existing white/navy/blue design. Preserve all verified metrics. Add source/date notes. Do not invent completed work, savings or approved reassignment.
   ```

3. Review all four slides. Check status definitions, units and date, and correct any invented claim. Save a reconciled CSV using data/templates/Evidence_Register.csv: one row per claim and a source link. This is the bridge between app outputs; app chats are not automatically shared.

   ```text
   POWERPOINT COPILOT:
   Audit these four Northstar Water Services slides against the selected verified operations brief. For each numeric claim give the source, date and scope; flag unsupported service-restoration, safety, customer-impact or approval claims. Propose corrections without changing the checked values.
   ```

4. In Outlook create a new training draft addressed to operations.manager@example.invalid with subject DRAFT - Northstar maintenance update - review required. Do not send. Paste the synthetic thread into the draft or use it as quoted context; Copilot summarises the supplied text, not a real mailbox thread. Open Copilot > Draft with Copilot; UI names may differ.

   ```text
   OUTLOOK COPILOT:
   Draft a concise reply to the synthetic thread quoted below, using the verified Northstar brief and these checked metrics. State the 30 September 2026 scope, backlog/overdue findings, proposed next actions and the decision requested. Explain that assignments are unapproved proposals. Do not claim the attachments have been sent. Keep as a draft.
   ```

5. If your Outlook offers reference attachments, attach the verified Word brief and choose it as context. Otherwise paste the reviewed metrics into the drafting prompt. Replace any placeholder summary with exact checked values; inspect recipients, subject, tone and attachment names. Save only the draft and a local TXT copy of its reviewed body.
6. Ask Word Copilot to compare your pasted slide/email summaries with the brief, then perform the same comparison yourself. Add the cross-app prompt log entries manually. Keep all four source links with the reconciliation record; any mismatch must be fixed before the skill labs.

   ```text
   WORD COPILOT:
   Compare these pasted PowerPoint and Outlook summaries with this verified Word brief. List inconsistent figures, status definitions, dates, owner claims or approved-action wording. Do not resolve a conflict by guessing. Return a discrepancy table with source and correction needed.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| PowerPoint | Turn the reviewed brief into a four-slide update with source/date notes. |
| Outlook | Draft the maintenance reply from the same checked values; keep it unsent. |

**Test it**

| Check | Expected result |
|---|---|
| Four apps | Excel Checks, Word brief, four-slide update and unsent Outlook draft share the same date and values. |
| Cross-app grounding | Named file or pasted verified evidence is provided in each app; no assumed shared chat. |
| Draft boundary | example.invalid recipient; nothing sent and no assignment approved. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-02-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---


### Topic 1 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO1 | Same work-order evidence across four apps. |
| Verify | 120 clean IDs and reconciled brief/update/draft. |

---


## Topic 2 — Create Skills for Microsoft 365 Copilot

A reusable method for Excel and PowerPoint

**Key concepts**

- SKILL.md — Matching folder/name and reusable instructions.
- Discovery — Install and verify separately in each app.
- Repeatability — Input guards and controlled reruns.
- Proposals — Preserve source owners and evidence boundaries.

Concepts for Lab 3: Skills, Prompts and Workbook Rules, Custom Skill Discovery in Each App.


### Skills, Prompts and Workbook Rules

A prompt is one request. A custom skill is a reusable set of instructions that tells Copilot when and how to perform a recurring task. SKILL.md contains required YAML name and description followed by the instructions. Each skill needs its own folder with a matching name. Workbook-specific rules describe constraints for one workbook; a skill can carry the same maintenance process across repeated reports and supported apps.

The skill makes stable definitions and review boundaries reusable: backlog excludes two terminal statuses, overdue uses a fixed date, missing owners stay missing and output reruns do not duplicate sheets. It does not supply absent work-order data or turn an unsupported app feature into an available one. Skill availability must be verified separately in the app where it will run.

**How it works**

- Identify a recurring task.
- Separate stable rules from current inputs.
- Write name, description and instructions.
- Install, invoke and inspect the result.

**Worked example**

- maintenance-reporting contains definitions and output boundaries.
- Each request still supplies this month’s source, date and scope.
- Native skill use and pasted manual instructions are recorded differently.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The same reporting method recurs and can be tested. | Inputs or desired behaviour are still undefined. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-skills
- https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills

---


### Custom Skill Discovery in Each App

Excel uses its Manage plugins & skills interface and an app-created OneDrive skills folder. PowerPoint uses Choose skills and Manage skills with an Add skill/upload route or its own custom skills folder. The app UI resolves the supported folder; a guessed universal path is unreliable. Refresh and enable the skill, then verify the exact name in each app before invoking it by @mention or the menu.

Folder-name/frontmatter mismatches, an extra .txt extension, unavailable licence features and disabled skills can all prevent discovery. A web Copilot authoring conversation can produce the complete Markdown text, but the learner still saves, installs and tests it. Excel cannot log the web chat automatically. Clear installation evidence prevents confusing a manually pasted policy with a native reusable skill.

**How it works**

- Save complete UTF-8 SKILL.md.
- Use the app-created skills location.
- Refresh and verify the matching name.
- Run and record a smoke test.

**Worked example**

- Folder maintenance-reporting matches YAML name maintenance-reporting.
- Excel and PowerPoint both show the skill before native invocation.
- If a menu is absent, manual practice is labelled feature unavailable.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The app exposes its supported skill installation controls. | A missing menu is being treated as successful installation. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-skills
- https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills

---


### Lab 3 · Author SKILL.md — Create a Custom Maintenance Reporting Skill

Learning outcome: LO2: create and improve a reusable maintenance skill in Excel and PowerPoint.

Goal: A reviewed maintenance-reporting/SKILL.md v1, a smoke-test record, and a native-skill or explicitly labelled manual-practice route for each app.

Capture the maintenance definitions and reporting style as one custom skill. You will ask Microsoft 365 Copilot on the web to write SKILL.md, compare it with a supplied complete template, install it in each app’s own supported skills location, and perform a small smoke test. A skill is reusable instructions, while a prompt is one request and workbook rules govern one file.

**What you'll build**

A reviewed maintenance-reporting/SKILL.md v1, a smoke-test record, and a native-skill or explicitly labelled manual-practice route for each app.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.

**Step-by-step**

1. Read data/templates/maintenance-reporting/SKILL.md and data/Northstar_Maintenance_Context.txt. Open Microsoft 365 Copilot at https://copilot.cloud.microsoft in your assigned account. Provide the skill requirements as prompt context. Do not upload private work data.

   ```text
   MICROSOFT 365 COPILOT WEB:
   Write a complete SKILL.md for maintenance-reporting. Require YAML name and description, input table or verified Word snapshot, report date and filter scope. Define backlog, overdue and on-time closed rate. Preserve IDs/status/current owners. Put assignment suggestions in a separate proposals sheet. Support Excel outputs and PowerPoint storytelling with source notes, existing white/navy/blue style, no invented facts and safe reruns. Never send email or approve assignments. Ask for missing inputs. Return the entire Markdown file.
   ```

2. Copy the complete returned file into a plain text editor, save UTF-8 as SKILL.md in a folder named maintenance-reporting, not SKILL.md.txt. Check the opening --- name/description --- block. Compare every definition and boundary with the supplied template. Edit missing instructions and retain your own version at work-c027/maintenance-reporting-v1/SKILL.md.

   ```text
   MICROSOFT 365 COPILOT WEB:
   Review this supplied maintenance-reporting SKILL.md for Northstar Water Services. Check YAML name/description, required source/date/scope, backlog and overdue definitions, source preservation, assignment proposal boundaries, app-specific context and safe reruns. Return exact corrections and then the complete revised file; do not invent missing data.
   ```

3. Open data/Northstar_Work_Orders.xlsx in Excel and save a working copy first. Then open Copilot > ... > Manage skills (or Manage plugins & skills) > Custom skills > Create OneDrive folder (if needed) > Open skills folder. Put the maintenance-reporting folder containing SKILL.md inside that app-created folder. Return to Custom skills and select Refresh. Enable the skill and verify the exact name; do not guess the OneDrive folder path.
4. In that Lab 3 workbook invoke the skill from Add work content > Choose skills (or Choose plugins & skills) or @mention. Inspect the proposed plan before editing; keep the source table unchanged. Save the result as Northstar_Skill_Smoke_Test.xlsx. If the Excel skills menu is absent, paste the complete reviewed SKILL.md as instructions before the test prompt, omit @mention, and record Manual practice - native skill unavailable.

   ```text
   EXCEL - CHAT ONLY:
   @maintenance-reporting Explain the reporting definitions for tblWorkOrders at 2026-09-30, all filters All. State which sheets you may change, how missing owners are handled, and what you need before producing a PowerPoint update. Do not edit yet.
   ```

5. Open PowerPoint template > Copilot > + > Choose skills > Manage skills > Add skill. Upload your SKILL.md or paste it in Add skill as supported; verify it appears and is enabled. Alternatively use Manage skills > Custom skills > Open skills folder and copy the correctly named folder there. The PowerPoint location is app-created; installing in Excel alone is not proof it is available in PowerPoint.
6. Run a PowerPoint smoke test with the verified snapshot selected as a file reference. Record the actual app name, selected skill name and response. If a skills menu is absent, paste the complete reviewed skill as instructions alongside the snapshot and mark Manual practice - native skill unavailable. Do not claim a native invocation.

   ```text
   POWERPOINT COPILOT:
   @maintenance-reporting Using the selected Northstar_Verified_Snapshot.docx, propose an eight-slide maintenance report outline. Explain how every claim will be grounded and which actions remain proposals. Keep the reporting date and scope visible; do not edit slides yet.
   ```

7. Log the web authoring prompt and PowerPoint test manually in workbook Prompt_Log. For Excel log the actual response and your check. Keep the v1 file and test notes for Lab 4; no app can automatically read the other app’s chat.

   ```text
   EXCEL - CHAT ONLY:
   Using only the web and PowerPoint smoke-test responses I paste here and this workbook test response, prepare a Prompt_Log comparison. Record the app, source, scope, actual behaviour and my verification. Leave missing responses UNKNOWN. Do not claim access to another app chat or a successful test without evidence.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| Web Copilot | Write complete maintenance-reporting SKILL.md with input guards and reporting definitions. |
| Excel / PowerPoint | @maintenance-reporting Explain your inputs and output boundaries before making changes. |

**Test it**

| Check | Expected result |
|---|---|
| Skill format | maintenance-reporting folder; matching name in YAML; nonempty description; UTF-8 SKILL.md. |
| Metric controls | Backlog excludes two terminal statuses; due-today not overdue; zero closed -> N/A. |
| Installation evidence | Excel and PowerPoint names verified separately, or manual route honestly recorded. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-03-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx), plus data/templates/maintenance-reporting/SKILL.md (Complete custom maintenance skill template). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---

Concepts for Lab 4: Repeatability and Safe Skill Reruns, Assignment Proposals and Capacity Evidence.


### Repeatability and Safe Skill Reruns

Repeatability means the same verified inputs and method yield equivalent business measures and a controlled output structure. A safe rerun preserves source IDs, statuses, assignments and unrelated sheets. It creates or replaces only explicitly named outputs after review. The concept is similar to idempotence: rerunning should not append duplicate summaries, inflate totals or silently destroy a learner’s unrelated work.

Reporting skills may be used every week or month, so uncontrolled output accumulation quickly creates conflicting summaries. An input guard asks for missing data; a replacement guard identifies the output to change. Test those guards using a copy and compare row count, sums, sheet inventory and output measures before and after, rather than relying on Copilot saying it was careful.

**How it works**

- Capture the source fingerprint and outputs.
- Request a reviewed rerun plan.
- Replace only named output areas.
- Compare source and measures again.

**Worked example**

- 120 source IDs remain 120 after rerunning Maintenance_Summary.
- Missing report date causes a clarification request, not invented numbers.
- A second output sheet is a defect when replacement was requested.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Named output boundaries and reconciliation checks exist. | The skill can overwrite source rows or unrelated sheets. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-skills
- https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills

---


### Assignment Proposals and Capacity Evidence

Assignment planning combines the work category, existing owner, estimated hours, technician primary category and available hours. These inputs help generate a proposal; they do not prove complete operational suitability, approved schedules or safety authorisation. Keep Current_Assigned_To separate from Proposed_Assigned_To and use an explicit manager-decision field. Missing evidence is UNKNOWN, not a confident allocation.

The same skill can improve Excel analysis and PowerPoint wording by preserving this boundary. Excel shows category/capacity checks and assumptions in a proposals sheet; PowerPoint explains the findings and requests a decision. A polished visual must not conceal uncertain capacity or make the proposed owner look like the current owner.

**How it works**

- Identify unassigned backlog.
- Compare category and available hours.
- Record the proposal and assumptions.
- Request the manager decision.

**Worked example**

- Unassigned work is counted only within nonterminal statuses.
- Available hours minus proposed effort is a planning check.
- The source Assigned_To stays unchanged until a real authorised operational update.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A manager can review the proposal and missing constraints. | The report claims automatic approval or verified safety qualification. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-skills
- https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills

---


### Lab 4 · Repeatable reporting — Use and Improve the Skill in Excel and PowerPoint

Learning outcome: LO2: create and improve a reusable maintenance skill in Excel and PowerPoint.

Goal: Northstar_Skill_Report.xlsx with Maintenance_Summary and Assignment_Proposals, Northstar_Skill_Update.pptx, SKILL.md v2 and a before/after improvement log.

Use the Lab 3 skill to create a verified summary and improve the initial PowerPoint update. Then deliberately test missing inputs and a rerun, tighten the skill to v2, and compare before/after evidence. The target is consistent reporting, not a longer prompt or an unsupported promise of autonomous approval.

**What you'll build**

Northstar_Skill_Report.xlsx with Maintenance_Summary and Assignment_Proposals, Northstar_Skill_Update.pptx, SKILL.md v2 and a before/after improvement log.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Lab 3 skill v1 and test record; Lab 2 update, or named supplied checkpoints.

**Step-by-step**

1. Copy the Lab 3 reviewed SKILL.md to your output folder and retain v1. Open this lab’s clean workbook or your Lab 1 cleaned workbook. Save as Northstar_Skill_Report.xlsx. Read Technicians: primary category and available hours are synthetic planning inputs, not approvals. Check that your skill is enabled in Excel.
2. Invoke the skill in Plan or Chat only, review its proposed output boundaries, then allow editing. Inspect the resulting formulas and charts. Summary counts must reconcile to Control, and the source table must remain 120 unique records.

   ```text
   EXCEL - PLAN:
   @maintenance-reporting Build Maintenance_Summary for tblWorkOrders at 2026-09-30 with all filters All. Include total, closed, cancelled, backlog, overdue, on-time closed rate and recorded cost; show formulas and source scope. Plan first. Preserve source records.

   EXCEL - ALLOW EDITING:
   Apply that reviewed summary plan. Add Assignment_Proposals for unassigned backlog only. Use tblTechnicians primary category and available hours as planning inputs; show category/capacity checks, current owner and proposed owner separately. Leave manager decision UNKNOWN. Do not change Assigned_To.
   ```

3. Check the unassigned backlog count against Control. A technician with the same category may still lack usable capacity: use available hours minus known proposed hours, flag conflicts, and do not convert a suggestion into confirmed assignment. Export your verified summary into the Word snapshot template, preserving measures and date.

   ```text
   EXCEL - CHAT ONLY:
   @maintenance-reporting Review Assignment_Proposals against tblWorkOrders and tblTechnicians. Check each suggested owner has the matching water-service job category, capacity limitations are visible and original Assigned_To values are unchanged. Leave manager approval UNKNOWN; do not assign or schedule a technician.
   ```

4. Open the four-slide initial update from Lab 2, or use data/checkpoints/Northstar_Initial_Update_Checkpoint.pptx, a four-slide rejoin example explicitly labelled as a checkpoint. Save as Northstar_Skill_Update.pptx. Select the reviewed snapshot in PowerPoint and invoke your installed skill.

   ```text
   POWERPOINT COPILOT:
   @maintenance-reporting Improve this existing initial maintenance update from the selected verified snapshot. Retain four slides and accurate values; strengthen claim headlines, simplify text, improve source notes and use the current design. Do not duplicate slides or imply live links to Excel. Label suggested reassignment as proposed.
   ```

5. Create a new EMPTY workbook with no table, open a fresh Copilot chat and run a missing-input test for a different reporting period with no source selected. A proper skill asks for source/date/scope rather than inventing metrics. If it guesses, record the failure and revise the skill’s input guard. Return to Northstar_Skill_Report.xlsx and Save As Northstar_Skill_Rerun_Test.xlsx. Run the second summary request in this copy of the report workbook, not in the empty workbook; only named outputs may be replaced after review, with no duplicated source or output sheets. Compare a before/after copy of Work_Orders sorted by Work_Order_ID for status, owner, dates and cost; every original source value must match.

   ```text
   EXCEL - CHAT ONLY:
   @maintenance-reporting Prepare my next maintenance report. I need a DIFFERENT reporting period from the course example and have not supplied any source, date or scope. This empty workbook contains no work orders. Tell me what you need; do not invent data.

   EXCEL - PLAN:
   @maintenance-reporting Rebuild the existing Maintenance_Summary for the same table, date and scope. Describe what will be replaced, ask before replacement and keep source/unrelated sheets. Do not duplicate outputs.
   ```

6. In a plain text editor improve SKILL.md: require an input guard, category/capacity evidence, source provenance per claim and a clear rerun rule. Retain YAML name maintenance-reporting and add a body version note v2. Re-upload/Refresh in BOTH Excel and PowerPoint. Record actual before/after changes, or already present - retained for safeguards that your v1 already contains. Do not fabricate differences. Rerun the smoke tests and compare values. If using the manual route, replace the pasted instructions in both apps.

   ```text
   MICROSOFT 365 COPILOT WEB:
   Improve this supplied maintenance-reporting skill to v2 using only my actual smoke-test and rerun findings pasted here. Add explicit missing-input and no-duplicate-output guards. Keep Excel source and current owners protected. Return the complete revised SKILL.md and a short before/after change log; do not fabricate test evidence.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| Excel | @maintenance-reporting Build the verified summary and separate assignment proposals. |
| PowerPoint | @maintenance-reporting Improve the existing four-slide update; preserve facts and count. |

**Test it**

| Check | Expected result |
|---|---|
| Source preserved | 120 unique orders; current owner/status unchanged. |
| Skill outputs | Backlog 60; overdue 50; on-time closed 30/48; cost S$35,827.50. |
| Improvement evidence | Input guard and rerun tested; v1/v2 retained; PowerPoint four-slide output accurate. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-04-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx), plus data/templates/maintenance-reporting/SKILL.md (Complete custom maintenance skill template). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---


### Topic 2 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO2 | Skill authoring, discovery, use and revision proven. |
| Verify | Preserved source plus missing-input and rerun tests. |

---


## Topic 3 — Create an Interactive Dashboard with Excel Copilot

From definitions to filters and refresh evidence

**Key concepts**

- Measures — Counts, backlog, overdue, on-time rate and cost.
- Visuals — Choose charts by maintenance question.
- Interactions — One filter scope for every chart and KPI.
- Refresh — Known deltas in an isolated test copy.

Concepts for Lab 5: Dashboard Measures and Denominators, Visual Dashboard Design for Maintenance.


### Dashboard Measures and Denominators

A dashboard measure needs a business definition, numerator, denominator where relevant, date rule and filter scope. Total orders describes the selected portfolio. Backlog is the selected nonterminal work. Overdue is a subset of backlog. On-time closure rate describes Closed rows only: closed on or before their due date divided by Closed rows. Recorded cost sums selected Cost_SGD; it is not a budget variance or inferred savings.

Changing the denominator can make an attractive rate meaningless. If the selected data contains no Closed rows, the on-time rate is N/A because it is undefined; a displayed 0% would falsely suggest failed delivery. A Measures dictionary and independent control sheet make the definitions inspectable. A fixed reporting date gives reproducible comparisons, while TODAY would change the snapshot over time.

**How it works**

- Define source fields and scope.
- Compute count and denominator.
- Handle empty selections explicitly.
- Reconcile against controls.

**Worked example**

- Closed-only rate is different from closed/total completion share.
- A due-today backlog item is not overdue under a strict before-date rule.
- All selected status/chart counts reconcile to total selected work orders.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Measures have agreed definitions and evidence. | A zero denominator is being represented as a measured 0%. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/create-and-share-a-dashboard-with-excel-and-microsoft-groups

---


### Visual Dashboard Design for Maintenance

A dashboard should make an operational decision easier. KPI cards summarise magnitude; bar charts compare sites, categories or status counts. Labels, units and source/date context define what each visual means. Site backlog and total orders by site answer different questions and must have different names. Use a line chart for a genuine ordered time series, not unordered site names.

Consistent chart scales, short labels, whitespace and limited accents help a manager compare the work queue quickly. Colour alone is insufficient to distinguish statuses. A category count is evidence of frequency, not a causal diagnosis; a busy site is not necessarily performing badly. Choose the visual based on the question and include the limitation that prevents overinterpretation.

**How it works**

- Name the maintenance decision.
- Choose the measure and comparison.
- Use an appropriate labelled chart.
- Check meaning and readability.

**Worked example**

- Status count chart shows the portfolio mix.
- Site backlog chart excludes Closed and Cancelled.
- A category count does not establish the root cause of overdue jobs.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The visual has a clear audience and question. | Decorative charts hide an ambiguous metric. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/create-and-share-a-dashboard-with-excel-and-microsoft-groups

---


### Lab 5 · Design and build — Build Maintenance Dashboard Measures and Charts

Learning outcome: LO3: build and validate an interactive Excel maintenance dashboard.

Goal: Northstar_Dashboard.xlsx with a Dashboard layout, six verified measures, three labelled charts and a measure dictionary ready for Lab 6 filters.

Use Excel Copilot to plan a maintenance dashboard for operations managers. Define the measures before designing the charts, then build source-linked KPI cards and a status, category and site chart. You will distinguish stock measures such as current backlog from flows such as closures, and avoid calling category frequency a root cause.

**What you'll build**

Northstar_Dashboard.xlsx with a Dashboard layout, six verified measures, three labelled charts and a measure dictionary ready for Lab 6 filters.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Verified clean table from earlier labs or supplied clean checkpoint.

**Step-by-step**

1. Open data/templates/Northstar_Dashboard_Starter.xlsx and save as Northstar_Dashboard.xlsx in OneDrive. If continuing your own workbook, copy its CLEAN tblWorkOrders into the starter, keeping exact headers and table name; do not create a second table. The starter has a labelled blank Dashboard and four selection cells B2:B5, initially All.

   ```text
   EXCEL - CHAT ONLY:
   Inspect this Northstar Water Services dashboard starter. Confirm tblWorkOrders, 120 unique IDs, reporting date 2026-09-30 and selection cells B2:B5 initially All. Explain which source and control sheets must remain intact. Report discrepancies before any edits.
   ```

2. Read Control and confirm the fixed reporting date. Ask for a visual plan before edits. Keep source, Checks and Prompt_Log separate from the Dashboard view. A dashboard is a decision interface: each visual should answer a maintenance question rather than decorate the page.

   ```text
   EXCEL - PLAN:
   Plan Dashboard for Northstar maintenance at 2026-09-30. Use selection cells B2:B5 for Site, Job_Category, Status, Assigned_To, all initially All. Reserve B7 total orders, B8 backlog, B9 overdue backlog, B10 closed, B11 on-time closure rate, B12 Cost_SGD. Place three charts for status, category and site with labels, units and scope. Preserve source data.
   ```

3. Ask Copilot to insert formulas for the six measures using structured table references. For now all selectors are All; in Lab 6 the same formulas must honour the four filters. Verify the denominator and use N/A, not 0%, if no Closed rows remain.

   ```text
   EXCEL - ALLOW EDITING:
   Build the planned six KPI formulas from tblWorkOrders. Backlog excludes Closed/Cancelled. Overdue also requires Due_Date < Control!B2. On-time rate counts Closed_Date <= Due_Date among Closed rows only, and shows N/A when none. Recorded cost sums Cost_SGD of all included statuses. Link to table columns, never a fixed 120-row range. Keep source data unchanged.
   ```

4. Add formula-backed chart summaries for the six statuses, five categories and five sites. Use bar/column charts: category and site are nominal groups; a line chart would imply an order that is not present. Label count axes and avoid 3-D effects. Ask the skill for consistent style if available.

   ```text
   EXCEL - ALLOW EDITING:
   Create three editable bar or column charts using formula-backed summaries: work-order count by Status, by Job_Category and by Site. Each summary must reconcile to the total selected orders. Use white background, navy titles, blue/teal accents, readable labels and a visible reporting date. Do not use category counts as evidence of causes or use colour alone for status.
   ```

5. In Checks confirm sum of each chart’s categories equals 120 with All filters. Compare six KPIs to Control and record the on-time numerator/denominator. Add data/templates/Evidence_Register.csv entries for each chart and metric. If Copilot has used hard-coded numbers, replace them with formulas before Lab 6.

   ```text
   EXCEL - CHAT ONLY:
   Reconcile the Northstar Water Services dashboard with Control at All selections. Compare all six KPIs and totals of the Status, Job_Category and Site charts. Flag hard-coded values, fixed row ranges, inconsistent scopes and any interpretation that treats job-category frequency as a cause. Do not edit.
   ```

6. Create a measure dictionary on a new Measures sheet: metric, business definition, formula, source fields, date rule, scope and limitation. Ask Copilot to explain formulas, then read one overdue example and one closed example from the source table yourself. Save the baseline dashboard with all filters All.

   ```text
   EXCEL - CHAT ONLY:
   Explain each Dashboard measure in plain English, including terminal statuses, strict overdue date rule, closed-only SLA denominator and meaning of recorded cost. Give one source-row example for overdue and one for on-time closure; cite Work_Order_ID. Do not guess a root cause or financial saving.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| Excel | Plan six dashboard measures and three charts from tblWorkOrders; preserve source data. |
| Excel | Explain the closed-only SLA denominator and verify it against source rows. |

**Test it**

| Check | Expected result |
|---|---|
| Baseline | Total 120; backlog 60; overdue 50; closed 48. |
| SLA and cost | 30/48 = 62.5%; S$35,827.50. |
| Chart reconciliation | Three count summaries each total 120; formulas reference tblWorkOrders. |
| Decision design | Measures dictionary and source/date visible; no unsupported cause claims. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-05-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---

Concepts for Lab 6: One Filter Scope for Every Visual, Refresh Tests and Static Snapshots.


### One Filter Scope for Every Visual

Interactive means a learner-controlled selection changes the evidence shown. This course’s portable route uses four dropdowns and formula measures with AND logic. All bypasses one dimension only. Every KPI and chart uses the same selected rows. Optional slicers filter connected PivotTables; they do not automatically alter unrelated formulas or every table on the sheet. PivotTables sharing a slicer need the same source.

A dashboard can appear interactive while only one chart changes. Test a single-site selection, a combined category/owner selection and an empty selection. Check the displayed scope and compare every chart total with the selected total. Worksheet AutoFilter and formula-selector filters are different mechanisms; hiding source rows does not prove that formulas have changed scope.

**How it works**

- Define the selector cells.
- Apply the same AND mask everywhere.
- Test each control and edge case.
- Reconcile selected chart and KPI totals.

**Worked example**

- Woodlands Hub plus All in other selectors isolates that site.
- Status New gives zero Closed and N/A closure rate.
- A slicer must connect to every intended PivotTable.

**Decision guide**

| Use when | Avoid when |
|---|---|
| All output calculations follow the same scope. | A selector only changes a decorative title or one chart. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/get-started/use-slicers-to-filter-data
- https://support.microsoft.com/en-us/excel/create-and-share-a-dashboard-with-excel-and-microsoft-groups

---


### Refresh Tests and Static Snapshots

A refresh test deliberately introduces known new records and verifies the expected delta. Table references should expand when rows are appended; PivotTables additionally need a refresh and valid source extent. The course adds two rows in a sandbox copy so the live baseline remains 120 rows. A Word/PDF/PowerPoint snapshot freezes evidence and does not automatically update when the Excel dashboard changes.

A correct dashboard today may fail after the next export if formulas reference a fixed cell range. Known delta testing reveals that failure. Preserving a separate baseline prevents a test record from contaminating the management pack. A snapshot should record source, as-at date, filters and version so its claims remain interpretable after the workbook is refreshed.

**How it works**

- Save an isolated sandbox copy.
- Append known unique test rows.
- Recalculate and verify expected deltas.
- Handoff the untouched baseline.

**Worked example**

- Two test rows increase total by2 and recorded cost byS$400.
- Only one new row adds to backlog/overdue; the other adds to on-time Closed.
- The final deck uses the untouched 120-row baseline, not the test copy.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A predictable change can be checked independently. | Test rows are being mixed into the report without disclosure. |

**Authoritative references**

- https://support.microsoft.com/en-us/excel/create-and-share-a-dashboard-with-excel-and-microsoft-groups

---


### Lab 6 · Filters and refresh — Make the Dashboard Interactive and Prove Refresh

Learning outcome: LO3: build and validate an interactive Excel maintenance dashboard.

Goal: Northstar_Dashboard.xlsx with four working filters plus Northstar_Dashboard_Refresh_Test.xlsx, filter evidence and a verified baseline snapshot for PowerPoint.

Continue Lab 5 by making four dropdown selectors control every KPI and chart. Test a single site, a zero-denominator selection and a combined category/owner filter. Then append two synthetic work orders in a sandbox copy and prove the dashboard expands. Optional PivotTable slicers use one source and shared connections; the portable dropdown route is the required working dashboard.

**What you'll build**

Northstar_Dashboard.xlsx with four working filters plus Northstar_Dashboard_Refresh_Test.xlsx, filter evidence and a verified baseline snapshot for PowerPoint.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Lab 5 dashboard or supplied formula checkpoint.

**Step-by-step**

1. Open your Lab 5 baseline dashboard. Rejoin using data/checkpoints/Northstar_Verified_Checkpoint.xlsx only if needed; record that it is an example formula dashboard. Set all four selections B2:B5 to All and confirm 120. Save baseline before creating any refresh-test copy.

   ```text
   EXCEL - CHAT ONLY:
   Before testing filters, report the baseline Northstar Water Services dashboard source, date and scope. Confirm 120 unique work orders and all four selectors All. Identify the baseline file that must remain untouched when making the refresh-test copy.
   ```

2. Use Data > Data Validation > Allow List to set dropdowns on B2 Site, B3 Job_Category, B4 Status and B5 Assigned_To. Include All plus the source values, using Filter_Lists if supplied. Ask Copilot to apply all four selections to EVERY KPI and chart summary. A selection of All bypasses only that filter; selected dimensions combine with AND.

   ```text
   EXCEL - PLAN:
   Make Dashboard B2:B5 control all six KPIs and three chart summaries with AND logic. All bypasses its dimension. Use COUNTIFS/SUMIFS or SUMPRODUCT with structured table references. Blank owner means unassigned and must not disappear from All. Keep N/A for no closed jobs.

   EXCEL - ALLOW EDITING:
   Apply the reviewed filter plan and dropdown lists. Keep existing source rows and chart positions. Show the selected scope beside the reporting date and make all charts recalculate from the same selected rows.
   ```

3. Choose Woodlands Hub in B2 and leave other selectors All. Filter the source table to the same site and compare rows, backlog, overdue and cost. Use Data > Clear on source table afterwards; dashboard selectors and source AutoFilter are distinct mechanisms. Record evidence in data/templates/Filter_Test_Log.csv.

   ```text
   EXCEL - CHAT ONLY:
   For the dashboard selection Site = Woodlands Hub and all other dimensions All, list the expected six KPI values from tblWorkOrders and verify each chart sum matches the selected total. Do not infer that filtering the worksheet automatically changes formula measures.
   ```

4. Set Status to New with other selectors All. Confirm zero closed -> N/A. Then set Site = Woodlands Hub, Job_Category = Leak Repair, Assigned_To = Daniel Lee, Status = All, a combination with no rows; total, backlog, overdue, closed and cost must be 0 and rate N/A. Reset all four to All and verify baseline controls. Optional: create PivotTables from one tblWorkOrders source, insert slicers, and use Slicer > Report Connections for every PivotTable; unconnected KPI cells are a defect.

   ```text
   EXCEL - CHAT ONLY:
   Check two dashboard edge cases without changing source data: Status New with other selectors All; then Site Woodlands Hub, Job_Category Leak Repair, Assigned_To Daniel Lee, Status All. Verify zero closed gives N/A and no selected rows gives zero count/cost with N/A rate. Show how all charts follow the same selection. Restore all selectors to All.
   ```

5. Save a COPY as Northstar_Dashboard_Refresh_Test.xlsx. In the last row of tblWorkOrders press Tab to append, then enter the two rows from data/Refresh_Test_Rows.csv with real Excel dates (YYYY-MM-DD). WO-2026-0121 is Assigned, due 2026-09-29 and cost 150; WO-2026-0122 is Closed on time and cost 250. No existing IDs are edited.
6. Recalculate with all selections All. If using PivotTables also Data > Refresh All and inspect source extent. Verify total122, closed49, backlog61, overdue baseline+1, cost baseline+400 and on-time numerator baseline+1 over49. If formulas do not expand, fix structured references/table extent. Keep this sandbox copy as refresh evidence; do not use its figures in the baseline presentation.

   ```text
   EXCEL - CHAT ONLY:
   Verify the sandbox append test for the two new work orders. Reconcile total 122, closed 49, backlog 61, overdue increased by 1, cost increased by S$400 and on-time numerator increased by 1. Confirm no original source record changed and all three charts total 122 with All selections. Compare original IDs, statuses, owners, dates and costs to the saved baseline; all original 120 rows must match.
   ```

7. Return to the untouched 120-row Northstar_Dashboard.xlsx. Set selectors All and record a frozen evidence snapshot dated 2026-09-30 for Lab 7. Copy data/templates/Northstar_Operations_Brief_Template.docx to Northstar_Verified_Snapshot.docx in Word and insert the reviewed summary and chart values. Save chart images if needed with right-click chart > Save as Picture; the slide copy will be a static snapshot, not a live dashboard.

   ```text
   WORD COPILOT:
   Using only the verified baseline dashboard evidence I paste here, prepare the frozen Northstar Water Services presentation snapshot. Include reporting date, All scope, 120-row baseline, six KPIs, chart values, source workbook link and limitations. Exclude the 122-row sandbox. Keep proposed priorities separate from observed facts.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| Excel | Apply Site, Category, Status and Owner selections to every KPI and chart. |
| Excel | Verify the sandbox append adds 2 orders and S$400 without changing original records. |

**Test it**

| Check | Expected result |
|---|---|
| Woodlands control | Total 24; backlog 8; overdue 7; closed 16; cost S$6,668.50; on-time 10/16. |
| Interactive scope | Changing any of four filters affects all six KPI measures and all chart counts. |
| Edge case | No Closed -> N/A; no rows -> zero count/cost and N/A rate. |
| Refresh sandbox | 122 total;49 closed;61 backlog;51 overdue;S$36,227.50;31/49 on-time. |
| Handoff baseline | Return to 120-row untouched baseline; date and All scope recorded. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-06-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---


### Topic 3 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO3 | Six measures and three charts share four filters. |
| Verify | Baseline controls and known refresh deltas. |

---


## Topic 4 — Create a Professional Presentation with PowerPoint Copilot

Continue the dashboard into a decision pack

**Key concepts**

- Evidence story — Observation, implication, action and decision.
- Charts — Reviewed values, provenance and snapshot date.
- Refinement — Hierarchy, notes and actual rehearsal feedback.
- Handoff — Reconciled pack and unsent communication.

Concepts for Lab 7: From Dashboard Evidence to a Decision Story, Charts, Templates and Source Provenance.


### From Dashboard Evidence to a Decision Story

A management presentation transforms evidence into a sequence of observations, implications, proposed actions and a decision request. Each slide needs one defensible headline and a register entry linking the claim to its measure, source, reporting date and filter scope. A chart contains data; the headline interprets it. That interpretation must stay within what the data supports.

Copilot can accelerate outlines and drafting, but a persuasive invented conclusion is still wrong. Before generating the deck, use Word to organise an eight-slide brief with a supporting chart and limitation for each claim. This explicit bridge makes the Excel-to-PowerPoint handoff reliable and avoids assuming a workbook can be used by every presentation-generation mode.

**How it works**

- Freeze the verified dashboard snapshot.
- Register each proposed claim.
- Write a reviewed Word brief.
- Generate and reconcile the deck.

**Worked example**

- Backlog by site supports prioritisation, not a proven cause.
- Available-hours evidence supports a capacity discussion, not confirmed allocation.
- The final slide asks management to decide on a proposed plan.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Every headline has a checked measure and clear scope. | The story introduces savings, causes or approvals absent from evidence. |

**Authoritative references**

- https://support.microsoft.com/en-gb/word/copilot/draft-and-add-content-with-copilot-in-word
- https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint
- https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot

---


### Charts, Templates and Source Provenance

A template supplies slide layouts, typography and colours; it does not supply correct facts. PowerPoint Copilot can draft slides from selected supported files. Reviewed Word briefs are a reliable narrative input for this course. Excel charts may be embedded for editing or pasted as images; both are copies of a reporting state unless a separate supported link is deliberately configured and tested.

Approximate AI-generated charts can contradict source values while looking plausible. Replace them with reviewed charts or verified tables and keep source/date notes. Distinguish all-work-order counts from backlog-only counts. A professional presentation uses consistent units and chart semantics, not just a consistent palette.

**How it works**

- Select the reviewed brief.
- Apply the existing template.
- Insert verified charts or tables.
- Record source and snapshot scope.

**Worked example**

- An editable embedded chart remains a copy rather than a tested live link.
- An image is labelled as a snapshot at 30 September.
- All eight slides use one reviewed baseline.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The chart object or image can be verified against the register. | A visual is assumed accurate because Copilot produced it. |

**Authoritative references**

- https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint
- https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot

---


### Lab 7 · Dashboard to presentation — Turn Dashboard Evidence into a Management Story

Learning outcome: LO4: turn verified dashboard evidence into a professional management presentation.

Goal: Northstar_Presentation_Brief.docx, Northstar_Management_Draft.pptx and a slide-by-slide evidence register tied to the 120-row dashboard snapshot.

Continue the baseline dashboard from Topic 3. Build a slide evidence register and a Word presentation brief before asking PowerPoint Copilot for an eight-slide management deck. The story connects work-order status, site backlog, service delivery and assignment proposals to a specific decision; it does not introduce unsupported savings or causes.

**What you'll build**

Northstar_Presentation_Brief.docx, Northstar_Management_Draft.pptx and a slide-by-slide evidence register tied to the 120-row dashboard snapshot.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Verified Lab 6 baseline dashboard and frozen evidence snapshot.

**Step-by-step**

1. Open the untouched baseline Northstar_Dashboard.xlsx from Lab 6; confirm All selectors, total120 and report date2026-09-30. Do not use the 122-row sandbox. If needed use this lab’s checkpoint and record rejoin. Copy verified metric/chart values to data/templates/Slide_Evidence_Register.csv with source sheet/table, scope and date.

   ```text
   EXCEL - CHAT ONLY:
   For the untouched 120-row Northstar Water Services baseline dashboard at 2026-09-30, All selectors, return a presentation evidence table: six KPIs, backlog by site, status and job-category counts, unassigned backlog and relevant source references. Do not use the refresh-test copy or infer service disruption, safety risk, causes or savings.
   ```

2. Open data/templates/Northstar_Presentation_Brief_Template.docx in Word. Add the verified summary and chart values plus the OneDrive workbook link. Save as Northstar_Presentation_Brief.docx. Copilot must see selected files or pasted evidence; the link alone and the Excel conversation do not guarantee accessible context.

   ```text
   WORD COPILOT:
   Using this verified 120-row Northstar maintenance snapshot, draft an eight-slide management presentation brief. For each slide give one claim headline, supporting measure/chart, source/date/scope, limitation and speaker note. Structure: overview, portfolio, site backlog, status/category mix, SLA/overdue, assignment/capacity, proposed actions/trade-offs, decision/next review. Do not invent causes, savings, approval or future dates; use UNKNOWN when absent.
   ```

3. Review the brief against source values. A bar showing counts by site is not a severity index; if you want backlog by site, count only nonterminal statuses. Correct any misleading headline and fill the slide evidence register. Suggested actions must cite a finding and say proposed.

   ```text
   WORD COPILOT:
   Review this eight-slide Northstar Water Services brief against the supplied baseline evidence. Check each headline has a supporting value, correct units, source/date/scope and an explicit limitation. Rewrite unsupported claims as questions or proposed actions. Do not change verified figures or invent approvals.
   ```

4. Open the supplied PowerPoint template, save as Northstar_Management_Draft.pptx and open Copilot. Choose Create presentation from file if offered, or reference the Word brief while editing the existing deck. Select your reviewed OneDrive Word brief; direct workbook-to-deck creation is not assumed. Invoke @maintenance-reporting if available.

   ```text
   POWERPOINT COPILOT:
   @maintenance-reporting Create or update an eight-slide management presentation from the selected Northstar_Presentation_Brief.docx. Follow the existing white/navy/blue template. One evidence-based message per slide, short visible text, charts or tables for numerical evidence, source/as-at/scope in notes, and a final decision request. Keep values exact, and label all next actions as proposed. Do not add extra slides or invented facts.
   ```

5. Replace approximate or invented charts with your reviewed Excel charts: copy chart in Excel, then PowerPoint Home > Paste > Paste Special > Microsoft Excel Chart Object for an editable embedded chart when supported; otherwise paste a static image and label it snapshot. Embedded copies and images do not automatically follow the original workbook. Use direct verified values if a chart object is unsupported.
6. Inspect all eight slides and notes. Check chart title, axis, unit, status definition, date and scope. Each numeric headline must match one register row. Confirm the deck uses baseline120, not refresh122. Save for Lab 8; do not represent the draft as an approved plan.

   ```text
   POWERPOINT COPILOT:
   Audit the eight-slide Northstar Water Services management draft against the selected presentation brief and evidence register. Confirm baseline 120, source notes, chart labels and units, correct backlog exclusions and proposed-action wording. List needed corrections and preserve slide count; do not claim Excel charts update automatically.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| Word | Create an eight-slide brief with one checked claim, source and limitation per slide. |
| PowerPoint | @maintenance-reporting Build the management deck from the reviewed Word evidence. |

**Test it**

| Check | Expected result |
|---|---|
| Evidence continuity | Every deck figure maps to the 120-row Lab 6 baseline and slide evidence register. |
| Eight-slide narrative | Observation -> implication -> proposed action -> decision; no invented cause/savings. |
| Chart semantics | Backlog charts exclude Closed/Cancelled; embedded/image copies labelled snapshot. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-07-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---

Concepts for Lab 8: Professional Refinement and Rehearsal, Reviewed Handoff and Artifact Lifecycle.


### Professional Refinement and Rehearsal

Refinement improves the clarity of the existing evidence without changing its meaning. Claim-led titles, short visible text, readable axes, consistent chart styles and concise speaker notes help an audience understand the maintenance decision. Rehearsal tests whether the audience can identify the reporting scope, the key finding and the decision required. It produces observed feedback, not a fabricated checklist completion.

A well-designed deck can still fail when the speaker’s notes contain different numbers or a proposal is spoken as an approved action. Review notes as part of the evidence pack and inspect the exported PDF at presentation size. Exporting can alter layout or font rendering, so the PDF must be opened and checked rather than assumed identical to the source.

**How it works**

- Audit the draft against evidence.
- Apply reviewed design changes.
- Rehearse and record actual feedback.
- Inspect PPTX and exported PDF.

**Worked example**

- One message per slide; chart labels remain readable.
- A 45-second note explains evidence and limitation.
- Partner feedback leads to one recorded revision.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The message and decision can be understood quickly. | Polish hides an unsupported claim or unreadable chart. |

**Authoritative references**

- https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills

---


### Reviewed Handoff and Artifact Lifecycle

The final pack contains an interactive Excel dashboard, a fixed reporting brief, a static PowerPoint/PDF snapshot, the custom skill and a reviewed communication draft. These artifacts have different lifecycles. The dashboard may refresh; the skill defines a method; the presentation records a dated claim set. Link each file accurately and preserve the evidence register so a later reader knows what was reviewed.

Updating one artifact without the others creates inconsistent communication. Reconcile the final pack and explicitly state that actions remain proposed and the email remains a draft. Versioned source and archived superseded artifacts let the team revisit an earlier report without confusing it with the current one. A missing link is UNKNOWN until an actual accessible link is supplied.

**How it works**

- Reconcile final artifacts.
- Record actual filenames and links.
- Review the handoff draft.
- Preserve the dated snapshot and skill.

**Worked example**

- PowerPoint and PDF both show eight slides/pages from the same baseline.
- Outlook does not claim a missing attachment was sent.
- The next update reruns the method with new verified inputs.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Current versions and review evidence are explicit. | A refreshed dashboard is assumed to rewrite an old presentation. |

**Authoritative references**

- https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot
- https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills

---


### Lab 8 · Professional handoff — Refine and Present the Maintenance Decision Deck

Learning outcome: LO4: turn verified dashboard evidence into a professional management presentation.

Goal: Northstar_Management_Final.pptx/PDF, a rehearsal record, final evidence register and unsent Outlook handoff draft with accurate artifact links.

Refine the management deck using the same custom skill and reviewed dashboard evidence. Improve hierarchy, consistency and speaker notes, test the story in a short rehearsal, and prepare a reviewed Outlook handoff draft. The final pack preserves the distinction between a static presentation snapshot, a refreshable dashboard and a manager’s unmade decision.

**What you'll build**

Northstar_Management_Final.pptx/PDF, a rehearsal record, final evidence register and unsent Outlook handoff draft with accurate artifact links.   (Tools: Microsoft 365 Copilot · Excel · Word · PowerPoint · Outlook · OneDrive.)

**Prerequisites**

- Microsoft 365 account with Copilot available in Word, Excel, PowerPoint and Outlook. Availability depends on the assigned licence and tenant settings; confirm access with the trainer before class.
- Desktop Excel on Windows or Mac is recommended; save working copies to your assigned OneDrive course folder with AutoSave on. Do not overwrite the supplied input.
- Download this whole lab folder. All files are synthetic; work-c027 is your own learner output folder.
- Lab 7 management draft, reviewed presentation brief and evidence register.

**Step-by-step**

1. Open your Lab 7 draft and save as Northstar_Management_Final.pptx. Rejoin only if necessary using data/checkpoints/Northstar_Management_Example.pptx and snapshot; review and adapt its supplied example charts and narrative against the verified snapshot. Open the same reviewed brief in the file picker; confirm native skill or label manual practice.
2. Ask the skill to audit before editing. It should report crowded slides, weak evidence, missing labels and inconsistent scope. Review the list yourself against the evidence register; styling changes must never change values.

   ```text
   POWERPOINT COPILOT:
   @maintenance-reporting Audit this eight-slide deck against the selected verified Northstar brief. List inaccurate figures, ambiguous units, date/scope omissions, unsupported causal or approval wording, dense text and weak hierarchy. Propose corrections; do not change values or source facts.
   ```

3. Apply only the reviewed corrections. Keep white/navy/blue with teal highlights, one main message, readable labels, consistent chart formats and source notes. Ask for concise speaker notes; check that notes do not introduce new numbers or promise assignment approvals.

   ```text
   POWERPOINT COPILOT:
   @maintenance-reporting Apply the reviewed design and wording corrections to the existing eight slides. Improve hierarchy and whitespace, make titles claim-led, retain accurate figures and charts, and add 45-second speaker notes per slide. Separate observed findings from proposed actions and end with the decision requested. Preserve the baseline date/scope; do not duplicate slides.
   ```

4. Use Slide Show to inspect at presentation size. Run a five-minute rehearsal with a partner or PowerPoint Rehearse with Coach if available. Ask the partner to identify the reporting date, highest-priority evidence and decision requested. Record one actual change in data/templates/Rehearsal_Log.csv; do not fabricate feedback.

   ```text
   POWERPOINT COPILOT:
   Using only this Northstar Water Services decision deck, propose three rehearsal questions a service operations manager could ask about overdue jobs, technician capacity and proposed priorities. Suggest where the existing evidence supports an answer and where it remains UNKNOWN. Do not invent partner feedback or alter the evidence.
   ```

5. Export File > Export or Save As > PDF. Open the PDF and verify eight pages, readable charts and all visible values. Compare PPTX, PDF, Word brief and dashboard against the evidence register. Keep the source workbook with All filters and the archived refresh-test copy separately.
6. Open Outlook and create a draft to operations.manager@example.invalid. Provide the reviewed brief and the actual OneDrive links to the dashboard/deck. Ask Copilot to draft a handoff email; it may not invent shared links or claim a sent attachment. Keep the email unsent and save a local reviewed TXT copy.

   ```text
   OUTLOOK COPILOT:
   Draft a short Northstar management handoff email using this verified brief and the links I provide. State the 30 September 2026 baseline scope, headline findings, proposed actions and decision required. Explain that the PowerPoint/PDF is a static snapshot while the Excel dashboard is interactive. Leave missing links UNKNOWN. Do not claim approval or send the draft.
   ```

7. Complete data/templates/Final_Handoff_Checklist.csv: workbook source and controls, working filters, sandbox refresh proof, skillv2 installation/manual record, eight-slide PPTX/PDF, reviewed notes, evidence register and unsent draft. Record the exact filenames and your actual checks. Save the final pack in work-c027.

   ```text
   WORD COPILOT:
   Review the final Northstar Water Services handoff evidence I supply: baseline workbook, refresh-test record, skill v2, eight-slide deck and PDF, brief, source register and unsent email draft. Return a completeness checklist with verified evidence and missing items UNKNOWN. Confirm every artifact uses the same baseline date/scope; never claim approval, submission or sending.
   ```


**Sample prompts**

| Purpose | Prompt |
|---|---|
| PowerPoint | @maintenance-reporting Audit and refine the eight-slide deck without changing values. |
| Outlook | Draft the handoff with real supplied links and the static-snapshot limitation. |

**Test it**

| Check | Expected result |
|---|---|
| Presentation integrity | Eight slides and eight PDF pages; visible figures agree with verified register. |
| Professional delivery | Readable chart labels, consistent design, evidence-specific notes and actual rehearsal improvement. |
| Final continuity | Baseline dashboard, brief, deck and unsent draft agree; static snapshot stated. |
| Decision boundary | No real email sent or work order reassigned; proposed actions remain proposed. |

**Checkpoint and rejoin point**

If you fell behind, use data/checkpoints/Northstar_Verified_Checkpoint.xlsx and data/checkpoints/Northstar_Verified_Snapshot.docx. Record checkpoint used in Prompt_Log; then perform this lab, rather than claiming the checkpoint as your output.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot find the source | Use the app file picker to select the actual OneDrive file. A typed local path or a different app chat is not shared context. If needed copy only the verified snapshot into the current app. |
| A total disagrees with Control | Clear dashboard filters to All, check table extent and duplicate IDs, recalculate, then compare definitions and reporting date. Reconcile before continuing. |
| The named feature is missing | Confirm the correct assigned account, English display language and app version. Use the stated manual practice route; record feature unavailable. This is not evidence that a native skill ran. |

**Challenge**

Repeat the task for one different site and explain how the filter scope changes the result. Keep the original verified output.

**Reflection**

Which evidence proves the output is correct, and which decision still needs a person?

> **Note:** The lab folder labs/lab-08-*/ holds the instruction PDF with sample prompts, a data folder with templates, checkpoints and the mock-data workbook (data/Northstar_Work_Orders.xlsx). Northstar Water Services is a fictional water-pipe maintenance and service company. All service hubs, staff and work orders are synthetic. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.

---


### Topic 4 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO4 | Eight-slide evidence story and reviewed handoff. |
| Verify | PDF, notes, register and actual rehearsal agree. |

---


## Next Steps

- First pass: complete every lab yourself, following the steps in each lab file.
- Second pass: redo the labs from memory until the workflow is automatic.
- Apply the techniques to a real process or project in your own organisation.
- Review each lab's detailed steps in this guide and re-run the labs on your own.


## Glossary

- **Grounding** — Supplying accessible evidence for the current request.
- **Backlog** — Selected work with Status neither Closed nor Cancelled.
- **Overdue** — Backlog due strictly before the fixed reporting date.
- **Skill** — Reusable instructions in a matching folder and SKILL.md file.
- **Snapshot** — A dated, scoped copy of verified evidence.
- **Structured reference** — A formula reference to a named Excel table or its columns.
- **Denominator** — The population used to calculate a rate.
- **Proposed assignment** — A suggested owner awaiting a real manager decision.
