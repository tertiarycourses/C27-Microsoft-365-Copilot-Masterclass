"""Single source of truth for the C027 non-WSQ courseware package."""

TITLE = "Microsoft 365 Copilot Masterclass"
SHORT_TITLE = "Microsoft 365 Copilot Masterclass"
COURSE_CODE = "C027"
COURSE_PAGE = "tertiarycourses.com.sg/microsoft-365-copilot-masterclass.html"
VERSION = "v1.0"
VERSION_DATE = "29 July 2026"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Assigned Tertiary Infotech Academy Trainer"
DAYS = 1
DAY_MINUTES = 480
INSTRUCTIONAL_MINUTES = 450
MODE = "Instructor-led masterclass with connected hands-on labs"
DAILY_TIMING = (
    "9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; "
    "7.5 instructional hours)"
)
DARK_THEME = False

TRAINER_TEAM = [
    (
        "Kesston Tang",
        "Consultant and trainer with experience in business analysis, negotiation, corporate advisory and stakeholder communication.",
    ),
    (
        "Angel Koh",
        "Technology practitioner and trainer with extensive experience designing information systems and applying emerging digital tools.",
    ),
]

ICE_BREAKER = [
    "Your name, organisation and role.",
    "One Microsoft 365 task that repeatedly consumes time.",
    "One output you would never share without checking it first.",
    "Which Copilot entry points you can see in Chat, Word, PowerPoint, Excel, Outlook and Teams.",
]

LEARNING_OUTCOMES = [
    (
        "LO1: Explain how Microsoft 365 Copilot grounds responses, apply a structured prompt method "
        "and verify a source-backed research summary in Copilot Chat."
    ),
    (
        "LO2: Draft, rewrite and validate a business document in Word, then generate and refine a "
        "presentation in PowerPoint from the approved document."
    ),
    (
        "LO3: Analyse a bounded dataset and generate formulas in Excel, then summarise a synthetic "
        "email thread and prepare a reviewed response in Outlook."
    ),
    (
        "LO4: Produce a Teams meeting recap and action register, connect outputs across Microsoft "
        "365 apps, and apply responsible-use, privacy and human-review controls."
    ),
]

LO_TITLES = [
    "Ground & Prompt",
    "Write & Present",
    "Analyse & Communicate",
    "Coordinate & Govern",
]

TOPIC_RECAPS = {
    1: [
        (
            "LO1 - Ground and Prompt",
            "Distinguish prompt instructions from grounding sources, use Goal-Context-Source-Expectations, "
            "and trace every factual statement in a Copilot Chat summary to an approved source.",
        ),
        (
            "LO2 - Write and Present",
            "Use Word to draft and rewrite against an audience brief, approve the document before handoff, "
            "and use that approved file as the source for a concise PowerPoint presentation.",
        ),
    ],
    2: [
        (
            "LO3 - Analyse and Communicate",
            "Bound Excel analysis to named data, inspect formulas and reconcile totals; in Outlook, separate "
            "thread facts from generated wording and keep the final send decision with the user.",
        ),
        (
            "LO4 - Coordinate and Govern",
            "Validate Teams actions against the transcript, preserve ownership and due dates across app "
            "handoffs, and use permissions, sensitivity, source checks and human approval as release gates.",
        ),
    ],
}

