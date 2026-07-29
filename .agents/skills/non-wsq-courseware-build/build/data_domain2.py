"""Topic 2 labs for C027: analyse, communicate, coordinate and govern."""

DOMAIN2 = [
    dict(
        num=4,
        topic=2,
        title="Analyse Pilot Readiness and Verify Copilot Formulas in Excel",
        duration=45,
        objective=(
            "LO3: analyse a bounded Excel table, generate formula columns and reconcile every headline "
            "measure to independent controls"
        ),
        goal=(
            "Create a verified readiness workbook with explicit grain, inspectable formulas, control totals and "
            "a short evidence-backed management summary."
        ),
        workflow=["Protect source", "Define measures", "Generate formulas", "Tie out controls", "Write summary"],
        desc=(
            "You will import a 20-row synthetic pilot cohort, preserve the raw source and ask Copilot to create "
            "a priority formula and readiness summary. You will inspect the logic, correct denominator rules and "
            "reconcile counts, rates and averages before writing three decision-relevant observations."
        ),
        build=(
            "work-c027/C027-Asteron-Pilot-Readiness.xlsx with Raw_Cohort, Analysis, Control and Prompt_Log "
            "sheets, a verified priority column and an Approved internal readiness summary, plus "
            "work-c027/C027-Asteron-Verified-Readiness-Summary.txt"
        ),
        services="Excel for Microsoft 365 · Copilot in Excel · asteron-pilot-readiness.csv",
        prerequisites=[
            "Download labs/assets/asteron-pilot-readiness.csv and asteron-excel-controls.md.",
            "Sign in to Excel with Copilot available; record the actual experience label if it differs.",
            "Use the supplied synthetic cohort only and keep the original CSV unchanged.",
        ],
        steps=[
            (
                "Open asteron-pilot-readiness.csv in Excel and save it as "
                "work-c027/C027-Asteron-Pilot-Readiness.xlsx. Rename the first sheet Raw_Cohort. Copy the sheet "
                "to Analysis, format the data as table tblReadiness and create empty Control and Prompt_Log sheets.",
                "Grain: one row = one synthetic pilot participant\n"
                "Key: Participant_ID\n"
                "Raw_Cohort must remain unchanged\n"
                "Working table: tblReadiness",
            ),
            (
                "On Control, enter these metric labels in A2:A10 and exact formulas in B2:B10. State that attendance "
                "rate uses Confirmed registrations as its denominator and counts only Attended as its numerator.",
                "B2 Rows: =ROWS(tblReadiness[Participant_ID])\n"
                "B3 Unique Participant_ID: =COUNTA(UNIQUE(tblReadiness[Participant_ID]))\n"
                "B4 Confirmed: =COUNTIF(tblReadiness[Registration_Status],\"Confirmed\")\n"
                "B5 Attended among Confirmed: =COUNTIFS(tblReadiness[Registration_Status],\"Confirmed\",tblReadiness[Attendance_Status],\"Attended\")\n"
                "B6 Attendance rate: =B5/B4\n"
                "B7 Training complete among Confirmed: =COUNTIFS(tblReadiness[Registration_Status],\"Confirmed\",tblReadiness[Training_Complete],\"Yes\")\n"
                "B8 Training completion rate: =B7/B4\n"
                "B9 Average readiness among Confirmed: =AVERAGEIF(tblReadiness[Registration_Status],\"Confirmed\",tblReadiness[Readiness_Score])\n"
                "B10 Support tickets among Confirmed: =SUMIFS(tblReadiness[Support_Tickets],tblReadiness[Registration_Status],\"Confirmed\")\n"
                "Expected values: 20 | 20 | 16 | 14 | 87.5% | 12 | 75.0% | 80.0625 | 9",
            ),
            (
                "Ask Copilot to add a Priority column using the rule below. Require a formula explanation before "
                "applying it. Inspect the structured references and verify rows P004, P008, P010, P015 and P017. "
                "Non-confirmed rows must be Not in cohort rather than High.",
                "GOAL: Add an editable Priority column to tblReadiness.\n"
                "CONTEXT: Asteron uses the column to plan support for confirmed pilot participants.\n"
                "SOURCE: Use Registration_Status, Training_Complete, Readiness_Score and Support_Tickets in tblReadiness only.\n"
                "EXPECTATIONS: If Registration_Status is not Confirmed, return 'Not in cohort'. Otherwise return 'High' "
                "when Training_Complete is No OR Readiness_Score is below 70 OR Support_Tickets is 2 or more; else 'Standard'. "
                "Explain the formula, then apply it without changing Raw_Cohort.",
            ),
            (
                "Ask Copilot for a summary table of confirmed participants by Department with count, attended count, "
                "training-complete count, average readiness and support tickets. Build an independent PivotTable from "
                "tblReadiness filtered to Confirmed and reconcile every department row—not only the grand total—against "
                "labs/assets/asteron-department-controls.csv. Do not accept a summary whose denominator includes Waitlist "
                "or Withdrawn rows.",
                "Summarise confirmed participants in tblReadiness by Department. Return Count, Attended, "
                "Training_Complete, Average_Readiness and Support_Tickets. Include grand totals and state the filters and denominator.",
            ),
            (
                "Write three observations in a Summary area: one about attendance, one about training completion and one "
                "about high-priority support. Label each OBSERVED and cite the control cells. Add a Limitations line noting "
                "that readiness scores are synthetic and do not prove future performance. Record prompt, formula, checks "
                "and release decision in Prompt_Log. Export the verified headline measures as plain text to "
                "work-c027/C027-Asteron-Verified-Readiness-Summary.txt for the supported Copilot Chat handoff in Lab 7.",
                "Required summary facts:\n"
                "Attendance = 14 of 16 confirmed (87.5%)\n"
                "Training complete = 12 of 16 confirmed (75.0%)\n"
                "High priority = 4 confirmed participants: P004, P008, P010, P015\n"
                "Release state = Approved for internal workflow lab",
            ),
        ],
        test=(
            "Raw_Cohort must match the CSV and tblReadiness must contain 20 rows with 20 unique IDs. Control values "
            "must match asteron-excel-controls.md exactly. Priority must show High only for P004, P008, P010 and P015 "
            "among confirmed participants, and Not in cohort for P017-P020. Every department row and the grand total "
            "must tie to asteron-department-controls.csv, every summary sentence must cite a control cell, and the verified "
            "TXT export must contain the three headline measures."
        ),
        checkpoint=(
            "Save the approved readiness workbook and verified-readiness TXT. Lab 7 uses the supported TXT export for "
            "its three verified headline measures. If any tie-out fails, keep the workbook in REVISE and do not copy its "
            "numbers to another app."
        ),
        troubleshooting=[
            (
                "Copilot uses all 20 rows as the attendance denominator.",
                "Restate the Confirmed filter explicitly and compare the formula with COUNTIF(tblReadiness[Registration_Status],\"Confirmed\").",
            ),
            (
                "Priority marks waitlisted or withdrawn rows High.",
                "Place the Registration_Status condition first so non-confirmed rows return Not in cohort before other tests.",
            ),
            (
                "The average differs from 80.0625.",
                "Check that AVERAGEIF uses Confirmed as the criterion and Readiness_Score as the average range; do not round before reconciliation.",
            ),
        ],
        challenge=(
            "Create a PivotTable of confirmed participants by Department and Preferred_Session. Reconcile the grand "
            "total to 16 and explain why the table supports capacity planning but not employee performance decisions."
        ),
        reflection="Which denominator choice most changed the meaning of a readiness measure, and how did you make it visible?",
    ),
    dict(
        num=5,
        topic=2,
        title="Summarise the Launch Thread and Prepare a Reviewed Outlook Draft",
        duration=35,
        objective=(
            "LO3: summarise a bounded Outlook thread, distinguish confirmed facts from proposals and prepare "
            "a reviewed email draft without creating unsupported commitments"
        ),
        goal=(
            "Produce a fact-checked launch update draft whose recipients, dates, owners, attachments and unresolved "
            "items are explicitly reviewed before any send action."
        ),
        workflow=["Create thread", "Summarise facts", "Compare messages", "Draft response", "Keep in Draft"],
        desc=(
            "You will create a private synthetic email thread in your own mailbox from the supplied messages, use "
            "Copilot to summarise decisions and open questions, then draft a concise internal update. You will verify "
            "the thread facts and leave the message unsent for the cross-app review."
        ),
        build=(
            "An Outlook draft titled [DRAFT] Asteron pilot launch update - review required, plus "
            "work-c027/C027-Outlook-Thread-Review.md with the verified facts and release checklist"
        ),
        services="Outlook for Microsoft 365 · Copilot in Outlook · asteron-email-thread.md",
        prerequisites=[
            "Use only your own training mailbox or a trainer-approved sandbox mailbox.",
            "Open labs/assets/asteron-email-thread.md and asteron-outlook-review-template.md.",
            "Copy asteron-outlook-review-template.md to work-c027/C027-Outlook-Thread-Review.md before writing into it.",
            "Do not send the final update; the required outcome is a reviewed draft.",
        ],
        steps=[
            (
                "Create the synthetic thread in your own mailbox. Send Message 1 from asteron-email-thread.md to "
                "yourself with subject Asteron pilot launch coordination - synthetic. Paste each supplied message in full, "
                "including its synthetic From and Date labels inside the message body. Reply to the same thread with "
                "Messages 2 and 3, still addressed only to yourself. Confirm the three messages appear as one thread. "
                "For project history, the embedded synthetic labels govern; your real self-send transport metadata records "
                "only when the exercise copy was created.",
                "Safety boundary:\n"
                "Recipient = your own training address only\n"
                "Subject contains 'synthetic'\n"
                "No real client, colleague or external address\n"
                "Use only the supplied message text",
            ),
            (
                "Use Summary by Copilot or Copilot Chat in Outlook on the thread. Ask for confirmed decisions, "
                "current owners and due dates, superseded information, proposals and open questions in separate sections. "
                "Copy the result into work-c027/C027-Outlook-Thread-Review.md.",
                "Summarise this synthetic thread as Confirmed decisions | Owners and current due dates | Superseded "
                "information | Proposals | Open questions. Use ISO dates and quote the message date for each item. "
                "Do not convert a proposal or pending approval into a commitment.",
            ),
            (
                "Compare the summary with all three messages. Correct the data-export due date to 2026-08-13, keep "
                "the 2026-08-19 support clinic and room as proposed, and retain the privacy sign-off dependency before "
                "any external announcement. Record VERIFIED, REVISE or HOLD beside every item.",
                "Expected distinctions:\n"
                "FAQ / Nisha Rao / 2026-08-11 = confirmed\n"
                "Data export / Leon Wu / 2026-08-13 = current; 2026-08-12 superseded\n"
                "Support clinic / 2026-08-19 14:00 = proposed; room pending\n"
                "External announcement = HOLD until privacy sign-off",
            ),
            (
                "Use Draft with Copilot to create an internal response. Address it only to yourself, prefix the subject "
                "with [DRAFT], and require sections for Confirmed, Needs confirmation and Actions. Use coaching to review "
                "clarity and tone, but reject any suggestion that changes a fact or commitment.",
                "Draft a concise internal launch update from this verified thread. Separate Confirmed, Needs confirmation "
                "and Actions. Preserve current owners and ISO dates. Ask for room confirmation; do not announce externally. "
                "Professional, neutral tone, under 180 words. Keep the message in Draft.",
            ),
            (
                "Complete the Outlook release checklist in C027-Outlook-Thread-Review.md: To, Cc, subject, facts, "
                "commitments, attachments, links, sensitivity, tone and send decision. Save the draft without sending it. "
                "Set the release state to HOLD - pending Lab 7 cross-app consistency review.",
                "Required send decision: DO NOT SEND\n"
                "Required state: HOLD - cross-app review pending\n"
                "Attachments: none\n"
                "Recipients: self only",
            ),
        ],
        test=(
            "The mailbox must contain a three-message synthetic self-thread and one unsent draft. The review file must "
            "exist in work-c027, state that embedded synthetic sender/date labels govern project history, show 2026-08-13 "
            "as the current export date, keep the support clinic proposed and hold external announcement "
            "until privacy sign-off. The final draft must be under 180 words, addressed only to self, contain no attachment "
            "and remain HOLD - cross-app review pending."
        ),
        checkpoint=(
            "Leave the email in Draft and save C027-Outlook-Thread-Review.md. Lab 7 compares this draft with the Word "
            "brief, PowerPoint deck, Excel workbook and Teams action register."
        ),
        troubleshooting=[
            (
                "Outlook does not group the three messages.",
                "Use Reply on the first self-message for Messages 2 and 3 and keep the subject unchanged.",
            ),
            (
                "Summary by Copilot is unavailable.",
                "Use Copilot Chat in Outlook with the selected synthetic thread if supported. Otherwise use Copilot Chat "
                "with asteron-email-thread.md and record that the Outlook summary capability was unavailable.",
            ),
            (
                "Coaching recommends stronger commitment language.",
                "Keep the verified status. Tone advice never overrides evidence or approval state.",
            ),
        ],
        challenge=(
            "Create a second version for an executive reader in no more than 90 words. Compare which details can be "
            "removed without hiding an owner, due date, dependency or unresolved decision."
        ),
        reflection="Why must thread extraction and reply drafting be reviewed as two separate stages?",
    ),
    dict(
        num=6,
        topic=2,
        title="Validate a Teams Recap and Create the Action Register",
        duration=35,
        objective=(
            "LO4: validate a Teams recap against transcript evidence and convert confirmed follow-up work "
            "into an action register with owners, due dates and release status"
        ),
        goal=(
            "Create a transcript-backed action register that distinguishes decisions, actions, proposals and open questions."
        ),
        workflow=["Open recap", "Extract categories", "Trace evidence", "Correct actions", "Release register"],
        desc=(
            "You will use a trainer-provided synthetic Teams meeting recap or the supplied transcript in Copilot Chat "
            "inside Teams. You will compare generated decisions and actions with the evidence, correct attribution and "
            "dates, and create a durable action register for the cross-app workflow."
        ),
        build=(
            "work-c027/C027-Teams-Action-Register.xlsx with Decisions, Actions, Proposals and Open_Questions sheets, "
            "transcript references and a Reviewed internal coordination state, plus "
            "work-c027/C027-Asteron-Verified-Actions.txt"
        ),
        services="Microsoft Teams · Copilot or intelligent recap · asteron-teams-transcript.md · Excel",
        prerequisites=[
            "Use the trainer-provided Asteron synthetic meeting if available; follow organisational policy for transcription.",
            "If a live recap is unavailable, open asteron-teams-transcript.md in Copilot Chat within Teams and record the fallback.",
            "Open labs/assets/asteron-action-register-template.csv and asteron-teams-register-schemas.md.",
        ],
        steps=[
            (
                "Open the trainer-provided Asteron launch stand-up in Teams and select Recap and Copilot when available. "
                "If no permitted recap exists, upload or reference asteron-teams-transcript.md in Copilot Chat inside Teams. "
                "Record which path you used and the source date.",
                "Evidence path:\n"
                "A = Teams recap from permitted synthetic meeting\n"
                "B = Supplied synthetic transcript in Copilot Chat inside Teams\n"
                "Never claim A when you used B",
            ),
            (
                "Ask Copilot to return four separate sections: Decisions, Actions, Proposals and Open questions. "
                "For Actions require Owner, Deliverable, Due_Date and Transcript_Evidence. Do not ask for a blended summary.",
                "Using only this meeting evidence, return Decisions | Actions | Proposals | Open questions. For each action "
                "give one named owner, one deliverable, one ISO due date and the exact transcript line or timestamp. "
                "Do not infer ownership or dates.",
            ),
            (
                "Open the transcript and verify every generated row. Correct the privacy sign-off owner, distinguish "
                "the proposed support clinic from confirmed launch work, and keep the room question open. Mark any row "
                "without exact evidence HOLD.",
                "Required evidence:\n"
                "Nisha Rao - FAQ - 2026-08-11\n"
                "Leon Wu - data export - 2026-08-13\n"
                "Priya Menon - readiness dashboard - 2026-08-14 12:00\n"
                "Farah Lim - privacy sign-off - 2026-08-15\n"
                "Mei Tan - confirm support-clinic room - 2026-08-12\n"
                "Pilot launch remains 2026-08-18 subject to privacy sign-off",
            ),
            (
                "Open asteron-action-register-template.csv in Excel and save as C027-Teams-Action-Register.xlsx. "
                "Create tables tblDecisions, tblActions, tblProposals and tblOpenQuestions on the four separate sheets "
                "specified in asteron-teams-register-schemas.md. Copy only verified rows, retain the evidence reference "
                "and set Status to Confirmed, Proposed or Open.",
                "Decisions: Decision_ID | Decision | Evidence | Status | Reviewer | Release_State\n"
                "Actions: Action_ID | Deliverable | Owner | Due_Date | Evidence | Status | Reviewer | Release_State\n"
                "Proposals: Proposal_ID | Proposal | Proposed_By | Target_Date | Evidence | Resolution_Owner | Status\n"
                "Open Questions: Question_ID | Question | Resolution_Owner | Due_Date | Evidence | Status",
            ),
            (
                "Run a completeness check: every Confirmed action has one owner, one deliverable, one due date and evidence; "
                "Proposed items are not in the confirmed count; Open questions have an owner for resolution. Record reviewer, "
                "review date and state Reviewed for internal coordination. Export the confirmed action rows with owner, "
                "deliverable, due date and evidence to work-c027/C027-Asteron-Verified-Actions.txt for Lab 7.",
                "Expected confirmed work items = 5\n"
                "Expected unresolved item = support-clinic room availability\n"
                "Release state = Reviewed for internal coordination",
            ),
        ],
        test=(
            "The register must contain all four required sheets/tables, the five required work items with exact owners and "
            "dates, plus one proposed clinic and one open room question. Every confirmed action must include transcript evidence, and the "
            "file must record whether the source was a Teams recap or the supplied transcript fallback. The release state must "
            "be Reviewed for internal coordination, and the verified-actions TXT export must contain only confirmed actions."
        ),
        checkpoint=(
            "Save the action register and verified-actions TXT in work-c027. Lab 7 uses the supported TXT export plus "
            "the open question. Do not remove the evidence column when copying information into another app."
        ),
        troubleshooting=[
            (
                "The recap assigns an action to the wrong speaker.",
                "Use the transcript speaker label and surrounding lines; correct the owner and record the generated attribution as REVISE.",
            ),
            (
                "A due date is missing from the evidence.",
                "Set the action to HOLD and create an open question for the owner instead of inventing a date.",
            ),
            (
                "The live meeting cannot be transcribed.",
                "Use the supplied synthetic transcript inside Teams and record the fallback. Do not change tenant policy or record without permission.",
            ),
        ],
        challenge=(
            "Ask Copilot to identify two risks implied by the action register. Label them HYPOTHESIS and state which "
            "additional evidence would be required before they could become confirmed risks."
        ),
        reflection="Which recap error would have caused the greatest coordination cost if it had entered the action register?",
    ),
    dict(
        num=7,
        topic=2,
        title="Assemble and Reconcile the Cross-App Coordination Pack",
        duration=45,
        objective=(
            "LO4: connect approved outputs across Microsoft 365 apps using handoff contracts and reconcile "
            "repeated facts, owners, measures and release states"
        ),
        goal=(
            "Create a cross-app manifest and concise coordination pack in which every repeated fact agrees with the "
            "governing artifact."
        ),
        workflow=["Register artifacts", "Declare authority", "Draft pack", "Reconcile facts", "Approve handoffs"],
        desc=(
            "You will register the Chat, Word, PowerPoint, Excel, Outlook and Teams outputs, declare which artifact "
            "governs each type of information, then use Copilot to draft a coordination update. A consistency matrix "
            "will expose any date, owner, number or status that drifted during an app handoff."
        ),
        build=(
            "work-c027/C027-Asteron-Cross-App-Manifest.xlsx and C027-Asteron-Coordination-Pack.docx "
            "with authoritative-source links, a consistency matrix and an Approved internal handoff state"
        ),
        services="Microsoft 365 Copilot Chat · Word · Excel · PowerPoint · Outlook · Teams",
        prerequisites=[
            "Labs 1-6 outputs are saved in work-c027 with their stated release records; if one is unavailable, use "
            "the versioned trainer-validated labs/assets/asteron-capstone-rejoin-pack.txt and record the substitution.",
            "Do not use an artifact that remains REVISE; HOLD artifacts can be registered but cannot govern released facts.",
            "Open the partially populated asteron-cross-app-manifest-template.csv and asteron-consistency-matrix-template.csv.",
        ],
        steps=[
            (
                "Open asteron-cross-app-manifest-template.csv in Excel and save as C027-Asteron-Cross-App-Manifest.xlsx. "
                "Enter one row for the source register, Word brief, PowerPoint deck, Excel readiness workbook, Outlook review "
                "and draft, and Teams action register. Record file link, version, owner, purpose, source authority, state and "
                "next use. Complete Source_Coverage as Learner-created checkpoint or Trainer-validated practice fallback. "
                "Timebox: 5 minutes; fill placeholders in the six pre-populated rows rather than rebuilding the table.",
                "Required artifacts = 6\n"
                "Allowed states = Draft | Reviewed | Approved | Hold\n"
                "No blank owner, purpose or next use\n"
                "Outlook draft remains Hold",
            ),
            (
                "Create an Authority sheet. Declare that the source register governs confirmed launch facts, the Word brief "
                "governs the narrative, Excel governs cohort measures, Teams governs meeting actions and the Outlook thread "
                "governs email history. PowerPoint may communicate facts but does not replace its sources. Timebox: 5 minutes.",
                "Authority map:\n"
                "Launch facts -> Source register\n"
                "Narrative -> Approved Word brief\n"
                "Readiness measures -> Verified Excel workbook\n"
                "Meeting actions -> Teams action register\n"
                "Email history -> Outlook thread review",
            ),
            (
                "In Microsoft 365 Copilot Chat, reference the approved Word brief, "
                "C027-Asteron-Verified-Readiness-Summary.txt and C027-Asteron-Verified-Actions.txt. If any normal input "
                "is missing, reference asteron-capstone-rejoin-pack.txt instead and name only the applicable WORD BRIEF, "
                "EXCEL READINESS or TEAMS substitute section. Ask for the bounded "
                "draft below; review it, then paste the accepted text into C027-Asteron-Coordination-Pack.docx with sections "
                "Executive position, Readiness, Confirmed actions, Open questions and Artifact links. Do not ask Copilot in "
                "Word to read Excel workbooks, and do not use the held Outlook draft as a factual source. Timebox: 12 minutes.",
                "GOAL: Draft a two-page internal coordination update.\n"
                "CONTEXT: Asteron department heads need the launch position, readiness measures, actions and open questions.\n"
                "SOURCE: Use the approved Word brief and the two referenced verified TXT exports only.\n"
                "EXPECTATIONS: Preserve ISO dates and owners; cite the governing artifact after every section; distinguish "
                "Confirmed, Proposed and Open; include 14/16 attendance, 12/16 training completion and four high-priority participants.",
            ),
            (
                "Copy the nine pre-populated rows from asteron-consistency-matrix-template.csv into a Consistency sheet. "
                "Fill only the applicable artifact cells and compare the source register, Word brief, deck, Excel workbook, "
                "Outlook review, Teams register and coordination pack. Use N/A where a fact does not belong. Timebox: 15 minutes.",
                "Required consistency rows:\n"
                "Launch 2026-08-18 | Cohort 20 / five departments\n"
                "FAQ Nisha Rao / 2026-08-11 | Export Leon Wu / 2026-08-13\n"
                "Privacy sign-off before external announcement | Clinic proposed / room open\n"
                "Attendance 14/16 (87.5%) | Training 12/16 (75.0%) | High priority 4",
            ),
            (
                "Correct every mismatch in the downstream artifact, not in the governing source. Update the manifest with "
                "the reviewed version and state. In the coordination pack add a release table with Source coverage, Fact "
                "consistency, Permissions, Audience, Owner and Decision. Set the pack to Approved internal handoff only when "
                "all consistency rows agree. Timebox: 8 minutes.",
                "Final conditions:\n"
                "Consistency_Result = MATCH for every required row\n"
                "Coordination pack = Approved internal handoff\n"
                "Outlook draft = Hold until Lab 8 release review\n"
                "No artifact is marked Approved without a named reviewer",
            ),
        ],
        test=(
            "The manifest must contain six artifact rows with links, owners, versions and states. The authority map must "
            "name one governing artifact for each information type. Every required consistency row must show MATCH across "
            "all artifacts where the fact appears. The coordination pack must be no more than two pages, cite its source "
            "artifacts and be Approved internal handoff; the Outlook draft must remain Hold. Any substituted prior output "
            "must be visibly marked REJOIN-PACK-v1.0 and Trainer-validated practice fallback."
        ),
        checkpoint=(
            "Save the manifest and coordination pack. Lab 8 applies the final responsible-use and privacy review before "
            "the workflow is considered ready for controlled internal use. If an earlier artifact is missing or still "
            "blocked, copy the relevant section from asteron-capstone-rejoin-pack.txt, set its manifest Link to "
            "REJOIN-PACK-v1.0, record Trainer-validated practice fallback as coverage and continue; replace it later when "
            "the learner-created artifact passes its checkpoint."
        ),
        troubleshooting=[
            (
                "A downstream artifact contains an older date.",
                "Confirm the governing source, correct the downstream file, update its version and rerun the consistency row.",
            ),
            (
                "Copilot cannot reference all three source files at once.",
                "Draft one section per supported Word/TXT reference in Microsoft 365 Copilot Chat, then assemble and "
                "reconcile manually. Record actual source coverage; never imply an Excel workbook was read when it was not.",
            ),
            (
                "Two files appear to govern the same fact.",
                "Choose the artifact closest to the approved source of that information and record the decision in the Authority sheet.",
            ),
        ],
        challenge=(
            "Draw a simple lineage diagram from source register and raw cohort through each downstream artifact. Mark "
            "where an error could propagate to three or more outputs and add one preventive check at that handoff."
        ),
        reflection="Which handoff carried the greatest risk of multiplying an early error, and which checkpoint contained it?",
    ),
    dict(
        num=8,
        topic=2,
        title="Run the Responsible-Use and Privacy Release Gate",
        duration=45,
        objective=(
            "LO4: apply permission, minimisation, accuracy, sensitivity, transparency and accountability "
            "controls to the complete Copilot-assisted workflow"
        ),
        goal=(
            "Produce a final release log that identifies unsafe sharing, records remediation and assigns a human "
            "decision to every artifact."
        ),
        workflow=["Inspect permissions", "Minimise data", "Review risks", "Remediate gaps", "Record decision"],
        desc=(
            "You will inspect a simulated sharing and sensitivity scenario for every Asteron artifact, identify an "
            "overbroad readiness-data link, minimise copied personal detail and complete the C027 release gate. The default "
            "path is a tabletop review; an actual permission change is permitted only in a trainer-authorised sandbox. The "
            "exercise ends with simulation-only, Revise or Hold decisions and named owners."
        ),
        build=(
            "work-c027/C027-Asteron-Responsible-Use-Release-Log.docx with artifact-level permission, data, "
            "accuracy, audience, transparency, reviewer and release decisions"
        ),
        services="Microsoft 365 · OneDrive or SharePoint sharing controls · Copilot · asteron-sharing-simulation.md",
        prerequisites=[
            "Labs 1-7 artifacts and cross-app manifest are complete.",
            "Open labs/assets/asteron-sharing-simulation.md and asteron-release-gate-template.md.",
            "Treat every person and access setting in the simulation as synthetic; never inspect or modify real group "
            "membership unless the trainer explicitly authorises the sandbox path.",
        ],
        steps=[
            (
                "Create a blank Word document, copy the headings and tables from asteron-release-gate-template.md into it, "
                "and save it as work-c027/C027-Asteron-Responsible-Use-Release-Log.docx. Add one row for each of the six "
                "manifest artifacts plus the coordination pack. Record intended audience, simulated current "
                "access, minimum necessary data, governing source, reviewer and current state. Record Exercise path = "
                "Tabletop by default, or Trainer-authorised sandbox only when the trainer has explicitly approved it.",
                "Required artifacts = 7\n"
                "Checks = Purpose | Access | Minimisation | Accuracy | Sensitivity | Transparency | Reviewer | Decision",
            ),
            (
                "Compare the simulated current access with the intended audience. Identify the readiness workbook's "
                "organisation-wide link as overbroad and the participant contact list as unnecessary for the coordination "
                "pack. Set affected artifacts to HOLD before proposing remediation.",
                "Required findings:\n"
                "Readiness workbook: intended pilot team; current anyone-in-organisation link -> HOLD\n"
                "Contact list: not required for stated purpose -> exclude\n"
                "Outlook draft: self only and unsent -> HOLD until recipient review\n"
                "Coordination pack: department heads group -> request owner verification",
            ),
            (
                "Write the remediation plan. On the default tabletop path, record the requested restriction, authorised "
                "owner and missing evidence; do not change a permission or inspect group membership. Remove unnecessary "
                "synthetic participant contact fields from your downstream lab copies, request department-heads membership "
                "verification from the owner and keep the external announcement blocked until privacy sign-off. Only on an "
                "explicitly trainer-authorised sandbox path may you perform and verify the actual permission change on the "
                "supplied lab copy.",
                "Remediation evidence to record:\n"
                "Exercise path and trainer authority, if any\n"
                "Requested control or actual sandbox change\n"
                "Owner\n"
                "Completion date\n"
                "Before audience\n"
                "After audience\n"
                "Evidence gap or verification method",
            ),
            (
                "Run the C027 release gate on the coordination pack and Outlook draft. Check Source, Accuracy, Sensitivity, "
                "Quality, Consistency and Accountability. In Microsoft 365 Copilot Chat, reference the completed "
                "C027-Asteron-Responsible-Use-Release-Log.docx and ask for the critique below. If file reference is "
                "unavailable, paste the completed rows into Chat or apply the same checklist manually and record the fallback. "
                "Make the final decision yourself and record any generated suggestion as a proposal.",
                "Review this release log for blank evidence, inconsistent states, overbroad audiences, unsupported claims "
                "and missing owners. Return findings only; do not change permissions, send messages or approve artifacts.",
            ),
            (
                "Record final states. On the tabletop path, the coordination pack may become Approved in simulation only "
                "after the requested control, owner and evidence gap are recorded; otherwise keep it HOLD. On a trainer-"
                "authorised sandbox path, it may become Approved for controlled sandbox use only after actual evidence is "
                "verified. Neither state approves a real organisational release. The Outlook draft may become Reviewed but "
                "remains unsent. Add a transparency note describing meaningful Copilot assistance, sources reviewed, "
                "limitations and the named human release owner.",
                "Tabletop: Pack = Approved in simulation only, or HOLD when a gate remains unresolved.\n"
                "Authorised sandbox: Pack = Approved for controlled sandbox use only after verified evidence.\n"
                "Outlook = Reviewed draft, unsent; external announcement = HOLD until privacy sign-off.\n"
                "Real organisational release = not granted; release owner = <LEARNER NAME>.",
            ),
        ],
        test=(
            "The release log must contain seven artifact rows and no blank reviewer or decision. It must identify the "
            "overbroad readiness link, exclude the unnecessary contact list, record the group-verification request or "
            "trainer-authorised sandbox evidence, keep the Outlook message unsent and hold the external announcement pending "
            "privacy sign-off. The coordination pack may be Approved in simulation only on the tabletop path or Approved "
            "for controlled sandbox use only on an authorised sandbox path after the required evidence is recorded. Real "
            "organisational release must remain unapproved, and the log must include a meaningful-AI-assistance note."
        ),
        checkpoint=(
            "Save the responsible-use release log with the complete work-c027 folder. The package is the final C027 "
            "practice checkpoint and can be repeated with another authorised workflow after class. Preserve the exercise "
            "path and the statement that no real organisational release was granted."
        ),
        troubleshooting=[
            (
                "You cannot change a simulated sharing setting in your environment.",
                "Stay on the tabletop path. Do not seek extra access. Record the current setting, required owner, remediation "
                "request and evidence gap; use Approved in simulation only only when the simulation gate is complete, otherwise HOLD.",
            ),
            (
                "Copilot's critique recommends approval without evidence.",
                "Reject the recommendation. Only the named human reviewer can release an artifact after all gate evidence is complete.",
            ),
            (
                "An artifact contains more personal detail than its purpose requires.",
                "Remove or aggregate the unnecessary fields in the downstream copy, retain the governed source separately and rerun the accuracy check.",
            ),
        ],
        challenge=(
            "Create a reusable one-page release card for your own role with the six C027 gate dimensions and one "
            "escalation trigger for each. Keep the card independent of any specific Copilot interface label."
        ),
        reflection="Which control depended on organisational governance rather than prompt quality, and who owns that control?",
    ),
]
