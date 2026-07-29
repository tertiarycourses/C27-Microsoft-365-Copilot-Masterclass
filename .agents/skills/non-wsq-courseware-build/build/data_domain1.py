"""Topic 1 labs for C027: ground, prompt, write and present."""

DOMAIN1 = [
    dict(
        num=1,
        topic=1,
        title="Research the Asteron Launch and Build a Verified Source Register",
        duration=35,
        objective=(
            "LO1: use G-C-S-E to research a bounded source pack in Copilot Chat, trace material "
            "claims to evidence and record unresolved questions"
        ),
        goal=(
            "Create a source register and verified claim ledger that can safely govern the Word brief "
            "and every later Asteron artifact."
        ),
        workflow=["Inspect sources", "Write G-C-S-E", "Generate ledger", "Trace claims", "Release checkpoint"],
        desc=(
            "You will inspect three synthetic Asteron source files, register their purpose and status, "
            "then ask Copilot Chat to synthesise the launch facts. You will open the sources, verify dates, "
            "owners, decisions and open questions, and keep unsupported statements out of the approved ledger."
        ),
        build=(
            "work-c027/C027-Asteron-Source-Register.xlsx with Sources, Claim_Ledger and Review_Log tables, plus "
            "work-c027/C027-Asteron-Verified-Claims.txt and a Reviewed release record"
        ),
        services=(
            "Microsoft 365 Copilot Chat · Excel · asteron-project-brief.md · "
            "asteron-decision-log.csv · asteron-stakeholder-notes.md"
        ),
        prerequisites=[
            "Download the repository and keep every file in labs/assets together.",
            "Sign in to an eligible Microsoft 365 account and open Copilot Chat.",
            "Create work-c027 in an approved OneDrive location; use only the supplied synthetic Asteron sources.",
        ],
        steps=[
            (
                "Open labs/assets/asteron-project-brief.md, asteron-decision-log.csv and "
                "asteron-stakeholder-notes.md. For each file, note its title, owner, effective date, purpose, "
                "governing facts and limitations. Do not ask Copilot to summarise the files yet.",
                "Required pre-read questions:\n"
                "1. Which source governs the launch date?\n"
                "2. Which source governs named decisions and owners?\n"
                "3. Which notes are observations rather than approved decisions?\n"
                "4. Which question remains unresolved?",
            ),
            (
                "Open labs/assets/asteron-source-register-template.csv in Excel and save it as "
                "work-c027/C027-Asteron-Source-Register.xlsx. Rename the first sheet Sources, format the data "
                "as table tblSources and enter one row per source. Add a second sheet named Claim_Ledger and "
                "copy in the headers from asteron-claim-ledger-template.csv as table tblClaims. Add a third sheet "
                "named Review_Log and copy asteron-review-log-template.csv as table tblReviewLog.",
                "Required tables:\n"
                "tblSources: Source_ID | File | Owner | Effective_Date | Purpose | Governs | Limitation | Status\n"
                "tblClaims: Claim_ID | Claim | Source_ID | Evidence | Confidence | Check | Reviewer_Note | Release_State\n"
                "tblReviewLog: Artifact | Prompt | Sources_Used | Source_Coverage | Reviewer | Review_Date | Open_Question | Release_State | Next_Use",
            ),
            (
                "Attach or reference only the three files in the permitted source pack in Copilot Chat. Submit the G-C-S-E "
                "prompt below. If your experience cannot reference all three files, process one file at a time and "
                "record that limitation in Sources; do not imply that an unavailable source was used. Preserve each "
                "source's true authority and status; stakeholder notes remain working observations, not decisions.",
                "GOAL: Build a claim ledger for the Asteron client portal pilot launch.\n"
                "CONTEXT: Department heads need confirmed dates, owners, decisions, dependencies and open questions.\n"
                "SOURCE: Use only the attached project brief, decision log and stakeholder notes. Name the Source_ID for every row.\n"
                "EXPECTATIONS: Return Claim_ID | Claim | Source_ID | Evidence | Confidence | Check. Use ISO dates. "
                "Do not turn a proposal into a decision. Mark contradictions and missing evidence as HOLD. Do not add web facts.",
            ),
            (
                "Copy the proposed rows into tblClaims. Open the governing source for each material date, number, "
                "owner and decision. Set Check to VERIFIED only when the source supports the statement. Use REVISE "
                "for a correctable wording issue and HOLD for an unresolved or unsupported statement.",
                "Material checks:\n"
                "Launch date = 2026-08-18\n"
                "Pilot scope = 20 internal participants across five departments\n"
                "FAQ owner = Nisha Rao, due 2026-08-11\n"
                "Data export owner = Leon Wu, current due date 2026-08-13\n"
                "External announcement = not released before privacy sign-off\n"
                "Support clinic date and room = proposed, not confirmed",
            ),
            (
                "Complete one row in tblReviewLog with the exact prompt, sources actually used, coverage, reviewer "
                "name, review date, remaining open question, release state and next use. Export only VERIFIED claim "
                "rows as plain text to work-c027/C027-Asteron-Verified-Claims.txt, including Claim_ID, Claim, Source_ID "
                "and Evidence. A source-supported claim may be explicitly labelled Confirmed, Proposed or Open; exclude "
                "all unsupported HOLD rows. Save the workbook and link both outputs in your work-c027 notes.",
                "Release record:\n"
                "Artifact: C027-Asteron-Source-Register.xlsx\n"
                "State: Reviewed\n"
                "Open question: Is the 2026-08-19 support clinic room confirmed?\n"
                "Next use: governing source for Lab 2 Word brief",
            ),
        ],
        test=(
            "tblSources must contain exactly three permitted sources with their true authority/status and no web source. "
            "tblClaims must include the "
            "six material checks with Source_ID and evidence. The 2026-08-13 data-export date must supersede "
            "2026-08-12, and the support clinic must remain proposed. Every unsupported statement must be REVISE "
            "or HOLD. tblReviewLog must contain every required review field, and the TXT export must contain only "
            "VERIFIED claims, including source-supported Proposed/Open items with those labels and no unsupported HOLD "
            "rows. The final release state must be Reviewed, not Approved, because one room question remains open."
        ),
        checkpoint=(
            "Save the source register and verified-claims TXT in work-c027. Lab 2 references the supported TXT export "
            "and preserves the open support-clinic question. If you need to rejoin, use labs/assets/asteron-expected-facts.md "
            "to rebuild the ledger and TXT export."
        ),
        troubleshooting=[
            (
                "Copilot cannot reference one or more local files.",
                "Save the files to an approved OneDrive location or process them one at a time. Record the actual source "
                "coverage and merge the ledgers manually; never claim a missing file was reviewed.",
            ),
            (
                "A generated claim has no traceable source.",
                "Set Release_State to HOLD, add 'No governing evidence found' and exclude the claim from the Word brief.",
            ),
            (
                "Copilot treats the earlier 2026-08-12 export date as current.",
                "Open the decision log, use the latest dated decision and record 2026-08-13 as current while noting the superseded date.",
            ),
        ],
        challenge=(
            "Ask Copilot to return a contradiction matrix by Source_ID. Verify it manually and explain why the latest "
            "dated statement is not automatically authoritative unless the source is allowed to govern that fact."
        ),
        reflection="Which prompt element made it easiest to detect an unsupported or superseded claim, and why?",
    ),
    dict(
        num=2,
        topic=1,
        title="Draft and Approve the Asteron Launch Brief in Word",
        duration=40,
        objective=(
            "LO2: draft a source-grounded business document in Word, apply a bounded rewrite and validate "
            "the final version against the source register and audience brief"
        ),
        goal=(
            "Produce an approved launch brief of no more than two pages whose facts, open questions and call to action agree with "
            "the verified source register."
        ),
        workflow=["Create brief", "Ground draft", "Trace facts", "Rewrite one passage", "Approve version"],
        desc=(
            "You will create a Word document for Asteron department heads, use the supported verified-claims TXT "
            "export as the Copilot reference, then review the generated draft against the source register and project "
            "brief line by line. You will use Copilot to "
            "rewrite one selected passage without changing scope, commitments or unresolved items."
        ),
        build=(
            "work-c027/C027-Asteron-Launch-Brief-v1.0.docx with five required sections, source notes, an "
            "Open Questions box and an Approved for deck handoff record"
        ),
        services="Word for Microsoft 365 · Copilot in Word · C027-Asteron-Verified-Claims.txt · C027-Asteron-Source-Register.xlsx",
        prerequisites=[
            "Completed Lab 1 workbook and C027-Asteron-Verified-Claims.txt export.",
            "Open labs/assets/asteron-word-brief-spec.md and labs/assets/asteron-style-guide.md.",
            "Keep the support-clinic room as an open question; no source approves it.",
            "For this simulation, the learner is the document owner and supplies the owner review; trainer feedback may supplement it.",
        ],
        steps=[
            (
                "Create a blank Word document in work-c027 and save it as C027-Asteron-Launch-Brief-v1.0.docx. "
                "Add a title, document owner, version, date and a status line set to Draft. Insert the five required "
                "headings from the brief specification before generating any body text.",
                "Required headings:\n"
                "1. Purpose and Audience\n"
                "2. Confirmed Launch Position\n"
                "3. Readiness and Dependencies\n"
                "4. Decisions and Owners\n"
                "5. Open Questions and Next Actions",
            ),
            (
                "Open Copilot in Word and reference C027-Asteron-Verified-Claims.txt from Lab 1. Submit the prompt below. "
                "Word's referenced drafting accepts this supported TXT handoff; do not cite the Excel workbook as if "
                "Copilot in Word read it. Use the workbook and project brief for the manual source review in Step 3.",
                "GOAL: Draft an Asteron client portal pilot launch brief of no more than two pages.\n"
                "CONTEXT: Department heads need the confirmed position, named owners and decisions needed before 2026-08-18.\n"
                "SOURCE: Use only the referenced C027-Asteron-Verified-Claims.txt export. Preserve items explicitly "
                "labelled Proposed or Open; the export contains no unsupported HOLD rows.\n"
                "EXPECTATIONS: Use the five existing headings, concise professional language, bullets for owners, ISO dates, "
                "and source notes in [Source_ID] form. Do not add market claims or present proposals as confirmed.",
            ),
            (
                "Review the draft against the source register. Highlight every date, number, owner and commitment. "
                "Add a Word comment containing the governing Source_ID, then set the review decision to Keep, Change "
                "or Remove. Correct any unsupported language before continuing.",
                "Required trace points:\n"
                "2026-08-18 launch date\n"
                "20 internal participants\n"
                "five departments\n"
                "Nisha Rao / FAQ / 2026-08-11\n"
                "Leon Wu / export / 2026-08-13\n"
                "privacy sign-off before external announcement",
            ),
            (
                "Select the Readiness and Dependencies section only. Ask Copilot to make it more concise for senior "
                "leaders while preserving every fact and the distinction between confirmed and proposed. Compare the "
                "before and after text and reject any change to scope, date, owner or status.",
                "Rewrite this selected section to no more than 90 words for department heads. Preserve all dates, owners, "
                "scope and status labels exactly. Keep the support clinic room as an open question. Do not introduce new commitments.",
            ),
            (
                "Insert a two-column release table at the end with Check and Result. Complete Source fidelity, Audience "
                "fit, Scope, Open questions, Privacy, Accessibility and Owner approval. As the lab document owner, enter "
                "your name and review date for Owner approval. Change the document status to Approved for deck handoff "
                "only when all required checks are complete; this is a simulated workflow state, not organisational approval. "
                "Save and close the file.",
                "Release states:\n"
                "APPROVED = evidence and audience checks complete\n"
                "REVISE = correctable content or format gap\n"
                "HOLD = unsupported fact, unsafe disclosure or unresolved release decision",
            ),
        ],
        test=(
            "The Word file must contain exactly the five required headings and remain within two pages including the "
            "release table. Every material date, number, owner and commitment must trace to a Source_ID. The launch date "
            "must be 2026-08-18, the data export 2026-08-13 and the support-clinic room must remain open. The title block "
            "must show v1.0 and Approved for deck handoff."
        ),
        checkpoint=(
            "Save the approved Word brief in work-c027. Lab 3 uses this exact version as the governing PowerPoint source. "
            "If the status is REVISE or HOLD, correct the document before continuing."
        ),
        troubleshooting=[
            (
                "Copilot changes a confirmed fact during rewrite.",
                "Reject the rewrite, narrow the selected text and state which terms, dates and statuses must remain exact.",
            ),
            (
                "The document is longer than two pages.",
                "Remove duplication, convert owner details to a compact table and shorten explanation without removing evidence or open questions.",
            ),
            (
                "A source note points to the wrong file.",
                "Return to tblClaims, identify the governing Source_ID and correct both the note and any affected wording.",
            ),
        ],
        challenge=(
            "Ask Copilot in Chat-only mode to pressure-test the brief from a department head's perspective. Add only "
            "questions that expose a genuine evidence gap; do not let speculative questions become new facts."
        ),
        reflection="What is the difference between improving a sentence and changing the commitment expressed by that sentence?",
    ),
    dict(
        num=3,
        topic=1,
        title="Generate and Refine the Asteron Decision Deck in PowerPoint",
        duration=40,
        objective=(
            "LO2: generate a presentation from an approved Word source, refine the narrative and verify "
            "facts, visuals, accessibility and speaker notes before use"
        ),
        goal=(
            "Create a concise six-slide decision deck that preserves the approved Word brief and makes the "
            "remaining decision visible without inventing evidence."
        ),
        workflow=["Generate from file", "Check story", "Trace facts", "Refine visuals", "Release deck"],
        desc=(
            "You will use the approved Lab 2 Word brief to generate a PowerPoint draft for department heads. "
            "You will compare every factual slide with the source, replace generic or misleading content, refine "
            "one slide from a referenced file and complete an accessibility and release check."
        ),
        build=(
            "work-c027/C027-Asteron-Decision-Deck-v1.0.pptx with six decision-oriented slides, concise "
            "speaker notes, source notes and a Reviewed for internal presentation status"
        ),
        services="PowerPoint for Microsoft 365 · Copilot in PowerPoint · C027-Asteron-Launch-Brief-v1.0.docx",
        prerequisites=[
            "Lab 2 Word brief is saved in OneDrive and marked Approved for deck handoff.",
            "Open labs/assets/asteron-deck-spec.md and keep the Lab 1 source register available.",
            "Use only synthetic Asteron files and approved built-in or licensed visual assets.",
        ],
        steps=[
            (
                "Open PowerPoint, start a new presentation and use Copilot to create a presentation from "
                "C027-Asteron-Launch-Brief-v1.0.docx. Request exactly six slides for department heads. Save the "
                "result immediately as work-c027/C027-Asteron-Decision-Deck-v1.0.pptx.",
                "Create a six-slide internal decision presentation from the referenced approved Word brief. "
                "Use concise titles, one message per slide and speaker notes. Do not add facts not present in the source.",
            ),
            (
                "Compare the generated structure with the deck specification. Rename, reorder, add or remove slides "
                "until the sequence is exactly: decision, scope, readiness, timeline, risks and next actions. Keep the "
                "support-clinic room visibly unresolved. Because verified numerical readiness measures are not created "
                "until Lab 4, slide 3 must show dependencies and status only; add no readiness numbers in this lab.",
                "Required sequence:\n"
                "1. Decision needed\n"
                "2. Pilot scope\n"
                "3. Readiness snapshot\n"
                "4. Timeline and owners\n"
                "5. Risks and open question\n"
                "6. Next actions",
            ),
            (
                "For slides 2-6, compare every date, number, owner and status with the Word brief and source register. "
                "Add a small source note in the speaker notes using Source_ID values. Remove or rewrite any content that "
                "cannot be traced.",
                "Required facts:\n"
                "20 internal participants · five departments · 2026-08-18 launch\n"
                "Nisha Rao / 2026-08-11 · Leon Wu / 2026-08-13\n"
                "external announcement waits for privacy sign-off\n"
                "support clinic room remains open",
            ),
            (
                "Refine slide 4 by asking Copilot to rewrite the existing timeline. If Copilot creates a new timeline "
                "slide, move it into position 4 and delete the superseded slide so the deck remains exactly six slides. "
                "Keep four milestones only. Replace decorative imagery that could be mistaken for real Asteron evidence "
                "with a simple editable timeline or icon-based process.",
                "Create a four-milestone timeline from the referenced brief: FAQ due 2026-08-11; data export due "
                "2026-08-13; privacy sign-off before external announcement; pilot launch 2026-08-18. "
                "Do not add a confirmed support-clinic milestone.",
            ),
            (
                "Run Review > Check Accessibility in PowerPoint. Resolve each fixable issue and record the Accessibility "
                "Checker result, including any accepted limitation, in the final notes. Then confirm a single message per "
                "slide, readable text, strong contrast, logical reading order, meaningful alternative text, concise speaker "
                "notes and no unsupported image. In the file properties or final notes, record status Reviewed for internal "
                "presentation, reviewer and date.",
                "Release check:\n"
                "Story | Facts | Visual evidence | Accessibility | Speaker notes | Audience | Reviewer | State",
            ),
        ],
        test=(
            "The deck must contain exactly six slides in the required sequence. All repeated facts must match the "
            "approved Word brief, slide 3 must show dependencies/status without numerical readiness measures, slide 4 "
            "must contain only the four approved milestones, and no visual may imply real customer evidence. Each factual "
            "slide must have a Source_ID note. The final notes must record the Accessibility Checker result, and the final "
            "state must be Reviewed for internal presentation."
        ),
        checkpoint=(
            "Save and close the six-slide deck. Labs 7 and 8 will check it against the other app outputs. Keep the "
            "approved Word brief unchanged as the governing narrative source."
        ),
        troubleshooting=[
            (
                "Create from file is unavailable or the Word file is not listed.",
                "Confirm the file is saved to OneDrive, the correct account is active and Copilot is enabled. If necessary, "
                "create the six-slide structure manually and use Copilot to draft one slide at a time from the brief.",
            ),
            (
                "Copilot creates more or fewer than six slides.",
                "Keep only the required sequence and merge duplicate content. Do not add slides merely to preserve generated text.",
            ),
            (
                "A generated image is irrelevant or misleading.",
                "Remove it and use an editable shape, icon or timeline that communicates structure without pretending to be evidence.",
            ),
        ],
        challenge=(
            "Use Copilot to propose two alternative titles for slide 1: one neutral and one action-oriented. Choose the "
            "title that best reflects the actual decision without overstating urgency or certainty."
        ),
        reflection="Which part of the Word brief required the greatest transformation to work as a slide, and what had to remain unchanged?",
    ),
]