TOPICS = [
    dict(
        num=1,
        code="01",
        title="Getting Started with Microsoft 365 Copilot",
        subtitle=(
            "How Copilot works · effective prompts · Copilot Chat research · "
            "Word drafting and rewriting · PowerPoint generation and refinement"
        ),
        weighting="First half · 3 connected labs",
        concepts=[
            (
                "Orchestration and grounding",
                "Copilot combines the instruction, permitted work context and app capability before a model proposes a response.",
            ),
            (
                "G-C-S-E prompts",
                "State Goal, Context, Source and Expectations so the task, evidence boundary and output contract are visible.",
            ),
            (
                "Source-backed research",
                "Treat generated summaries as claims to trace, compare and approve rather than as automatic truth.",
            ),
            (
                "Word review loop",
                "Draft, inspect, rewrite a bounded selection, compare against the brief and approve the document.",
            ),
            (
                "Document-to-deck handoff",
                "Use an approved Word file as the PowerPoint source, then check structure, facts, visuals and speaker notes.",
            ),
            (
                "Availability awareness",
                "Licensing, organisational policy, platform and update channel can change which Copilot controls are visible.",
            ),
        ],
        sections=[
            dict(
                title="Introduction to Microsoft 365 Copilot and How It Works",
                definition=(
                    "Microsoft 365 Copilot is an AI-powered work assistant integrated with Microsoft 365 apps. "
                    "For a signed-in user it can combine the prompt, permitted organisational context from "
                    "Microsoft Graph, optional web grounding and the capabilities of the current app. The large "
                    "language model proposes an output; Microsoft 365 then returns it to the user for review."
                ),
                why=(
                    "A useful response depends on both the instruction and the information available to ground it. "
                    "Copilot does not receive unlimited visibility into a tenant: it works within the signed-in "
                    "user's permissions. Weak source access can produce an incomplete answer, while excessive "
                    "sharing can expose information that the user was already allowed to find."
                ),
                how=[
                    "The user states a task in Copilot Chat or inside a Microsoft 365 app.",
                    "Copilot interprets the instruction and retrieves permitted context from named files, current app content, work data or the web when enabled.",
                    "The model generates a proposal; the app presents the response, citations, draft or editable change for human inspection.",
                    "The user checks source coverage, accuracy, tone, permissions and downstream consequences before keeping or sharing it.",
                ],
                example=[
                    "An operations coordinator asks for a launch summary using an approved brief and a decision log.",
                    "Copilot grounds the response only in files the coordinator can access and returns a draft with source references.",
                    "The coordinator notices one missing decision, adds the correct source and regenerates before approving the summary.",
                ],
                use_when=[
                    "The task and evidence boundary are clear, the user has legitimate access and a person can review the output.",
                    "A draft, summary, comparison or first-pass structure will accelerate work without removing accountability.",
                ],
                avoid_when=[
                    "The task would disclose information to an unintended audience or relies on content the user should not access.",
                    "An unchecked output would trigger a high-impact financial, legal, safety, employment or customer decision.",
                ],
                quality=[
                    ("Permission", "Confirm the signed-in identity and whether every referenced source is appropriate for the task."),
                    ("Grounding", "Name the source and distinguish retrieved evidence from generated connective language."),
                    ("Review", "Check the response against the original files before accepting, editing or sharing it."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture",
                    "https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview",
                    "https://support.microsoft.com/en-US/Microsoft-365-Copilot/how-copilot-chat-works-in-microsoft-365-apps",
                ],
            ),
            dict(
                title="Writing Effective Prompts for Better Results",
                definition=(
                    "A prompt is the instruction and context supplied to Copilot. The C027 method uses four "
                    "elements: Goal states the outcome; Context explains the audience and situation; Source "
                    "sets the evidence boundary; Expectations define format, tone, constraints and review criteria. "
                    "A clear goal is essential, while the other elements reduce ambiguity and improve control."
                ),
                why=(
                    "Vague prompts shift important choices to the model. A visible prompt contract makes it easier "
                    "to compare the result with what was requested, identify missing evidence and refine only the "
                    "weak element. Effective prompting is iterative: ask, inspect, point to the gap and follow up."
                ),
                how=[
                    "Goal: use one action verb and name the decision, artifact or change required.",
                    "Context: state the audience, business situation, time period, terminology and intended use.",
                    "Source: name the files, thread, meeting, table or approved web sources to use and any sources to exclude.",
                    "Expectations: specify structure, length, tone, units, citation needs, uncertainty labels and acceptance checks.",
                    "Review the response, then use a focused follow-up instead of restarting with another vague prompt.",
                ],
                example=[
                    "Goal: create a one-page launch brief for department heads.",
                    "Context: the Asteron client portal pilot begins on 18 August and leaders need decisions, owners and risks.",
                    "Source: use only Project_Brief and Decision_Log; do not add market facts.",
                    "Expectations: five headings, concise professional tone, ISO dates, a source note for every decision and an Open Questions section.",
                ],
                use_when=[
                    "The task has a definable output and the user can name a trustworthy evidence boundary.",
                    "The first response is close but needs a controlled change to scope, format, tone or source coverage.",
                ],
                avoid_when=[
                    "The user cannot explain the intended decision or determine which source should govern the answer.",
                    "The prompt contains credentials, secrets or unnecessary sensitive personal information.",
                ],
                quality=[
                    ("Specific", "One task, one audience and one intended use."),
                    ("Grounded", "Named sources and explicit exclusions."),
                    ("Verifiable", "Acceptance checks that a reviewer can apply without guessing."),
                ],
                sources=[
                    "https://support.microsoft.com/en-US/Microsoft-365-Copilot/get-started-writing-prompts-in-microsoft-365-copilot",
                    "https://learn.microsoft.com/en-us/training/modules/get-ready-work-microsoft-365-copilot/",
                ],
            ),
            dict(
                title="Researching and Summarising with Copilot Chat",
                definition=(
                    "Copilot Chat is a conversational workspace for asking questions, researching and synthesising "
                    "information. Depending on the signed-in account, licence and organisational settings, it may use "
                    "web information, explicitly referenced files and broader work context. The response can include "
                    "citations or source links that help the user trace statements back to evidence."
                ),
                why=(
                    "Research becomes faster when Copilot can compare several permitted sources with explicit authority "
                    "labels, but synthesis can hide "
                    "contradictions, missing dates or weak evidence. A source register and claim ledger keep the research "
                    "auditable: every important claim is recorded with its source, confidence and unresolved question."
                ),
                how=[
                    "Define the research question and decide whether the boundary is work sources, web sources or both.",
                    "Attach or reference only the permitted source pack, preserve each file's authority and status, and ask "
                    "for a source-by-source inventory before synthesis.",
                    "Request claims in a table with source, evidence, uncertainty and follow-up needed.",
                    "Open the referenced material, compare quotations and numbers, and mark each claim Verified, Revise or Hold.",
                    "Save the approved summary and source register for the next app rather than relying on chat history alone.",
                ],
                example=[
                    "Copilot compares the Asteron project brief, stakeholder notes and decision log.",
                    "It correctly identifies the launch date but assigns the wrong owner because two notes use similar role titles.",
                    "The learner opens both sources, corrects the owner and records the unresolved training-room capacity question.",
                ],
                use_when=[
                    "Several accessible sources must be summarised, compared or turned into questions for a reviewer.",
                    "A human can inspect the cited sources and keep a durable record of the approved findings.",
                ],
                avoid_when=[
                    "The answer would depend on inaccessible, outdated or unapproved evidence that cannot be checked.",
                    "The user plans to paste the generated text directly into a public deliverable without source review.",
                ],
                quality=[
                    ("Coverage", "List which sources were used, missing and excluded."),
                    ("Traceability", "Link every material claim, date, number and owner to its governing source."),
                    ("Uncertainty", "Preserve contradictions and open questions instead of smoothing them away."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/microsoft-365-copilot/frequently-asked-questions-about-microsoft-365-copilot-chat",
                    "https://support.microsoft.com/en-us/onedrive/summarize-your-files-with-copilot",
                ],
            ),
            dict(
                title="Drafting, Rewriting and Summarising Documents in Word",
                definition=(
                    "Copilot in Word can create a draft from a prompt or referenced file, rewrite selected text, "
                    "summarise a document and answer questions about its contents. Chat-only work can stay in the pane, "
                    "while editing actions propose changes in the document. The user keeps control by reviewing the "
                    "preview, retaining accurate wording and rejecting unsupported additions."
                ),
                why=(
                    "Word turns research into a governed business artifact. A good workflow separates the approved facts "
                    "from the generated expression: the brief controls scope, the source pack controls content, the style "
                    "guide controls voice and a release checklist controls whether the document is ready to hand off."
                ),
                how=[
                    "Start from a saved Word file and state audience, purpose, length, structure and named source files.",
                    "Generate a first draft, then compare every heading, date, owner, number and commitment with the source register.",
                    "Select only the weak passage and request a bounded rewrite that preserves meaning and defined terms.",
                    "Use comments or a review table to record Keep, Change or Remove decisions.",
                    "Save an approved version before another app uses the document as a source.",
                ],
                example=[
                    "The learner creates an Asteron launch brief of no more than two pages from a supported verified-claims TXT export.",
                    "A rewrite makes the risks more concise but accidentally changes 'pilot group' to 'all customers'.",
                    "The learner rejects that change, restores the approved scope and marks the file Approved for deck handoff.",
                ],
                use_when=[
                    "A document needs a structured first draft, a bounded tone change or a source-based summary.",
                    "The owner can review proposed changes and maintain version history in OneDrive or SharePoint.",
                ],
                avoid_when=[
                    "The source brief is unresolved or the requested rewrite could alter a binding commitment without review.",
                    "The document contains material the signed-in account is not authorised to process with the feature.",
                ],
                quality=[
                    ("Fidelity", "Preserve approved meaning, scope, dates, owners and defined terms."),
                    ("Audience", "Use the reader's decisions and questions to shape structure and tone."),
                    ("Release", "Approve a named version before it becomes the source for another artifact."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/word/welcome-to-copilot-in-word",
                    "https://support.microsoft.com/en-us/office/create-a-summary-of-your-document-with-copilot-in-word",
                ],
            ),
            dict(
                title="Generating and Refining Presentations in PowerPoint",
                definition=(
                    "Copilot in PowerPoint can draft a presentation from a prompt or an existing Word or PDF file, "
                    "create or refine slide text, add a slide grounded in a referenced file, and summarise a deck. "
                    "The generated presentation remains a draft: layout, facts, sequence, visuals, accessibility and "
                    "speaker notes still require expert review."
                ),
                why=(
                    "A document-to-deck workflow can preserve the approved narrative while reducing assembly time. "
                    "However, a slide is not a paragraph pasted onto a canvas. Each slide needs one message, visible "
                    "evidence and a role in the story; decorative images must not imply facts that the source does not support."
                ),
                how=[
                    "Approve and save the source document in OneDrive or SharePoint before starting the presentation.",
                    "Ask for a bounded slide count, named audience, decision-oriented sequence and required sections.",
                    "Compare slide titles, claims, dates, owners and numbers with the Word source and source register.",
                    "Refine one slide at a time, replacing generic text and inappropriate imagery with accurate content.",
                    "Check reading order, alt text, contrast, speaker notes and the final call to action before sharing.",
                ],
                example=[
                    "Copilot creates a six-slide Asteron launch deck from the approved Word brief.",
                    "The generated risks slide omits the training dependency and uses a generic image unrelated to the pilot.",
                    "The learner restores the missing risk, replaces the image with a simple milestone diagram and adds source notes.",
                ],
                use_when=[
                    "A stable source document already contains the approved narrative and the deck needs a fast first structure.",
                    "The presenter can edit the result, check accessibility and rehearse the final story.",
                ],
                avoid_when=[
                    "The source file is unapproved, contradictory or too long to support a focused presentation.",
                    "A generated image or slide could be mistaken for real operational evidence.",
                ],
                quality=[
                    ("Story", "One audience, one decision path and one message per slide."),
                    ("Evidence", "Every factual slide traces to the approved source; visuals do not fabricate proof."),
                    ("Accessibility", "Readable contrast, concise text, logical reading order and useful alternative text."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint",
                    "https://support.microsoft.com/en-us/powerpoint/frequently-asked-questions-about-copilot-in-powerpoint",
                    "https://support.microsoft.com/en-us/microsoft-365-copilot/prepare-your-presentation-with-microsoft-365-copilot",
                ],
            ),
        ],
    ),
    dict(
        num=2,
        code="02",
        title="Copilot Across Your Everyday Work Apps",
        subtitle=(
            "Excel analysis and formulas · Outlook email work · Teams recaps · "
            "end-to-end app workflows · responsible AI and data privacy"
        ),
        weighting="Second half · 5 connected labs",
        concepts=[
            (
                "Bounded Excel analysis",
                "Name the table, columns, filters, units and expected checks before asking for a formula or insight.",
            ),
            (
                "Thread-to-response control",
                "Separate facts extracted from an Outlook thread from the generated wording of a draft reply.",
            ),
            (
                "Transcript-backed actions",
                "A Teams recap is useful only when owners, due dates and decisions agree with the meeting evidence.",
            ),
            (
                "Handoff contracts",
                "Each app passes an approved artifact, source note, owner and verification status to the next app.",
            ),
            (
                "Permissions are the perimeter",
                "Copilot honours the user's access; overshared content therefore remains an organisational risk.",
            ),
            (
                "Human release gate",
                "Generated content stays in Draft or Hold until a named person checks evidence, sensitivity and audience.",
            ),
        ],
        sections=[
            dict(
                title="Analysing Data and Generating Formulas in Excel",
                definition=(
                    "Copilot in Excel can help analyse table-like data, surface summaries, trends and outliers, generate "
                    "or explain formulas, and create editable workbook elements such as tables, PivotTables and charts in "
                    "supported experiences. Some analytical responses may be static. The user must understand the grain, "
                    "data types, filters and calculation logic before relying on the output."
                ),
                why=(
                    "A plausible formula can still use the wrong denominator, sign, date boundary or blank-value rule. "
                    "Excel makes generated logic inspectable, so the masterclass pairs every Copilot action with an "
                    "independent control: row count, formula sample, reconciliation total and edge-case review."
                ),
                how=[
                    "Save the workbook to an approved cloud location, keep the raw data unchanged and convert the bounded range into a named table.",
                    "State the row grain, business question, named columns, filters, units and required output.",
                    "Ask Copilot to propose or explain the formula before applying it; inspect structured references and fill behaviour.",
                    "Recalculate control totals using an independent method and sample normal, blank and boundary rows.",
                    "Label generated insights as Observed, Hypothesis or Unknown and record the checked workbook version.",
                ],
                example=[
                    "Asteron needs confirmed attendance rate and follow-up priority for a 20-person pilot cohort.",
                    "Copilot proposes a rate formula, but the learner notices blank attendance values are included in the denominator.",
                    "The learner revises the rule, checks three edge rows and ties the summary counts to the raw table.",
                ],
                use_when=[
                    "The data is tabular, the requested calculation is explicit and the workbook can retain visible controls.",
                    "The user can inspect formulas, PivotTables, charts or generated analytical logic.",
                ],
                avoid_when=[
                    "The dataset has undefined grain, mixed meanings or unresolved quality problems.",
                    "A static generated visual would be mistaken for a refreshable workbook result.",
                ],
                quality=[
                    ("Boundary", "Name the table, columns, date range, filters, units and exclusions."),
                    ("Logic", "Inspect formula, aggregation and missing-value rules rather than accepting the label."),
                    ("Tie-out", "Reconcile counts and totals independently before interpreting patterns."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel",
                    "https://support.microsoft.com/en-us/office/edit-with-copilot-in-excel-a2fd6fe4-97ac-416b-b89a-22f4d1357c7a",
                    "https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions",
                ],
            ),
            dict(
                title="Drafting Emails and Summarising Threads in Outlook",
                definition=(
                    "Copilot in Outlook can summarise email threads, draft messages from a prompt and thread context, "
                    "offer coaching on tone and clarity, and help prepare for meetings in eligible experiences. Feature "
                    "availability varies by licence, client and policy. Signed, encrypted, rights-managed or some labelled "
                    "messages can have additional limitations."
                ),
                why=(
                    "Email combines factual history with a consequential communication act. A safe workflow first extracts "
                    "decisions, requests, owners and dates from the thread, then drafts a reply that does not invent agreement. "
                    "The sender verifies recipients, attachments, sensitivity, commitments and tone before sending."
                ),
                how=[
                    "Open the bounded synthetic thread and ask for decisions, action items, open questions and conflicting statements.",
                    "Compare the summary with each message and correct owner, date, number and status errors.",
                    "Draft a response with explicit audience, purpose, tone, commitments and items that must remain unresolved.",
                    "Use coaching to review clarity and tone without allowing a rewrite to change factual meaning.",
                    "Check To, Cc, attachments, links, sensitivity and every commitment; keep the message as a draft until approved.",
                ],
                example=[
                    "The Asteron thread contains two proposed training dates but only one confirmed room booking.",
                    "Copilot's first draft presents both dates as final. The learner restores the distinction and asks the facilities owner to confirm.",
                    "The message remains in Draft and its facts are compared with the decision log before any send action.",
                ],
                use_when=[
                    "A bounded thread needs a catch-up summary, response outline or tone review.",
                    "The sender can inspect the complete thread and owns the final recipient and send decisions.",
                ],
                avoid_when=[
                    "The thread includes highly sensitive content not suitable for the intended audience or unsupported client experience.",
                    "The generated draft would create a commitment that no authorised person has approved.",
                ],
                quality=[
                    ("Facts", "Separate thread evidence from generated wording and preserve unresolved items."),
                    ("Recipients", "Recheck To, Cc, attachments and audience before release."),
                    ("Commitments", "Do not turn proposals, questions or estimates into promises."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/outlook/frequently-asked-questions-about-copilot-in-outlook",
                    "https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-outlook-07420c70-099e-4552-8522-7d426712917b",
                ],
            ),
            dict(
                title="Meeting Recaps and Action Items in Teams",
                definition=(
                    "Copilot and intelligent recap in Teams can use a meeting transcript, chat and supported event content "
                    "to summarise key points, decisions and follow-up tasks. Recap features depend on the event type, licence, "
                    "recording or transcription settings, language and organisational policy. A recap is generated evidence "
                    "aid, not a replacement for the governing transcript or a confirmed action register."
                ),
                why=(
                    "Meeting summaries compress fast-moving conversation, but transcription errors and ambiguous speech can "
                    "misassign an owner or due date. A strong action register requires an action verb, deliverable, named owner, "
                    "ISO date, status and a transcript reference; unresolved statements stay open."
                ),
                how=[
                    "Obtain consent and follow organisational policy before recording or transcription; use the supplied synthetic transcript when live transcription is unavailable.",
                    "Ask for decisions, action items, blockers and open questions in separate sections.",
                    "Compare each item with the transcript or chat and correct speaker attribution, negation, numbers and dates.",
                    "Convert confirmed actions into a register with owner, deliverable, due date, evidence and status.",
                    "Share the reviewed register only with the intended participants and retain open questions visibly.",
                ],
                example=[
                    "A speaker says the FAQ draft is due Friday, but the room booking will be confirmed next Monday.",
                    "The generated recap assigns both items to the same owner and date.",
                    "The learner checks the transcript, corrects the two records and labels the room decision Open.",
                ],
                use_when=[
                    "A permitted transcript or meeting chat exists and the participants need a faster first recap.",
                    "A person who attended can validate decisions, owners and due dates before circulation.",
                ],
                avoid_when=[
                    "Recording or transcription is not permitted, participants have not been informed or sensitive discussion needs special handling.",
                    "The recap will be treated as final minutes without comparison to the meeting evidence.",
                ],
                quality=[
                    ("Consent", "Follow policy and participant expectations for recording, transcription and sharing."),
                    ("Evidence", "Link actions and decisions to transcript language or chat context."),
                    ("Ownership", "Every confirmed action has one owner, one deliverable and one due date."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/teams/meetings-events/recap-a-teams-meeting",
                    "https://support.microsoft.com/en-us/teams/meetings/recap-in-microsoft-teams",
                    "https://support.microsoft.com/en-us/teams/copilot/how-to-use-microsoft-365-copilot-in-teams-chats-and-channels",
                ],
            ),
            dict(
                title="Building End-to-End Copilot Workflows Across Apps",
                definition=(
                    "An end-to-end Copilot workflow connects approved outputs across apps without losing source boundaries, "
                    "ownership or review status. The key is a handoff contract: every transition names the source artifact, "
                    "approved version, intended destination, required transformation, constraints, owner and verification gate."
                ),
                why=(
                    "Cross-app speed can multiply an early error. If an unverified chat summary becomes a Word brief, then a "
                    "deck, email and meeting plan, one wrong date appears everywhere. Checkpointed handoffs contain the blast "
                    "radius: downstream apps receive only approved artifacts and changes are reconciled back to the source register."
                ),
                how=[
                    "Map the workflow from source evidence to Chat synthesis, Word brief, PowerPoint deck, Excel analysis, Outlook draft and Teams actions.",
                    "Define a release state for each artifact: Draft, Reviewed, Approved or Hold.",
                    "At each handoff, name the file and version, destination, allowed transformation and facts that must not change.",
                    "Run a consistency check for titles, dates, numbers, owners, terminology and audience across every artifact.",
                    "Record the final owner and next action; keep links rather than duplicating uncontrolled copies where possible.",
                ],
                example=[
                    "The approved Asteron Word brief supplies the story for PowerPoint, while Excel supplies verified attendance figures.",
                    "The Outlook draft and Teams action register use links to those artifacts and repeat only the minimum confirmed facts.",
                    "A cross-app check detects that one slide uses an earlier launch date; the learner corrects it before the pack is released.",
                ],
                use_when=[
                    "Several apps contribute distinct strengths and each handoff can be checkpointed.",
                    "A named owner can reconcile downstream outputs to the governing sources.",
                ],
                avoid_when=[
                    "The workflow copies unapproved chat text from app to app or obscures which file is authoritative.",
                    "Automation would send, publish or schedule consequential output without a human release gate.",
                ],
                quality=[
                    ("Authority", "Declare which artifact governs each fact, number and commitment."),
                    ("State", "Show Draft, Reviewed, Approved or Hold at every handoff."),
                    ("Consistency", "Reconcile titles, dates, owners, measures and audience across the full pack."),
                ],
                sources=[
                    "https://support.microsoft.com/en-us/microsoft-365-copilot/",
                    "https://support.microsoft.com/en-us/office/365-copilot-app/get-started-with-word-excel-and-powerpoint-agents-in-microsoft-365-copilot",
                ],
            ),
            dict(
                title="Responsible AI, Data Privacy and Best Practices",
                definition=(
                    "Responsible use of Microsoft 365 Copilot combines technical protections with human judgment. "
                    "For organisational use, enterprise data protection applies to prompts and responses, Microsoft 365 "
                    "permissions continue to govern accessible work data, and interactions can be retained for audit and "
                    "compliance. These protections do not correct oversharing, weak sources or inaccurate generated content."
                ),
                why=(
                    "Copilot can accelerate existing good practice and expose existing information-governance weaknesses. "
                    "A user who can access an overshared file may receive it in grounded results. Responsible practice therefore "
                    "uses least privilege, sensitivity and sharing controls, minimal necessary data, source verification, "
                    "transparent AI use where appropriate and named human accountability."
                ),
                how=[
                    "Confirm identity, licence, organisational policy, approved app and the minimum data necessary for the task.",
                    "Check file permissions, sharing links, labels and audience before referencing or publishing content.",
                    "Do not place credentials, secrets or unnecessary sensitive personal information in prompts.",
                    "Review outputs for factual error, harmful bias, privacy exposure, unsupported inference and inappropriate tone.",
                    "Record sources, meaningful AI assistance, reviewer, release decision and unresolved limitations.",
                ],
                example=[
                    "A Copilot search surfaces an old broadly shared roster with personal contact details.",
                    "The learner does not use or reproduce the roster, reports the oversharing through the organisation's process and uses the synthetic cohort file instead.",
                    "The final pack records its sources, reviewer and Approved state without exposing unnecessary personal information.",
                ],
                use_when=[
                    "The task uses authorised data, proportionate controls and a reviewer who understands the decision context.",
                    "The organisation's retention, sensitivity, sharing and acceptable-use requirements are known.",
                ],
                avoid_when=[
                    "The prompt would expose secrets, bypass access controls, profile people unfairly or conceal an unsupported decision.",
                    "The user cannot identify who is accountable for checking and releasing the output.",
                ],
                quality=[
                    ("Minimise", "Use only the data and detail necessary for the declared purpose."),
                    ("Protect", "Apply permissions, labels, sharing and retention controls appropriate to the source."),
                    ("Account", "Name the reviewer, sources, limitations and release decision."),
                ],
                sources=[
                    "https://learn.microsoft.com/en-us/copilot/faq",
                    "https://learn.microsoft.com/en-us/microsoft-365/copilot/security-microsoft-365-copilot",
                    "https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture-data-protection-auditing",
                    "https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy",
                ],
            ),
        ],
    ),
]

DAY_THEMES = {
    1: "Ground, create, analyse, coordinate and govern one connected Microsoft 365 Copilot workflow",
}


def SCHEDULE(lab_titles):
    return {
        1: (
            DAY_THEMES[1],
            [
                (
                    "9:30",
                    "9:50",
                    20,
                    "admin",
                    "Welcome, learning outcomes, setup and Copilot availability check",
                ),
                (
                    "9:50",
                    "10:45",
                    55,
                    "topic",
                    "Topic 1 - Copilot architecture, G-C-S-E prompting, Chat, Word and PowerPoint concepts with demonstrations",
                ),
                ("10:45", "11:20", 35, "lab", "Hands-on: " + lab_titles([1])),
                ("11:20", "11:35", 15, "break", "Tea break"),
                ("11:35", "12:15", 40, "lab", "Hands-on: " + lab_titles([2])),
                ("12:15", "12:55", 40, "lab", "Hands-on: " + lab_titles([3])),
                ("12:55", "13:55", 60, "lunch", "Lunch break"),
                (
                    "13:55",
                    "14:40",
                    45,
                    "topic",
                    "Topic 2 - Excel, Outlook, Teams, cross-app handoffs, responsible use and data privacy",
                ),
                ("14:40", "15:25", 45, "lab", "Hands-on: " + lab_titles([4])),
                ("15:25", "16:00", 35, "lab", "Hands-on: " + lab_titles([5])),
                ("16:00", "16:15", 15, "break", "Tea break"),
                ("16:15", "16:50", 35, "lab", "Hands-on: " + lab_titles([6])),
                ("16:50", "17:35", 45, "lab", "Hands-on: " + lab_titles([7])),
                ("17:35", "18:20", 45, "lab", "Hands-on: " + lab_titles([8])),
                (
                    "18:20",
                    "18:30",
                    10,
                    "recap",
                    "Topic recaps mapped to LO1-LO4, continuing-practice plan and questions",
                ),
            ],
        ),
    }


COURSE_OVERVIEW = dict(
    section_title="The Traceable Copilot Work System",
    concepts_title="Keep Four Layers Visible",
    concepts=[
        ("Source", "The approved file, table, thread, transcript or web page that governs the facts."),
        ("Prompt", "Goal, Context, Source and Expectations, including exclusions and review criteria."),
        ("Proposal", "The generated summary, draft, formula, slide, action or change that still needs review."),
        ("Release", "The named reviewer, verification evidence, decision and approved destination."),
    ],
    framework_title="G-C-S-E Prompt Framework",
    framework=[
        ("Goal", "What to create, decide, explain, compare or change."),
        ("Context", "Audience, situation, terminology, time period and intended use."),
        ("Source", "Named evidence, permitted scope and explicit exclusions."),
        ("Expectations", "Format, tone, constraints, citations, uncertainty and checks."),
    ],
    statement=dict(
        headline="Copilot accelerates the proposal; the evidence and reviewer determine whether it is ready.",
        body="Ground every task, inspect every handoff and keep consequential release decisions with a named person.",
        kicker="C027 OPERATING PRINCIPLE",
    ),
    pillars_title="What You Will Build",
    pillars=[
        ("Evidence layer", ["source register", "claim ledger", "verified Excel controls"]),
        ("Communication layer", ["approved Word brief", "refined PowerPoint deck", "reviewed Outlook draft"]),
        ("Coordination layer", ["Teams action register", "cross-app manifest", "responsible-use review log"]),
    ],
    arc_title="The Learning Arc in Every Lab",
    arc=[
        "Open the supplied checkpoint and state the intended outcome.",
        "Prompt Copilot with G-C-S-E and a bounded source.",
        "Inspect the generated proposal in the current app.",
        "Complete Test It, record the release state and save the checkpoint.",
    ],
    deep_dives=[
        dict(
            title="The C027 Release Gate",
            kicker="BEFORE AN OUTPUT LEAVES DRAFT",
            items=[
                ("Source", "Are all material facts grounded in approved, current and accessible evidence?"),
                ("Accuracy", "Do dates, numbers, owners, formulas and commitments match the governing sources?"),
                ("Sensitivity", "Are permissions, labels, recipients and minimum-necessary data appropriate?"),
                ("Quality", "Does the output fit the audience, format, tone and accessibility needs?"),
                ("Consistency", "Do downstream files agree with the approved source register and each other?"),
                ("Accountability", "Is a named reviewer choosing Approved, Revise or Hold with limitations visible?"),
            ],
        ),
    ],
)

LAB_SHOTS = {}

LG_INTRO = (
    "This Learner Guide accompanies Microsoft 365 Copilot Masterclass (C027). It follows the same "
    "two-topic sequence, eight connected labs, four learning outcomes and synthetic Asteron Services "
    "scenario as the slide deck, Lesson Plan and standalone lab files."
)

LG_INTRO2 = (
    "Use the guide as a self-contained study text before, during and after class. Each concept explains "
    "what the capability is, why it matters, how it works, a worked example and when to use or avoid it. "
    "The labs then apply the concepts across Chat, Word, PowerPoint, Excel, Outlook and Teams. Copilot "
    "output remains a proposal until its sources, facts, audience, permissions and consequences are reviewed."
)

LG_SETUP = dict(
    needs=[
        "A Windows or Mac laptop with a current supported browser and Microsoft 365 apps or their web equivalents.",
        "An eligible Microsoft 365 account with the Copilot experiences enabled by the organisation or subscription.",
        "Access to Copilot Chat, Word, PowerPoint, Excel, Outlook and Teams; feature names can vary by licence and update channel.",
        "A downloaded copy of this repository with the labs/assets folder intact.",
        "Permission to use only the supplied synthetic Asteron Services material during class.",
    ],
    verify_text=(
        "Sign in at microsoft365.com and record which Copilot entry points are visible. Open "
        "labs/assets/asteron-source-register-template.csv and confirm it has the eight required headers. "
        "Create a work-c027 folder in an approved OneDrive location. If an app capability is unavailable, "
        "use Copilot Chat with the supplied source file and record the limitation; do not invent a result."
    ),
    verify_code=(
        "Expected local structure:\n"
        "C027---Microsoft-365-Copilot-Masterclass/\n"
        "  labs/assets/\n"
        "  work-c027/"
    ),
    conventions=[
        "All Asteron names, messages, meeting content and numbers are synthetic training material.",
        "Text between <ANGLE_BRACKETS> is a placeholder to replace; never paste a password, token or secret.",
        "VERIFIED means traced to a governing source; REVISE means a correctable gap; HOLD means unresolved or unsafe to release.",
        "Dates use yyyy-mm-dd, currency uses S$, percentages include the stated denominator and every action has one owner.",
        "Save the prompt, source, proposal, verification and human release decision together.",
    ],
)

LAB_NOTE = (
    "Use only the supplied synthetic Asteron Services data or information you are authorised to process. "
    "Do not paste credentials, confidential business material or unnecessary personal data into Copilot."
)

LG_WRAPUP = dict(
    title="Wrap-Up - The Complete C027 Workflow",
    intro=(
        "The finished output is a traceable work system, not a collection of attractive generated files. "
        "Every artifact connects its source, prompt, proposed output, verification evidence and release owner."
    ),
    sections=[
        dict(
            title="Ground and create",
            bullets=[
                "Use G-C-S-E to name the goal, audience, evidence boundary and output contract.",
                "Verify a Chat synthesis before it becomes the factual basis of a Word document.",
                "Approve the Word brief before PowerPoint turns it into a visual story.",
            ],
        ),
        dict(
            title="Analyse and coordinate",
            bullets=[
                "Keep Excel data grain, formula logic, denominators and control totals visible.",
                "Separate Outlook thread facts from generated reply wording and review every commitment.",
                "Tie Teams actions to transcript evidence, named owners and due dates.",
            ],
        ),
        dict(
            title="Govern and release",
            bullets=[
                "Pass only approved versions across app handoffs and reconcile repeated facts.",
                "Use least privilege, minimum necessary data, sensitivity and recipient checks.",
                "Choose Approved, Revise or Hold with a named human reviewer and visible limitations.",
            ],
        ),
    ],
)

LG_NEXT_STEPS = [
    "Repeat all eight labs from the original source pack without using your completed artifacts.",
    "Adapt the G-C-S-E prompt card and release gate to one authorised recurring task in your role.",
    "Create a small cross-app manifest for authoritative files, owners, versions and release states.",
    "Review Microsoft Support and Learn before delivery because Copilot labels, availability and capabilities continue to change.",
]

LG_GLOSSARY = [
    ("Copilot Chat", "A Microsoft 365 conversational experience for asking, researching, summarising and creating from permitted context."),
    ("Grounding", "Adding relevant source context to a prompt so the response is specific to the task."),
    ("G-C-S-E", "Goal, Context, Source and Expectations - the C027 prompt framework."),
    ("Handoff contract", "A record of source artifact, version, destination, allowed transformation, owner and verification gate."),
    ("Microsoft Graph", "The service layer through which Microsoft 365 can surface work context the signed-in user is permitted to access."),
    ("Observed", "A statement directly supported by the reviewed data or source."),
    ("Open question", "A material point that the available evidence does not resolve."),
    ("Release gate", "The source, accuracy, sensitivity, quality, consistency and accountability checks before sharing."),
    ("Sensitivity label", "A Microsoft Purview label that can classify and protect organisational content according to policy."),
    ("Source register", "A list of governing files or records with owner, date, purpose, status and access note."),
    ("Structured reference", "An Excel formula reference that uses table and column names."),
    ("Transcript", "The text record of meeting speech used as evidence for a generated recap."),
]

NEXT_STEPS = dict(
    title="Continue the Traceable Workflow",
    items=[
        "Reuse the G-C-S-E prompt card on one bounded, authorised task.",
        "Keep source, proposal, verification and release state together.",
        "Reconcile repeated dates, owners and numbers across every app handoff.",
        "Review current Microsoft guidance whenever features or labels change.",
    ],
)

THANK_YOU = dict(
    body=(
        "You can now ground, create, analyse, coordinate and govern Microsoft 365 Copilot work "
        "while keeping evidence, permissions and human judgment in control."
    ),
    kicker="MICROSOFT 365 COPILOT MASTERCLASS · C027",
)

VERSION_HISTORY = [
    (
        "1.0",
        VERSION_DATE,
        "Initial aligned release of PPT, Learner Guide, Lesson Plan and eight connected labs.",
        TRAINER,
    ),
]
