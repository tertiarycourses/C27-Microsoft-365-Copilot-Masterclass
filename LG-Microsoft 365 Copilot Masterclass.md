# Microsoft 365 Copilot Masterclass — Learner Guide

**Course Code:** C027  |  **Conducted by:** Tertiary Infotech Academy Pte Ltd (UEN 201200696W)  |  **Version v1.0 · 29 July 2026**

## Contents

- [Introduction](#introduction)
- [Course Learning Outcomes](#course-learning-outcomes)
- [Before You Start — Preparation](#before-you-start--preparation)
- [Topic 01 — Getting Started with Microsoft 365 Copilot  (First half · 3 connected labs)](#topic-01--getting-started-with-microsoft-365-copilot--first-half--3-connected-labs)
  - [Introduction to Microsoft 365 Copilot and How It Works](#introduction-to-microsoft-365-copilot-and-how-it-works)
  - [Writing Effective Prompts for Better Results](#writing-effective-prompts-for-better-results)
  - [Researching and Summarising with Copilot Chat](#researching-and-summarising-with-copilot-chat)
  - [Drafting, Rewriting and Summarising Documents in Word](#drafting-rewriting-and-summarising-documents-in-word)
  - [Generating and Refining Presentations in PowerPoint](#generating-and-refining-presentations-in-powerpoint)
  - [Lab 1 — Research the Asteron Launch and Build a Verified Source Register](#lab-1--research-the-asteron-launch-and-build-a-verified-source-register)
  - [Lab 2 — Draft and Approve the Asteron Launch Brief in Word](#lab-2--draft-and-approve-the-asteron-launch-brief-in-word)
  - [Lab 3 — Generate and Refine the Asteron Decision Deck in PowerPoint](#lab-3--generate-and-refine-the-asteron-decision-deck-in-powerpoint)
  - [Topic 01 Recap - Mapped to Learning Outcomes](#topic-01-recap---mapped-to-learning-outcomes)
- [Topic 02 — Copilot Across Your Everyday Work Apps  (Second half · 5 connected labs)](#topic-02--copilot-across-your-everyday-work-apps--second-half--5-connected-labs)
  - [Analysing Data and Generating Formulas in Excel](#analysing-data-and-generating-formulas-in-excel)
  - [Drafting Emails and Summarising Threads in Outlook](#drafting-emails-and-summarising-threads-in-outlook)
  - [Meeting Recaps and Action Items in Teams](#meeting-recaps-and-action-items-in-teams)
  - [Building End-to-End Copilot Workflows Across Apps](#building-end-to-end-copilot-workflows-across-apps)
  - [Responsible AI, Data Privacy and Best Practices](#responsible-ai-data-privacy-and-best-practices)
  - [Lab 4 — Analyse Pilot Readiness and Verify Copilot Formulas in Excel](#lab-4--analyse-pilot-readiness-and-verify-copilot-formulas-in-excel)
  - [Lab 5 — Summarise the Launch Thread and Prepare a Reviewed Outlook Draft](#lab-5--summarise-the-launch-thread-and-prepare-a-reviewed-outlook-draft)
  - [Lab 6 — Validate a Teams Recap and Create the Action Register](#lab-6--validate-a-teams-recap-and-create-the-action-register)
  - [Lab 7 — Assemble and Reconcile the Cross-App Coordination Pack](#lab-7--assemble-and-reconcile-the-cross-app-coordination-pack)
  - [Lab 8 — Run the Responsible-Use and Privacy Release Gate](#lab-8--run-the-responsible-use-and-privacy-release-gate)
  - [Topic 02 Recap - Mapped to Learning Outcomes](#topic-02-recap---mapped-to-learning-outcomes)
- [Wrap-Up - The Complete C027 Workflow](#wrap-up---the-complete-c027-workflow)
- [Next Steps](#next-steps)
- [Glossary](#glossary)


## Introduction

This Learner Guide accompanies Microsoft 365 Copilot Masterclass (C027). It follows the same two-topic sequence, eight connected labs, four learning outcomes and synthetic Asteron Services scenario as the slide deck, Lesson Plan and standalone lab files.

Use the guide as a self-contained study text before, during and after class. Each concept explains what the capability is, why it matters, how it works, a worked example and when to use or avoid it. The labs then apply the concepts across Chat, Word, PowerPoint, Excel, Outlook and Teams. Copilot output remains a proposal until its sources, facts, audience, permissions and consequences are reviewed.


## Course Learning Outcomes

- LO1: Explain how Microsoft 365 Copilot grounds responses, apply a structured prompt method and verify a source-backed research summary in Copilot Chat.
- LO2: Draft, rewrite and validate a business document in Word, then generate and refine a presentation in PowerPoint from the approved document.
- LO3: Analyse a bounded dataset and generate formulas in Excel, then summarise a synthetic email thread and prepare a reviewed response in Outlook.
- LO4: Produce a Teams meeting recap and action register, connect outputs across Microsoft 365 apps, and apply responsible-use, privacy and human-review controls.


## Before You Start — Preparation

**What you need**

- A Windows or Mac laptop with a current supported browser and Microsoft 365 apps or their web equivalents.
- An eligible Microsoft 365 account with the Copilot experiences enabled by the organisation or subscription.
- Access to Copilot Chat, Word, PowerPoint, Excel, Outlook and Teams; feature names can vary by licence and update channel.
- A downloaded copy of this repository with the labs/assets folder intact.
- Permission to use only the supplied synthetic Asteron Services material during class.

**Verify your setup**

Sign in at microsoft365.com and record which Copilot entry points are visible. Open labs/assets/asteron-source-register-template.csv and confirm it has the eight required headers. Create a work-c027 folder in an approved OneDrive location. If an app capability is unavailable, use Copilot Chat with the supplied source file and record the limitation; do not invent a result.

```bash
Expected local structure:
C027---Microsoft-365-Copilot-Masterclass/
  labs/assets/
  work-c027/
```

**Conventions used in every lab**

- All Asteron names, messages, meeting content and numbers are synthetic training material.
- Text between <ANGLE_BRACKETS> is a placeholder to replace; never paste a password, token or secret.
- VERIFIED means traced to a governing source; REVISE means a correctable gap; HOLD means unresolved or unsafe to release.
- Dates use yyyy-mm-dd, currency uses S$, percentages include the stated denominator and every action has one owner.
- Save the prompt, source, proposal, verification and human release decision together.


## Topic 01 — Getting Started with Microsoft 365 Copilot  (First half · 3 connected labs)

How Copilot works · effective prompts · Copilot Chat research · Word drafting and rewriting · PowerPoint generation and refinement

**Key concepts**

- Orchestration and grounding — Copilot combines the instruction, permitted work context and app capability before a model proposes a response.
- G-C-S-E prompts — State Goal, Context, Source and Expectations so the task, evidence boundary and output contract are visible.
- Source-backed research — Treat generated summaries as claims to trace, compare and approve rather than as automatic truth.
- Word review loop — Draft, inspect, rewrite a bounded selection, compare against the brief and approve the document.
- Document-to-deck handoff — Use an approved Word file as the PowerPoint source, then check structure, facts, visuals and speaker notes.
- Availability awareness — Licensing, organisational policy, platform and update channel can change which Copilot controls are visible.


### Introduction to Microsoft 365 Copilot and How It Works

Microsoft 365 Copilot is an AI-powered work assistant integrated with Microsoft 365 apps. For a signed-in user it can combine the prompt, permitted organisational context from Microsoft Graph, optional web grounding and the capabilities of the current app. The large language model proposes an output; Microsoft 365 then returns it to the user for review.

A useful response depends on both the instruction and the information available to ground it. Copilot does not receive unlimited visibility into a tenant: it works within the signed-in user's permissions. Weak source access can produce an incomplete answer, while excessive sharing can expose information that the user was already allowed to find.

**How it works**

- The user states a task in Copilot Chat or inside a Microsoft 365 app.
- Copilot interprets the instruction and retrieves permitted context from named files, current app content, work data or the web when enabled.
- The model generates a proposal; the app presents the response, citations, draft or editable change for human inspection.
- The user checks source coverage, accuracy, tone, permissions and downstream consequences before keeping or sharing it.

**Worked example**

- An operations coordinator asks for a launch summary using an approved brief and a decision log.
- Copilot grounds the response only in files the coordinator can access and returns a draft with source references.
- The coordinator notices one missing decision, adds the correct source and regenerates before approving the summary.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task and evidence boundary are clear, the user has legitimate access and a person can review the output. | The task would disclose information to an unintended audience or relies on content the user should not access. |
| A draft, summary, comparison or first-pass structure will accelerate work without removing accountability. | An unchecked output would trigger a high-impact financial, legal, safety, employment or customer decision. |

**Practitioner quality lens**

- Permission: Confirm the signed-in identity and whether every referenced source is appropriate for the task.
- Grounding: Name the source and distinguish retrieved evidence from generated connective language.
- Review: Check the response against the original files before accepting, editing or sharing it.

**Authoritative references**

- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview
- https://support.microsoft.com/en-US/Microsoft-365-Copilot/how-copilot-chat-works-in-microsoft-365-apps

---


### Writing Effective Prompts for Better Results

A prompt is the instruction and context supplied to Copilot. The C027 method uses four elements: Goal states the outcome; Context explains the audience and situation; Source sets the evidence boundary; Expectations define format, tone, constraints and review criteria. A clear goal is essential, while the other elements reduce ambiguity and improve control.

Vague prompts shift important choices to the model. A visible prompt contract makes it easier to compare the result with what was requested, identify missing evidence and refine only the weak element. Effective prompting is iterative: ask, inspect, point to the gap and follow up.

**How it works**

- Goal: use one action verb and name the decision, artifact or change required.
- Context: state the audience, business situation, time period, terminology and intended use.
- Source: name the files, thread, meeting, table or approved web sources to use and any sources to exclude.
- Expectations: specify structure, length, tone, units, citation needs, uncertainty labels and acceptance checks.
- Review the response, then use a focused follow-up instead of restarting with another vague prompt.

**Worked example**

- Goal: create a one-page launch brief for department heads.
- Context: the Asteron client portal pilot begins on 18 August and leaders need decisions, owners and risks.
- Source: use only Project_Brief and Decision_Log; do not add market facts.
- Expectations: five headings, concise professional tone, ISO dates, a source note for every decision and an Open Questions section.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task has a definable output and the user can name a trustworthy evidence boundary. | The user cannot explain the intended decision or determine which source should govern the answer. |
| The first response is close but needs a controlled change to scope, format, tone or source coverage. | The prompt contains credentials, secrets or unnecessary sensitive personal information. |

**Practitioner quality lens**

- Specific: One task, one audience and one intended use.
- Grounded: Named sources and explicit exclusions.
- Verifiable: Acceptance checks that a reviewer can apply without guessing.

**Authoritative references**

- https://support.microsoft.com/en-US/Microsoft-365-Copilot/get-started-writing-prompts-in-microsoft-365-copilot
- https://learn.microsoft.com/en-us/training/modules/get-ready-work-microsoft-365-copilot/

---


### Researching and Summarising with Copilot Chat

Copilot Chat is a conversational workspace for asking questions, researching and synthesising information. Depending on the signed-in account, licence and organisational settings, it may use web information, explicitly referenced files and broader work context. The response can include citations or source links that help the user trace statements back to evidence.

Research becomes faster when Copilot can compare several permitted sources with explicit authority labels, but synthesis can hide contradictions, missing dates or weak evidence. A source register and claim ledger keep the research auditable: every important claim is recorded with its source, confidence and unresolved question.

**How it works**

- Define the research question and decide whether the boundary is work sources, web sources or both.
- Attach or reference only the permitted source pack, preserve each file's authority and status, and ask for a source-by-source inventory before synthesis.
- Request claims in a table with source, evidence, uncertainty and follow-up needed.
- Open the referenced material, compare quotations and numbers, and mark each claim Verified, Revise or Hold.
- Save the approved summary and source register for the next app rather than relying on chat history alone.

**Worked example**

- Copilot compares the Asteron project brief, stakeholder notes and decision log.
- It correctly identifies the launch date but assigns the wrong owner because two notes use similar role titles.
- The learner opens both sources, corrects the owner and records the unresolved training-room capacity question.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Several accessible sources must be summarised, compared or turned into questions for a reviewer. | The answer would depend on inaccessible, outdated or unapproved evidence that cannot be checked. |
| A human can inspect the cited sources and keep a durable record of the approved findings. | The user plans to paste the generated text directly into a public deliverable without source review. |

**Practitioner quality lens**

- Coverage: List which sources were used, missing and excluded.
- Traceability: Link every material claim, date, number and owner to its governing source.
- Uncertainty: Preserve contradictions and open questions instead of smoothing them away.

**Authoritative references**

- https://support.microsoft.com/en-us/microsoft-365-copilot/frequently-asked-questions-about-microsoft-365-copilot-chat
- https://support.microsoft.com/en-us/onedrive/summarize-your-files-with-copilot

---


### Drafting, Rewriting and Summarising Documents in Word

Copilot in Word can create a draft from a prompt or referenced file, rewrite selected text, summarise a document and answer questions about its contents. Chat-only work can stay in the pane, while editing actions propose changes in the document. The user keeps control by reviewing the preview, retaining accurate wording and rejecting unsupported additions.

Word turns research into a governed business artifact. A good workflow separates the approved facts from the generated expression: the brief controls scope, the source pack controls content, the style guide controls voice and a release checklist controls whether the document is ready to hand off.

**How it works**

- Start from a saved Word file and state audience, purpose, length, structure and named source files.
- Generate a first draft, then compare every heading, date, owner, number and commitment with the source register.
- Select only the weak passage and request a bounded rewrite that preserves meaning and defined terms.
- Use comments or a review table to record Keep, Change or Remove decisions.
- Save an approved version before another app uses the document as a source.

**Worked example**

- The learner creates an Asteron launch brief of no more than two pages from a supported verified-claims TXT export.
- A rewrite makes the risks more concise but accidentally changes 'pilot group' to 'all customers'.
- The learner rejects that change, restores the approved scope and marks the file Approved for deck handoff.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A document needs a structured first draft, a bounded tone change or a source-based summary. | The source brief is unresolved or the requested rewrite could alter a binding commitment without review. |
| The owner can review proposed changes and maintain version history in OneDrive or SharePoint. | The document contains material the signed-in account is not authorised to process with the feature. |

**Practitioner quality lens**

- Fidelity: Preserve approved meaning, scope, dates, owners and defined terms.
- Audience: Use the reader's decisions and questions to shape structure and tone.
- Release: Approve a named version before it becomes the source for another artifact.

**Authoritative references**

- https://support.microsoft.com/en-us/word/welcome-to-copilot-in-word
- https://support.microsoft.com/en-us/office/create-a-summary-of-your-document-with-copilot-in-word

---


### Generating and Refining Presentations in PowerPoint

Copilot in PowerPoint can draft a presentation from a prompt or an existing Word or PDF file, create or refine slide text, add a slide grounded in a referenced file, and summarise a deck. The generated presentation remains a draft: layout, facts, sequence, visuals, accessibility and speaker notes still require expert review.

A document-to-deck workflow can preserve the approved narrative while reducing assembly time. However, a slide is not a paragraph pasted onto a canvas. Each slide needs one message, visible evidence and a role in the story; decorative images must not imply facts that the source does not support.

**How it works**

- Approve and save the source document in OneDrive or SharePoint before starting the presentation.
- Ask for a bounded slide count, named audience, decision-oriented sequence and required sections.
- Compare slide titles, claims, dates, owners and numbers with the Word source and source register.
- Refine one slide at a time, replacing generic text and inappropriate imagery with accurate content.
- Check reading order, alt text, contrast, speaker notes and the final call to action before sharing.

**Worked example**

- Copilot creates a six-slide Asteron launch deck from the approved Word brief.
- The generated risks slide omits the training dependency and uses a generic image unrelated to the pilot.
- The learner restores the missing risk, replaces the image with a simple milestone diagram and adds source notes.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A stable source document already contains the approved narrative and the deck needs a fast first structure. | The source file is unapproved, contradictory or too long to support a focused presentation. |
| The presenter can edit the result, check accessibility and rehearse the final story. | A generated image or slide could be mistaken for real operational evidence. |

**Practitioner quality lens**

- Story: One audience, one decision path and one message per slide.
- Evidence: Every factual slide traces to the approved source; visuals do not fabricate proof.
- Accessibility: Readable contrast, concise text, logical reading order and useful alternative text.

**Authoritative references**

- https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint
- https://support.microsoft.com/en-us/powerpoint/frequently-asked-questions-about-copilot-in-powerpoint
- https://support.microsoft.com/en-us/microsoft-365-copilot/prepare-your-presentation-with-microsoft-365-copilot

---


### Lab 1 — Research the Asteron Launch and Build a Verified Source Register

Learning outcome: LO1: use G-C-S-E to research a bounded source pack in Copilot Chat, trace material claims to evidence and record unresolved questions.

Goal: Create a source register and verified claim ledger that can safely govern the Word brief and every later Asteron artifact.

You will inspect three synthetic Asteron source files, register their purpose and status, then ask Copilot Chat to synthesise the launch facts. You will open the sources, verify dates, owners, decisions and open questions, and keep unsupported statements out of the approved ledger.

**What you'll build**

work-c027/C027-Asteron-Source-Register.xlsx with Sources, Claim_Ledger and Review_Log tables, plus work-c027/C027-Asteron-Verified-Claims.txt and a Reviewed release record   (Tools: Microsoft 365 Copilot Chat · Excel · asteron-project-brief.md · asteron-decision-log.csv · asteron-stakeholder-notes.md.)

**Prerequisites**

- Download the repository and keep every file in labs/assets together.
- Sign in to an eligible Microsoft 365 account and open Copilot Chat.
- Create work-c027 in an approved OneDrive location; use only the supplied synthetic Asteron sources.

**Step-by-step**

1. Open labs/assets/asteron-project-brief.md, asteron-decision-log.csv and asteron-stakeholder-notes.md. For each file, note its title, owner, effective date, purpose, governing facts and limitations. Do not ask Copilot to summarise the files yet.

   ```bash
   Required pre-read questions:
1. Which source governs the launch date?
2. Which source governs named decisions and owners?
3. Which notes are observations rather than approved decisions?
4. Which question remains unresolved?
   ```

2. Open labs/assets/asteron-source-register-template.csv in Excel and save it as work-c027/C027-Asteron-Source-Register.xlsx. Rename the first sheet Sources, format the data as table tblSources and enter one row per source. Add a second sheet named Claim_Ledger and copy in the headers from asteron-claim-ledger-template.csv as table tblClaims. Add a third sheet named Review_Log and copy asteron-review-log-template.csv as table tblReviewLog.

   ```bash
   Required tables:
tblSources: Source_ID | File | Owner | Effective_Date | Purpose | Governs | Limitation | Status
tblClaims: Claim_ID | Claim | Source_ID | Evidence | Confidence | Check | Reviewer_Note | Release_State
tblReviewLog: Artifact | Prompt | Sources_Used | Source_Coverage | Reviewer | Review_Date | Open_Question | Release_State | Next_Use
   ```

3. Attach or reference only the three files in the permitted source pack in Copilot Chat. Submit the G-C-S-E prompt below. If your experience cannot reference all three files, process one file at a time and record that limitation in Sources; do not imply that an unavailable source was used. Preserve each source's true authority and status; stakeholder notes remain working observations, not decisions.

   ```bash
   GOAL: Build a claim ledger for the Asteron client portal pilot launch.
CONTEXT: Department heads need confirmed dates, owners, decisions, dependencies and open questions.
SOURCE: Use only the attached project brief, decision log and stakeholder notes. Name the Source_ID for every row.
EXPECTATIONS: Return Claim_ID | Claim | Source_ID | Evidence | Confidence | Check. Use ISO dates. Do not turn a proposal into a decision. Mark contradictions and missing evidence as HOLD. Do not add web facts.
   ```

4. Copy the proposed rows into tblClaims. Open the governing source for each material date, number, owner and decision. Set Check to VERIFIED only when the source supports the statement. Use REVISE for a correctable wording issue and HOLD for an unresolved or unsupported statement.

   ```bash
   Material checks:
Launch date = 2026-08-18
Pilot scope = 20 internal participants across five departments
FAQ owner = Nisha Rao, due 2026-08-11
Data export owner = Leon Wu, current due date 2026-08-13
External announcement = not released before privacy sign-off
Support clinic date and room = proposed, not confirmed
   ```

5. Complete one row in tblReviewLog with the exact prompt, sources actually used, coverage, reviewer name, review date, remaining open question, release state and next use. Export only VERIFIED claim rows as plain text to work-c027/C027-Asteron-Verified-Claims.txt, including Claim_ID, Claim, Source_ID and Evidence. A source-supported claim may be explicitly labelled Confirmed, Proposed or Open; exclude all unsupported HOLD rows. Save the workbook and link both outputs in your work-c027 notes.

   ```bash
   Release record:
Artifact: C027-Asteron-Source-Register.xlsx
State: Reviewed
Open question: Is the 2026-08-19 support clinic room confirmed?
Next use: governing source for Lab 2 Word brief
   ```


**Test it**

tblSources must contain exactly three permitted sources with their true authority/status and no web source. tblClaims must include the six material checks with Source_ID and evidence. The 2026-08-13 data-export date must supersede 2026-08-12, and the support clinic must remain proposed. Every unsupported statement must be REVISE or HOLD. tblReviewLog must contain every required review field, and the TXT export must contain only VERIFIED claims, including source-supported Proposed/Open items with those labels and no unsupported HOLD rows. The final release state must be Reviewed, not Approved, because one room question remains open.

**Checkpoint and rejoin point**

Save the source register and verified-claims TXT in work-c027. Lab 2 references the supported TXT export and preserves the open support-clinic question. If you need to rejoin, use labs/assets/asteron-expected-facts.md to rebuild the ledger and TXT export.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot cannot reference one or more local files. | Save the files to an approved OneDrive location or process them one at a time. Record the actual source coverage and merge the ledgers manually; never claim a missing file was reviewed. |
| A generated claim has no traceable source. | Set Release_State to HOLD, add 'No governing evidence found' and exclude the claim from the Word brief. |
| Copilot treats the earlier 2026-08-12 export date as current. | Open the decision log, use the latest dated decision and record 2026-08-13 as current while noting the superseded date. |

**Challenge**

Ask Copilot to return a contradiction matrix by Source_ID. Verify it manually and explain why the latest dated statement is not automatically authoritative unless the source is allowed to govern that fact.

**Reflection**

Which prompt element made it easiest to detect an unsupported or superseded claim, and why?

> **Note:** The complete lab and its support-file references are in labs/lab-01-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Lab 2 — Draft and Approve the Asteron Launch Brief in Word

Learning outcome: LO2: draft a source-grounded business document in Word, apply a bounded rewrite and validate the final version against the source register and audience brief.

Goal: Produce an approved launch brief of no more than two pages whose facts, open questions and call to action agree with the verified source register.

You will create a Word document for Asteron department heads, use the supported verified-claims TXT export as the Copilot reference, then review the generated draft against the source register and project brief line by line. You will use Copilot to rewrite one selected passage without changing scope, commitments or unresolved items.

**What you'll build**

work-c027/C027-Asteron-Launch-Brief-v1.0.docx with five required sections, source notes, an Open Questions box and an Approved for deck handoff record   (Tools: Word for Microsoft 365 · Copilot in Word · C027-Asteron-Verified-Claims.txt · C027-Asteron-Source-Register.xlsx.)

**Prerequisites**

- Completed Lab 1 workbook and C027-Asteron-Verified-Claims.txt export.
- Open labs/assets/asteron-word-brief-spec.md and labs/assets/asteron-style-guide.md.
- Keep the support-clinic room as an open question; no source approves it.
- For this simulation, the learner is the document owner and supplies the owner review; trainer feedback may supplement it.

**Step-by-step**

1. Create a blank Word document in work-c027 and save it as C027-Asteron-Launch-Brief-v1.0.docx. Add a title, document owner, version, date and a status line set to Draft. Insert the five required headings from the brief specification before generating any body text.

   ```bash
   Required headings:
1. Purpose and Audience
2. Confirmed Launch Position
3. Readiness and Dependencies
4. Decisions and Owners
5. Open Questions and Next Actions
   ```

2. Open Copilot in Word and reference C027-Asteron-Verified-Claims.txt from Lab 1. Submit the prompt below. Word's referenced drafting accepts this supported TXT handoff; do not cite the Excel workbook as if Copilot in Word read it. Use the workbook and project brief for the manual source review in Step 3.

   ```bash
   GOAL: Draft an Asteron client portal pilot launch brief of no more than two pages.
CONTEXT: Department heads need the confirmed position, named owners and decisions needed before 2026-08-18.
SOURCE: Use only the referenced C027-Asteron-Verified-Claims.txt export. Preserve items explicitly labelled Proposed or Open; the export contains no unsupported HOLD rows.
EXPECTATIONS: Use the five existing headings, concise professional language, bullets for owners, ISO dates, and source notes in [Source_ID] form. Do not add market claims or present proposals as confirmed.
   ```

3. Review the draft against the source register. Highlight every date, number, owner and commitment. Add a Word comment containing the governing Source_ID, then set the review decision to Keep, Change or Remove. Correct any unsupported language before continuing.

   ```bash
   Required trace points:
2026-08-18 launch date
20 internal participants
five departments
Nisha Rao / FAQ / 2026-08-11
Leon Wu / export / 2026-08-13
privacy sign-off before external announcement
   ```

4. Select the Readiness and Dependencies section only. Ask Copilot to make it more concise for senior leaders while preserving every fact and the distinction between confirmed and proposed. Compare the before and after text and reject any change to scope, date, owner or status.

   ```bash
   Rewrite this selected section to no more than 90 words for department heads. Preserve all dates, owners, scope and status labels exactly. Keep the support clinic room as an open question. Do not introduce new commitments.
   ```

5. Insert a two-column release table at the end with Check and Result. Complete Source fidelity, Audience fit, Scope, Open questions, Privacy, Accessibility and Owner approval. As the lab document owner, enter your name and review date for Owner approval. Change the document status to Approved for deck handoff only when all required checks are complete; this is a simulated workflow state, not organisational approval. Save and close the file.

   ```bash
   Release states:
APPROVED = evidence and audience checks complete
REVISE = correctable content or format gap
HOLD = unsupported fact, unsafe disclosure or unresolved release decision
   ```


**Test it**

The Word file must contain exactly the five required headings and remain within two pages including the release table. Every material date, number, owner and commitment must trace to a Source_ID. The launch date must be 2026-08-18, the data export 2026-08-13 and the support-clinic room must remain open. The title block must show v1.0 and Approved for deck handoff.

**Checkpoint and rejoin point**

Save the approved Word brief in work-c027. Lab 3 uses this exact version as the governing PowerPoint source. If the status is REVISE or HOLD, correct the document before continuing.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot changes a confirmed fact during rewrite. | Reject the rewrite, narrow the selected text and state which terms, dates and statuses must remain exact. |
| The document is longer than two pages. | Remove duplication, convert owner details to a compact table and shorten explanation without removing evidence or open questions. |
| A source note points to the wrong file. | Return to tblClaims, identify the governing Source_ID and correct both the note and any affected wording. |

**Challenge**

Ask Copilot in Chat-only mode to pressure-test the brief from a department head's perspective. Add only questions that expose a genuine evidence gap; do not let speculative questions become new facts.

**Reflection**

What is the difference between improving a sentence and changing the commitment expressed by that sentence?

> **Note:** The complete lab and its support-file references are in labs/lab-02-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Lab 3 — Generate and Refine the Asteron Decision Deck in PowerPoint

Learning outcome: LO2: generate a presentation from an approved Word source, refine the narrative and verify facts, visuals, accessibility and speaker notes before use.

Goal: Create a concise six-slide decision deck that preserves the approved Word brief and makes the remaining decision visible without inventing evidence.

You will use the approved Lab 2 Word brief to generate a PowerPoint draft for department heads. You will compare every factual slide with the source, replace generic or misleading content, refine one slide from a referenced file and complete an accessibility and release check.

**What you'll build**

work-c027/C027-Asteron-Decision-Deck-v1.0.pptx with six decision-oriented slides, concise speaker notes, source notes and a Reviewed for internal presentation status   (Tools: PowerPoint for Microsoft 365 · Copilot in PowerPoint · C027-Asteron-Launch-Brief-v1.0.docx.)

**Prerequisites**

- Lab 2 Word brief is saved in OneDrive and marked Approved for deck handoff.
- Open labs/assets/asteron-deck-spec.md and keep the Lab 1 source register available.
- Use only synthetic Asteron files and approved built-in or licensed visual assets.

**Step-by-step**

1. Open PowerPoint, start a new presentation and use Copilot to create a presentation from C027-Asteron-Launch-Brief-v1.0.docx. Request exactly six slides for department heads. Save the result immediately as work-c027/C027-Asteron-Decision-Deck-v1.0.pptx.

   ```bash
   Create a six-slide internal decision presentation from the referenced approved Word brief. Use concise titles, one message per slide and speaker notes. Do not add facts not present in the source.
   ```

2. Compare the generated structure with the deck specification. Rename, reorder, add or remove slides until the sequence is exactly: decision, scope, readiness, timeline, risks and next actions. Keep the support-clinic room visibly unresolved. Because verified numerical readiness measures are not created until Lab 4, slide 3 must show dependencies and status only; add no readiness numbers in this lab.

   ```bash
   Required sequence:
1. Decision needed
2. Pilot scope
3. Readiness snapshot
4. Timeline and owners
5. Risks and open question
6. Next actions
   ```

3. For slides 2-6, compare every date, number, owner and status with the Word brief and source register. Add a small source note in the speaker notes using Source_ID values. Remove or rewrite any content that cannot be traced.

   ```bash
   Required facts:
20 internal participants · five departments · 2026-08-18 launch
Nisha Rao / 2026-08-11 · Leon Wu / 2026-08-13
external announcement waits for privacy sign-off
support clinic room remains open
   ```

4. Refine slide 4 by asking Copilot to rewrite the existing timeline. If Copilot creates a new timeline slide, move it into position 4 and delete the superseded slide so the deck remains exactly six slides. Keep four milestones only. Replace decorative imagery that could be mistaken for real Asteron evidence with a simple editable timeline or icon-based process.

   ```bash
   Create a four-milestone timeline from the referenced brief: FAQ due 2026-08-11; data export due 2026-08-13; privacy sign-off before external announcement; pilot launch 2026-08-18. Do not add a confirmed support-clinic milestone.
   ```

5. Run Review > Check Accessibility in PowerPoint. Resolve each fixable issue and record the Accessibility Checker result, including any accepted limitation, in the final notes. Then confirm a single message per slide, readable text, strong contrast, logical reading order, meaningful alternative text, concise speaker notes and no unsupported image. In the file properties or final notes, record status Reviewed for internal presentation, reviewer and date.

   ```bash
   Release check:
Story | Facts | Visual evidence | Accessibility | Speaker notes | Audience | Reviewer | State
   ```


**Test it**

The deck must contain exactly six slides in the required sequence. All repeated facts must match the approved Word brief, slide 3 must show dependencies/status without numerical readiness measures, slide 4 must contain only the four approved milestones, and no visual may imply real customer evidence. Each factual slide must have a Source_ID note. The final notes must record the Accessibility Checker result, and the final state must be Reviewed for internal presentation.

**Checkpoint and rejoin point**

Save and close the six-slide deck. Labs 7 and 8 will check it against the other app outputs. Keep the approved Word brief unchanged as the governing narrative source.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Create from file is unavailable or the Word file is not listed. | Confirm the file is saved to OneDrive, the correct account is active and Copilot is enabled. If necessary, create the six-slide structure manually and use Copilot to draft one slide at a time from the brief. |
| Copilot creates more or fewer than six slides. | Keep only the required sequence and merge duplicate content. Do not add slides merely to preserve generated text. |
| A generated image is irrelevant or misleading. | Remove it and use an editable shape, icon or timeline that communicates structure without pretending to be evidence. |

**Challenge**

Use Copilot to propose two alternative titles for slide 1: one neutral and one action-oriented. Choose the title that best reflects the actual decision without overstating urgency or certainty.

**Reflection**

Which part of the Word brief required the greatest transformation to work as a slide, and what had to remain unchanged?

> **Note:** The complete lab and its support-file references are in labs/lab-03-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Topic 01 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO1 - Ground and Prompt | Distinguish prompt instructions from grounding sources, use Goal-Context-Source-Expectations, and trace every factual statement in a Copilot Chat summary to an approved source. |
| LO2 - Write and Present | Use Word to draft and rewrite against an audience brief, approve the document before handoff, and use that approved file as the source for a concise PowerPoint presentation. |

---


## Topic 02 — Copilot Across Your Everyday Work Apps  (Second half · 5 connected labs)

Excel analysis and formulas · Outlook email work · Teams recaps · end-to-end app workflows · responsible AI and data privacy

**Key concepts**

- Bounded Excel analysis — Name the table, columns, filters, units and expected checks before asking for a formula or insight.
- Thread-to-response control — Separate facts extracted from an Outlook thread from the generated wording of a draft reply.
- Transcript-backed actions — A Teams recap is useful only when owners, due dates and decisions agree with the meeting evidence.
- Handoff contracts — Each app passes an approved artifact, source note, owner and verification status to the next app.
- Permissions are the perimeter — Copilot honours the user's access; overshared content therefore remains an organisational risk.
- Human release gate — Generated content stays in Draft or Hold until a named person checks evidence, sensitivity and audience.


### Analysing Data and Generating Formulas in Excel

Copilot in Excel can help analyse table-like data, surface summaries, trends and outliers, generate or explain formulas, and create editable workbook elements such as tables, PivotTables and charts in supported experiences. Some analytical responses may be static. The user must understand the grain, data types, filters and calculation logic before relying on the output.

A plausible formula can still use the wrong denominator, sign, date boundary or blank-value rule. Excel makes generated logic inspectable, so the masterclass pairs every Copilot action with an independent control: row count, formula sample, reconciliation total and edge-case review.

**How it works**

- Save the workbook to an approved cloud location, keep the raw data unchanged and convert the bounded range into a named table.
- State the row grain, business question, named columns, filters, units and required output.
- Ask Copilot to propose or explain the formula before applying it; inspect structured references and fill behaviour.
- Recalculate control totals using an independent method and sample normal, blank and boundary rows.
- Label generated insights as Observed, Hypothesis or Unknown and record the checked workbook version.

**Worked example**

- Asteron needs confirmed attendance rate and follow-up priority for a 20-person pilot cohort.
- Copilot proposes a rate formula, but the learner notices blank attendance values are included in the denominator.
- The learner revises the rule, checks three edge rows and ties the summary counts to the raw table.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The data is tabular, the requested calculation is explicit and the workbook can retain visible controls. | The dataset has undefined grain, mixed meanings or unresolved quality problems. |
| The user can inspect formulas, PivotTables, charts or generated analytical logic. | A static generated visual would be mistaken for a refreshable workbook result. |

**Practitioner quality lens**

- Boundary: Name the table, columns, date range, filters, units and exclusions.
- Logic: Inspect formula, aggregation and missing-value rules rather than accepting the label.
- Tie-out: Reconcile counts and totals independently before interpreting patterns.

**Authoritative references**

- https://support.microsoft.com/en-us/excel/copilot/data-insights-with-copilot-in-excel
- https://support.microsoft.com/en-us/office/edit-with-copilot-in-excel-a2fd6fe4-97ac-416b-b89a-22f4d1357c7a
- https://support.microsoft.com/en-us/excel/get-direct-answers-to-your-data-analysis-questions

---


### Drafting Emails and Summarising Threads in Outlook

Copilot in Outlook can summarise email threads, draft messages from a prompt and thread context, offer coaching on tone and clarity, and help prepare for meetings in eligible experiences. Feature availability varies by licence, client and policy. Signed, encrypted, rights-managed or some labelled messages can have additional limitations.

Email combines factual history with a consequential communication act. A safe workflow first extracts decisions, requests, owners and dates from the thread, then drafts a reply that does not invent agreement. The sender verifies recipients, attachments, sensitivity, commitments and tone before sending.

**How it works**

- Open the bounded synthetic thread and ask for decisions, action items, open questions and conflicting statements.
- Compare the summary with each message and correct owner, date, number and status errors.
- Draft a response with explicit audience, purpose, tone, commitments and items that must remain unresolved.
- Use coaching to review clarity and tone without allowing a rewrite to change factual meaning.
- Check To, Cc, attachments, links, sensitivity and every commitment; keep the message as a draft until approved.

**Worked example**

- The Asteron thread contains two proposed training dates but only one confirmed room booking.
- Copilot's first draft presents both dates as final. The learner restores the distinction and asks the facilities owner to confirm.
- The message remains in Draft and its facts are compared with the decision log before any send action.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A bounded thread needs a catch-up summary, response outline or tone review. | The thread includes highly sensitive content not suitable for the intended audience or unsupported client experience. |
| The sender can inspect the complete thread and owns the final recipient and send decisions. | The generated draft would create a commitment that no authorised person has approved. |

**Practitioner quality lens**

- Facts: Separate thread evidence from generated wording and preserve unresolved items.
- Recipients: Recheck To, Cc, attachments and audience before release.
- Commitments: Do not turn proposals, questions or estimates into promises.

**Authoritative references**

- https://support.microsoft.com/en-us/outlook/frequently-asked-questions-about-copilot-in-outlook
- https://support.microsoft.com/en-us/office/frequently-asked-questions-about-copilot-in-outlook-07420c70-099e-4552-8522-7d426712917b

---


### Meeting Recaps and Action Items in Teams

Copilot and intelligent recap in Teams can use a meeting transcript, chat and supported event content to summarise key points, decisions and follow-up tasks. Recap features depend on the event type, licence, recording or transcription settings, language and organisational policy. A recap is generated evidence aid, not a replacement for the governing transcript or a confirmed action register.

Meeting summaries compress fast-moving conversation, but transcription errors and ambiguous speech can misassign an owner or due date. A strong action register requires an action verb, deliverable, named owner, ISO date, status and a transcript reference; unresolved statements stay open.

**How it works**

- Obtain consent and follow organisational policy before recording or transcription; use the supplied synthetic transcript when live transcription is unavailable.
- Ask for decisions, action items, blockers and open questions in separate sections.
- Compare each item with the transcript or chat and correct speaker attribution, negation, numbers and dates.
- Convert confirmed actions into a register with owner, deliverable, due date, evidence and status.
- Share the reviewed register only with the intended participants and retain open questions visibly.

**Worked example**

- A speaker says the FAQ draft is due Friday, but the room booking will be confirmed next Monday.
- The generated recap assigns both items to the same owner and date.
- The learner checks the transcript, corrects the two records and labels the room decision Open.

**Decision guide**

| Use when | Avoid when |
|---|---|
| A permitted transcript or meeting chat exists and the participants need a faster first recap. | Recording or transcription is not permitted, participants have not been informed or sensitive discussion needs special handling. |
| A person who attended can validate decisions, owners and due dates before circulation. | The recap will be treated as final minutes without comparison to the meeting evidence. |

**Practitioner quality lens**

- Consent: Follow policy and participant expectations for recording, transcription and sharing.
- Evidence: Link actions and decisions to transcript language or chat context.
- Ownership: Every confirmed action has one owner, one deliverable and one due date.

**Authoritative references**

- https://support.microsoft.com/en-us/teams/meetings-events/recap-a-teams-meeting
- https://support.microsoft.com/en-us/teams/meetings/recap-in-microsoft-teams
- https://support.microsoft.com/en-us/teams/copilot/how-to-use-microsoft-365-copilot-in-teams-chats-and-channels

---


### Building End-to-End Copilot Workflows Across Apps

An end-to-end Copilot workflow connects approved outputs across apps without losing source boundaries, ownership or review status. The key is a handoff contract: every transition names the source artifact, approved version, intended destination, required transformation, constraints, owner and verification gate.

Cross-app speed can multiply an early error. If an unverified chat summary becomes a Word brief, then a deck, email and meeting plan, one wrong date appears everywhere. Checkpointed handoffs contain the blast radius: downstream apps receive only approved artifacts and changes are reconciled back to the source register.

**How it works**

- Map the workflow from source evidence to Chat synthesis, Word brief, PowerPoint deck, Excel analysis, Outlook draft and Teams actions.
- Define a release state for each artifact: Draft, Reviewed, Approved or Hold.
- At each handoff, name the file and version, destination, allowed transformation and facts that must not change.
- Run a consistency check for titles, dates, numbers, owners, terminology and audience across every artifact.
- Record the final owner and next action; keep links rather than duplicating uncontrolled copies where possible.

**Worked example**

- The approved Asteron Word brief supplies the story for PowerPoint, while Excel supplies verified attendance figures.
- The Outlook draft and Teams action register use links to those artifacts and repeat only the minimum confirmed facts.
- A cross-app check detects that one slide uses an earlier launch date; the learner corrects it before the pack is released.

**Decision guide**

| Use when | Avoid when |
|---|---|
| Several apps contribute distinct strengths and each handoff can be checkpointed. | The workflow copies unapproved chat text from app to app or obscures which file is authoritative. |
| A named owner can reconcile downstream outputs to the governing sources. | Automation would send, publish or schedule consequential output without a human release gate. |

**Practitioner quality lens**

- Authority: Declare which artifact governs each fact, number and commitment.
- State: Show Draft, Reviewed, Approved or Hold at every handoff.
- Consistency: Reconcile titles, dates, owners, measures and audience across the full pack.

**Authoritative references**

- https://support.microsoft.com/en-us/microsoft-365-copilot/
- https://support.microsoft.com/en-us/office/365-copilot-app/get-started-with-word-excel-and-powerpoint-agents-in-microsoft-365-copilot

---


### Responsible AI, Data Privacy and Best Practices

Responsible use of Microsoft 365 Copilot combines technical protections with human judgment. For organisational use, enterprise data protection applies to prompts and responses, Microsoft 365 permissions continue to govern accessible work data, and interactions can be retained for audit and compliance. These protections do not correct oversharing, weak sources or inaccurate generated content.

Copilot can accelerate existing good practice and expose existing information-governance weaknesses. A user who can access an overshared file may receive it in grounded results. Responsible practice therefore uses least privilege, sensitivity and sharing controls, minimal necessary data, source verification, transparent AI use where appropriate and named human accountability.

**How it works**

- Confirm identity, licence, organisational policy, approved app and the minimum data necessary for the task.
- Check file permissions, sharing links, labels and audience before referencing or publishing content.
- Do not place credentials, secrets or unnecessary sensitive personal information in prompts.
- Review outputs for factual error, harmful bias, privacy exposure, unsupported inference and inappropriate tone.
- Record sources, meaningful AI assistance, reviewer, release decision and unresolved limitations.

**Worked example**

- A Copilot search surfaces an old broadly shared roster with personal contact details.
- The learner does not use or reproduce the roster, reports the oversharing through the organisation's process and uses the synthetic cohort file instead.
- The final pack records its sources, reviewer and Approved state without exposing unnecessary personal information.

**Decision guide**

| Use when | Avoid when |
|---|---|
| The task uses authorised data, proportionate controls and a reviewer who understands the decision context. | The prompt would expose secrets, bypass access controls, profile people unfairly or conceal an unsupported decision. |
| The organisation's retention, sensitivity, sharing and acceptable-use requirements are known. | The user cannot identify who is accountable for checking and releasing the output. |

**Practitioner quality lens**

- Minimise: Use only the data and detail necessary for the declared purpose.
- Protect: Apply permissions, labels, sharing and retention controls appropriate to the source.
- Account: Name the reviewer, sources, limitations and release decision.

**Authoritative references**

- https://learn.microsoft.com/en-us/copilot/faq
- https://learn.microsoft.com/en-us/microsoft-365/copilot/security-microsoft-365-copilot
- https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-architecture-data-protection-auditing
- https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy

---


### Lab 4 — Analyse Pilot Readiness and Verify Copilot Formulas in Excel

Learning outcome: LO3: analyse a bounded Excel table, generate formula columns and reconcile every headline measure to independent controls.

Goal: Create a verified readiness workbook with explicit grain, inspectable formulas, control totals and a short evidence-backed management summary.

You will import a 20-row synthetic pilot cohort, preserve the raw source and ask Copilot to create a priority formula and readiness summary. You will inspect the logic, correct denominator rules and reconcile counts, rates and averages before writing three decision-relevant observations.

**What you'll build**

work-c027/C027-Asteron-Pilot-Readiness.xlsx with Raw_Cohort, Analysis, Control and Prompt_Log sheets, a verified priority column and an Approved internal readiness summary, plus work-c027/C027-Asteron-Verified-Readiness-Summary.txt   (Tools: Excel for Microsoft 365 · Copilot in Excel · asteron-pilot-readiness.csv.)

**Prerequisites**

- Download labs/assets/asteron-pilot-readiness.csv and asteron-excel-controls.md.
- Sign in to Excel with Copilot available; record the actual experience label if it differs.
- Use the supplied synthetic cohort only and keep the original CSV unchanged.

**Step-by-step**

1. Open asteron-pilot-readiness.csv in Excel and save it as work-c027/C027-Asteron-Pilot-Readiness.xlsx. Rename the first sheet Raw_Cohort. Copy the sheet to Analysis, format the data as table tblReadiness and create empty Control and Prompt_Log sheets.

   ```bash
   Grain: one row = one synthetic pilot participant
Key: Participant_ID
Raw_Cohort must remain unchanged
Working table: tblReadiness
   ```

2. On Control, enter these metric labels in A2:A10 and exact formulas in B2:B10. State that attendance rate uses Confirmed registrations as its denominator and counts only Attended as its numerator.

   ```bash
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

3. Ask Copilot to add a Priority column using the rule below. Require a formula explanation before applying it. Inspect the structured references and verify rows P004, P008, P010, P015 and P017. Non-confirmed rows must be Not in cohort rather than High.

   ```bash
   GOAL: Add an editable Priority column to tblReadiness.
CONTEXT: Asteron uses the column to plan support for confirmed pilot participants.
SOURCE: Use Registration_Status, Training_Complete, Readiness_Score and Support_Tickets in tblReadiness only.
EXPECTATIONS: If Registration_Status is not Confirmed, return 'Not in cohort'. Otherwise return 'High' when Training_Complete is No OR Readiness_Score is below 70 OR Support_Tickets is 2 or more; else 'Standard'. Explain the formula, then apply it without changing Raw_Cohort.
   ```

4. Ask Copilot for a summary table of confirmed participants by Department with count, attended count, training-complete count, average readiness and support tickets. Build an independent PivotTable from tblReadiness filtered to Confirmed and reconcile every department row—not only the grand total—against labs/assets/asteron-department-controls.csv. Do not accept a summary whose denominator includes Waitlist or Withdrawn rows.

   ```bash
   Summarise confirmed participants in tblReadiness by Department. Return Count, Attended, Training_Complete, Average_Readiness and Support_Tickets. Include grand totals and state the filters and denominator.
   ```

5. Write three observations in a Summary area: one about attendance, one about training completion and one about high-priority support. Label each OBSERVED and cite the control cells. Add a Limitations line noting that readiness scores are synthetic and do not prove future performance. Record prompt, formula, checks and release decision in Prompt_Log. Export the verified headline measures as plain text to work-c027/C027-Asteron-Verified-Readiness-Summary.txt for the supported Copilot Chat handoff in Lab 7.

   ```bash
   Required summary facts:
Attendance = 14 of 16 confirmed (87.5%)
Training complete = 12 of 16 confirmed (75.0%)
High priority = 4 confirmed participants: P004, P008, P010, P015
Release state = Approved for internal workflow lab
   ```


**Test it**

Raw_Cohort must match the CSV and tblReadiness must contain 20 rows with 20 unique IDs. Control values must match asteron-excel-controls.md exactly. Priority must show High only for P004, P008, P010 and P015 among confirmed participants, and Not in cohort for P017-P020. Every department row and the grand total must tie to asteron-department-controls.csv, every summary sentence must cite a control cell, and the verified TXT export must contain the three headline measures.

**Checkpoint and rejoin point**

Save the approved readiness workbook and verified-readiness TXT. Lab 7 uses the supported TXT export for its three verified headline measures. If any tie-out fails, keep the workbook in REVISE and do not copy its numbers to another app.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Copilot uses all 20 rows as the attendance denominator. | Restate the Confirmed filter explicitly and compare the formula with COUNTIF(tblReadiness[Registration_Status],"Confirmed"). |
| Priority marks waitlisted or withdrawn rows High. | Place the Registration_Status condition first so non-confirmed rows return Not in cohort before other tests. |
| The average differs from 80.0625. | Check that AVERAGEIF uses Confirmed as the criterion and Readiness_Score as the average range; do not round before reconciliation. |

**Challenge**

Create a PivotTable of confirmed participants by Department and Preferred_Session. Reconcile the grand total to 16 and explain why the table supports capacity planning but not employee performance decisions.

**Reflection**

Which denominator choice most changed the meaning of a readiness measure, and how did you make it visible?

> **Note:** The complete lab and its support-file references are in labs/lab-04-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Lab 5 — Summarise the Launch Thread and Prepare a Reviewed Outlook Draft

Learning outcome: LO3: summarise a bounded Outlook thread, distinguish confirmed facts from proposals and prepare a reviewed email draft without creating unsupported commitments.

Goal: Produce a fact-checked launch update draft whose recipients, dates, owners, attachments and unresolved items are explicitly reviewed before any send action.

You will create a private synthetic email thread in your own mailbox from the supplied messages, use Copilot to summarise decisions and open questions, then draft a concise internal update. You will verify the thread facts and leave the message unsent for the cross-app review.

**What you'll build**

An Outlook draft titled [DRAFT] Asteron pilot launch update - review required, plus work-c027/C027-Outlook-Thread-Review.md with the verified facts and release checklist   (Tools: Outlook for Microsoft 365 · Copilot in Outlook · asteron-email-thread.md.)

**Prerequisites**

- Use only your own training mailbox or a trainer-approved sandbox mailbox.
- Open labs/assets/asteron-email-thread.md and asteron-outlook-review-template.md.
- Copy asteron-outlook-review-template.md to work-c027/C027-Outlook-Thread-Review.md before writing into it.
- Do not send the final update; the required outcome is a reviewed draft.

**Step-by-step**

1. Create the synthetic thread in your own mailbox. Send Message 1 from asteron-email-thread.md to yourself with subject Asteron pilot launch coordination - synthetic. Paste each supplied message in full, including its synthetic From and Date labels inside the message body. Reply to the same thread with Messages 2 and 3, still addressed only to yourself. Confirm the three messages appear as one thread. For project history, the embedded synthetic labels govern; your real self-send transport metadata records only when the exercise copy was created.

   ```bash
   Safety boundary:
Recipient = your own training address only
Subject contains 'synthetic'
No real client, colleague or external address
Use only the supplied message text
   ```

2. Use Summary by Copilot or Copilot Chat in Outlook on the thread. Ask for confirmed decisions, current owners and due dates, superseded information, proposals and open questions in separate sections. Copy the result into work-c027/C027-Outlook-Thread-Review.md.

   ```bash
   Summarise this synthetic thread as Confirmed decisions | Owners and current due dates | Superseded information | Proposals | Open questions. Use ISO dates and quote the message date for each item. Do not convert a proposal or pending approval into a commitment.
   ```

3. Compare the summary with all three messages. Correct the data-export due date to 2026-08-13, keep the 2026-08-19 support clinic and room as proposed, and retain the privacy sign-off dependency before any external announcement. Record VERIFIED, REVISE or HOLD beside every item.

   ```bash
   Expected distinctions:
FAQ / Nisha Rao / 2026-08-11 = confirmed
Data export / Leon Wu / 2026-08-13 = current; 2026-08-12 superseded
Support clinic / 2026-08-19 14:00 = proposed; room pending
External announcement = HOLD until privacy sign-off
   ```

4. Use Draft with Copilot to create an internal response. Address it only to yourself, prefix the subject with [DRAFT], and require sections for Confirmed, Needs confirmation and Actions. Use coaching to review clarity and tone, but reject any suggestion that changes a fact or commitment.

   ```bash
   Draft a concise internal launch update from this verified thread. Separate Confirmed, Needs confirmation and Actions. Preserve current owners and ISO dates. Ask for room confirmation; do not announce externally. Professional, neutral tone, under 180 words. Keep the message in Draft.
   ```

5. Complete the Outlook release checklist in C027-Outlook-Thread-Review.md: To, Cc, subject, facts, commitments, attachments, links, sensitivity, tone and send decision. Save the draft without sending it. Set the release state to HOLD - pending Lab 7 cross-app consistency review.

   ```bash
   Required send decision: DO NOT SEND
Required state: HOLD - cross-app review pending
Attachments: none
Recipients: self only
   ```


**Test it**

The mailbox must contain a three-message synthetic self-thread and one unsent draft. The review file must exist in work-c027, state that embedded synthetic sender/date labels govern project history, show 2026-08-13 as the current export date, keep the support clinic proposed and hold external announcement until privacy sign-off. The final draft must be under 180 words, addressed only to self, contain no attachment and remain HOLD - cross-app review pending.

**Checkpoint and rejoin point**

Leave the email in Draft and save C027-Outlook-Thread-Review.md. Lab 7 compares this draft with the Word brief, PowerPoint deck, Excel workbook and Teams action register.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| Outlook does not group the three messages. | Use Reply on the first self-message for Messages 2 and 3 and keep the subject unchanged. |
| Summary by Copilot is unavailable. | Use Copilot Chat in Outlook with the selected synthetic thread if supported. Otherwise use Copilot Chat with asteron-email-thread.md and record that the Outlook summary capability was unavailable. |
| Coaching recommends stronger commitment language. | Keep the verified status. Tone advice never overrides evidence or approval state. |

**Challenge**

Create a second version for an executive reader in no more than 90 words. Compare which details can be removed without hiding an owner, due date, dependency or unresolved decision.

**Reflection**

Why must thread extraction and reply drafting be reviewed as two separate stages?

> **Note:** The complete lab and its support-file references are in labs/lab-05-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Lab 6 — Validate a Teams Recap and Create the Action Register

Learning outcome: LO4: validate a Teams recap against transcript evidence and convert confirmed follow-up work into an action register with owners, due dates and release status.

Goal: Create a transcript-backed action register that distinguishes decisions, actions, proposals and open questions.

You will use a trainer-provided synthetic Teams meeting recap or the supplied transcript in Copilot Chat inside Teams. You will compare generated decisions and actions with the evidence, correct attribution and dates, and create a durable action register for the cross-app workflow.

**What you'll build**

work-c027/C027-Teams-Action-Register.xlsx with Decisions, Actions, Proposals and Open_Questions sheets, transcript references and a Reviewed internal coordination state, plus work-c027/C027-Asteron-Verified-Actions.txt   (Tools: Microsoft Teams · Copilot or intelligent recap · asteron-teams-transcript.md · Excel.)

**Prerequisites**

- Use the trainer-provided Asteron synthetic meeting if available; follow organisational policy for transcription.
- If a live recap is unavailable, open asteron-teams-transcript.md in Copilot Chat within Teams and record the fallback.
- Open labs/assets/asteron-action-register-template.csv and asteron-teams-register-schemas.md.

**Step-by-step**

1. Open the trainer-provided Asteron launch stand-up in Teams and select Recap and Copilot when available. If no permitted recap exists, upload or reference asteron-teams-transcript.md in Copilot Chat inside Teams. Record which path you used and the source date.

   ```bash
   Evidence path:
A = Teams recap from permitted synthetic meeting
B = Supplied synthetic transcript in Copilot Chat inside Teams
Never claim A when you used B
   ```

2. Ask Copilot to return four separate sections: Decisions, Actions, Proposals and Open questions. For Actions require Owner, Deliverable, Due_Date and Transcript_Evidence. Do not ask for a blended summary.

   ```bash
   Using only this meeting evidence, return Decisions | Actions | Proposals | Open questions. For each action give one named owner, one deliverable, one ISO due date and the exact transcript line or timestamp. Do not infer ownership or dates.
   ```

3. Open the transcript and verify every generated row. Correct the privacy sign-off owner, distinguish the proposed support clinic from confirmed launch work, and keep the room question open. Mark any row without exact evidence HOLD.

   ```bash
   Required evidence:
Nisha Rao - FAQ - 2026-08-11
Leon Wu - data export - 2026-08-13
Priya Menon - readiness dashboard - 2026-08-14 12:00
Farah Lim - privacy sign-off - 2026-08-15
Mei Tan - confirm support-clinic room - 2026-08-12
Pilot launch remains 2026-08-18 subject to privacy sign-off
   ```

4. Open asteron-action-register-template.csv in Excel and save as C027-Teams-Action-Register.xlsx. Create tables tblDecisions, tblActions, tblProposals and tblOpenQuestions on the four separate sheets specified in asteron-teams-register-schemas.md. Copy only verified rows, retain the evidence reference and set Status to Confirmed, Proposed or Open.

   ```bash
   Decisions: Decision_ID | Decision | Evidence | Status | Reviewer | Release_State
Actions: Action_ID | Deliverable | Owner | Due_Date | Evidence | Status | Reviewer | Release_State
Proposals: Proposal_ID | Proposal | Proposed_By | Target_Date | Evidence | Resolution_Owner | Status
Open Questions: Question_ID | Question | Resolution_Owner | Due_Date | Evidence | Status
   ```

5. Run a completeness check: every Confirmed action has one owner, one deliverable, one due date and evidence; Proposed items are not in the confirmed count; Open questions have an owner for resolution. Record reviewer, review date and state Reviewed for internal coordination. Export the confirmed action rows with owner, deliverable, due date and evidence to work-c027/C027-Asteron-Verified-Actions.txt for Lab 7.

   ```bash
   Expected confirmed work items = 5
Expected unresolved item = support-clinic room availability
Release state = Reviewed for internal coordination
   ```


**Test it**

The register must contain all four required sheets/tables, the five required work items with exact owners and dates, plus one proposed clinic and one open room question. Every confirmed action must include transcript evidence, and the file must record whether the source was a Teams recap or the supplied transcript fallback. The release state must be Reviewed for internal coordination, and the verified-actions TXT export must contain only confirmed actions.

**Checkpoint and rejoin point**

Save the action register and verified-actions TXT in work-c027. Lab 7 uses the supported TXT export plus the open question. Do not remove the evidence column when copying information into another app.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| The recap assigns an action to the wrong speaker. | Use the transcript speaker label and surrounding lines; correct the owner and record the generated attribution as REVISE. |
| A due date is missing from the evidence. | Set the action to HOLD and create an open question for the owner instead of inventing a date. |
| The live meeting cannot be transcribed. | Use the supplied synthetic transcript inside Teams and record the fallback. Do not change tenant policy or record without permission. |

**Challenge**

Ask Copilot to identify two risks implied by the action register. Label them HYPOTHESIS and state which additional evidence would be required before they could become confirmed risks.

**Reflection**

Which recap error would have caused the greatest coordination cost if it had entered the action register?

> **Note:** The complete lab and its support-file references are in labs/lab-06-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Lab 7 — Assemble and Reconcile the Cross-App Coordination Pack

Learning outcome: LO4: connect approved outputs across Microsoft 365 apps using handoff contracts and reconcile repeated facts, owners, measures and release states.

Goal: Create a cross-app manifest and concise coordination pack in which every repeated fact agrees with the governing artifact.

You will register the Chat, Word, PowerPoint, Excel, Outlook and Teams outputs, declare which artifact governs each type of information, then use Copilot to draft a coordination update. A consistency matrix will expose any date, owner, number or status that drifted during an app handoff.

**What you'll build**

work-c027/C027-Asteron-Cross-App-Manifest.xlsx and C027-Asteron-Coordination-Pack.docx with authoritative-source links, a consistency matrix and an Approved internal handoff state   (Tools: Microsoft 365 Copilot Chat · Word · Excel · PowerPoint · Outlook · Teams.)

**Prerequisites**

- Labs 1-6 outputs are saved in work-c027 with their stated release records; if one is unavailable, use the versioned trainer-validated labs/assets/asteron-capstone-rejoin-pack.txt and record the substitution.
- Do not use an artifact that remains REVISE; HOLD artifacts can be registered but cannot govern released facts.
- Open the partially populated asteron-cross-app-manifest-template.csv and asteron-consistency-matrix-template.csv.

**Step-by-step**

1. Open asteron-cross-app-manifest-template.csv in Excel and save as C027-Asteron-Cross-App-Manifest.xlsx. Enter one row for the source register, Word brief, PowerPoint deck, Excel readiness workbook, Outlook review and draft, and Teams action register. Record file link, version, owner, purpose, source authority, state and next use. Complete Source_Coverage as Learner-created checkpoint or Trainer-validated practice fallback. Timebox: 5 minutes; fill placeholders in the six pre-populated rows rather than rebuilding the table.

   ```bash
   Required artifacts = 6
Allowed states = Draft | Reviewed | Approved | Hold
No blank owner, purpose or next use
Outlook draft remains Hold
   ```

2. Create an Authority sheet. Declare that the source register governs confirmed launch facts, the Word brief governs the narrative, Excel governs cohort measures, Teams governs meeting actions and the Outlook thread governs email history. PowerPoint may communicate facts but does not replace its sources. Timebox: 5 minutes.

   ```bash
   Authority map:
Launch facts -> Source register
Narrative -> Approved Word brief
Readiness measures -> Verified Excel workbook
Meeting actions -> Teams action register
Email history -> Outlook thread review
   ```

3. In Microsoft 365 Copilot Chat, reference the approved Word brief, C027-Asteron-Verified-Readiness-Summary.txt and C027-Asteron-Verified-Actions.txt. If any normal input is missing, reference asteron-capstone-rejoin-pack.txt instead and name only the applicable WORD BRIEF, EXCEL READINESS or TEAMS substitute section. Ask for the bounded draft below; review it, then paste the accepted text into C027-Asteron-Coordination-Pack.docx with sections Executive position, Readiness, Confirmed actions, Open questions and Artifact links. Do not ask Copilot in Word to read Excel workbooks, and do not use the held Outlook draft as a factual source. Timebox: 12 minutes.

   ```bash
   GOAL: Draft a two-page internal coordination update.
CONTEXT: Asteron department heads need the launch position, readiness measures, actions and open questions.
SOURCE: Use the approved Word brief and the two referenced verified TXT exports only.
EXPECTATIONS: Preserve ISO dates and owners; cite the governing artifact after every section; distinguish Confirmed, Proposed and Open; include 14/16 attendance, 12/16 training completion and four high-priority participants.
   ```

4. Copy the nine pre-populated rows from asteron-consistency-matrix-template.csv into a Consistency sheet. Fill only the applicable artifact cells and compare the source register, Word brief, deck, Excel workbook, Outlook review, Teams register and coordination pack. Use N/A where a fact does not belong. Timebox: 15 minutes.

   ```bash
   Required consistency rows:
Launch 2026-08-18 | Cohort 20 / five departments
FAQ Nisha Rao / 2026-08-11 | Export Leon Wu / 2026-08-13
Privacy sign-off before external announcement | Clinic proposed / room open
Attendance 14/16 (87.5%) | Training 12/16 (75.0%) | High priority 4
   ```

5. Correct every mismatch in the downstream artifact, not in the governing source. Update the manifest with the reviewed version and state. In the coordination pack add a release table with Source coverage, Fact consistency, Permissions, Audience, Owner and Decision. Set the pack to Approved internal handoff only when all consistency rows agree. Timebox: 8 minutes.

   ```bash
   Final conditions:
Consistency_Result = MATCH for every required row
Coordination pack = Approved internal handoff
Outlook draft = Hold until Lab 8 release review
No artifact is marked Approved without a named reviewer
   ```


**Test it**

The manifest must contain six artifact rows with links, owners, versions and states. The authority map must name one governing artifact for each information type. Every required consistency row must show MATCH across all artifacts where the fact appears. The coordination pack must be no more than two pages, cite its source artifacts and be Approved internal handoff; the Outlook draft must remain Hold. Any substituted prior output must be visibly marked REJOIN-PACK-v1.0 and Trainer-validated practice fallback.

**Checkpoint and rejoin point**

Save the manifest and coordination pack. Lab 8 applies the final responsible-use and privacy review before the workflow is considered ready for controlled internal use. If an earlier artifact is missing or still blocked, copy the relevant section from asteron-capstone-rejoin-pack.txt, set its manifest Link to REJOIN-PACK-v1.0, record Trainer-validated practice fallback as coverage and continue; replace it later when the learner-created artifact passes its checkpoint.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| A downstream artifact contains an older date. | Confirm the governing source, correct the downstream file, update its version and rerun the consistency row. |
| Copilot cannot reference all three source files at once. | Draft one section per supported Word/TXT reference in Microsoft 365 Copilot Chat, then assemble and reconcile manually. Record actual source coverage; never imply an Excel workbook was read when it was not. |
| Two files appear to govern the same fact. | Choose the artifact closest to the approved source of that information and record the decision in the Authority sheet. |

**Challenge**

Draw a simple lineage diagram from source register and raw cohort through each downstream artifact. Mark where an error could propagate to three or more outputs and add one preventive check at that handoff.

**Reflection**

Which handoff carried the greatest risk of multiplying an early error, and which checkpoint contained it?

> **Note:** The complete lab and its support-file references are in labs/lab-07-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Lab 8 — Run the Responsible-Use and Privacy Release Gate

Learning outcome: LO4: apply permission, minimisation, accuracy, sensitivity, transparency and accountability controls to the complete Copilot-assisted workflow.

Goal: Produce a final release log that identifies unsafe sharing, records remediation and assigns a human decision to every artifact.

You will inspect a simulated sharing and sensitivity scenario for every Asteron artifact, identify an overbroad readiness-data link, minimise copied personal detail and complete the C027 release gate. The default path is a tabletop review; an actual permission change is permitted only in a trainer-authorised sandbox. The exercise ends with simulation-only, Revise or Hold decisions and named owners.

**What you'll build**

work-c027/C027-Asteron-Responsible-Use-Release-Log.docx with artifact-level permission, data, accuracy, audience, transparency, reviewer and release decisions   (Tools: Microsoft 365 · OneDrive or SharePoint sharing controls · Copilot · asteron-sharing-simulation.md.)

**Prerequisites**

- Labs 1-7 artifacts and cross-app manifest are complete.
- Open labs/assets/asteron-sharing-simulation.md and asteron-release-gate-template.md.
- Treat every person and access setting in the simulation as synthetic; never inspect or modify real group membership unless the trainer explicitly authorises the sandbox path.

**Step-by-step**

1. Create a blank Word document, copy the headings and tables from asteron-release-gate-template.md into it, and save it as work-c027/C027-Asteron-Responsible-Use-Release-Log.docx. Add one row for each of the six manifest artifacts plus the coordination pack. Record intended audience, simulated current access, minimum necessary data, governing source, reviewer and current state. Record Exercise path = Tabletop by default, or Trainer-authorised sandbox only when the trainer has explicitly approved it.

   ```bash
   Required artifacts = 7
Checks = Purpose | Access | Minimisation | Accuracy | Sensitivity | Transparency | Reviewer | Decision
   ```

2. Compare the simulated current access with the intended audience. Identify the readiness workbook's organisation-wide link as overbroad and the participant contact list as unnecessary for the coordination pack. Set affected artifacts to HOLD before proposing remediation.

   ```bash
   Required findings:
Readiness workbook: intended pilot team; current anyone-in-organisation link -> HOLD
Contact list: not required for stated purpose -> exclude
Outlook draft: self only and unsent -> HOLD until recipient review
Coordination pack: department heads group -> request owner verification
   ```

3. Write the remediation plan. On the default tabletop path, record the requested restriction, authorised owner and missing evidence; do not change a permission or inspect group membership. Remove unnecessary synthetic participant contact fields from your downstream lab copies, request department-heads membership verification from the owner and keep the external announcement blocked until privacy sign-off. Only on an explicitly trainer-authorised sandbox path may you perform and verify the actual permission change on the supplied lab copy.

   ```bash
   Remediation evidence to record:
Exercise path and trainer authority, if any
Requested control or actual sandbox change
Owner
Completion date
Before audience
After audience
Evidence gap or verification method
   ```

4. Run the C027 release gate on the coordination pack and Outlook draft. Check Source, Accuracy, Sensitivity, Quality, Consistency and Accountability. In Microsoft 365 Copilot Chat, reference the completed C027-Asteron-Responsible-Use-Release-Log.docx and ask for the critique below. If file reference is unavailable, paste the completed rows into Chat or apply the same checklist manually and record the fallback. Make the final decision yourself and record any generated suggestion as a proposal.

   ```bash
   Review this release log for blank evidence, inconsistent states, overbroad audiences, unsupported claims and missing owners. Return findings only; do not change permissions, send messages or approve artifacts.
   ```

5. Record final states. On the tabletop path, the coordination pack may become Approved in simulation only after the requested control, owner and evidence gap are recorded; otherwise keep it HOLD. On a trainer-authorised sandbox path, it may become Approved for controlled sandbox use only after actual evidence is verified. Neither state approves a real organisational release. The Outlook draft may become Reviewed but remains unsent. Add a transparency note describing meaningful Copilot assistance, sources reviewed, limitations and the named human release owner.

   ```bash
   Tabletop: Pack = Approved in simulation only, or HOLD when a gate remains unresolved.
Authorised sandbox: Pack = Approved for controlled sandbox use only after verified evidence.
Outlook = Reviewed draft, unsent; external announcement = HOLD until privacy sign-off.
Real organisational release = not granted; release owner = <LEARNER NAME>.
   ```


**Test it**

The release log must contain seven artifact rows and no blank reviewer or decision. It must identify the overbroad readiness link, exclude the unnecessary contact list, record the group-verification request or trainer-authorised sandbox evidence, keep the Outlook message unsent and hold the external announcement pending privacy sign-off. The coordination pack may be Approved in simulation only on the tabletop path or Approved for controlled sandbox use only on an authorised sandbox path after the required evidence is recorded. Real organisational release must remain unapproved, and the log must include a meaningful-AI-assistance note.

**Checkpoint and rejoin point**

Save the responsible-use release log with the complete work-c027 folder. The package is the final C027 practice checkpoint and can be repeated with another authorised workflow after class. Preserve the exercise path and the statement that no real organisational release was granted.

**Troubleshooting**

| If this happens | Fix |
|---|---|
| You cannot change a simulated sharing setting in your environment. | Stay on the tabletop path. Do not seek extra access. Record the current setting, required owner, remediation request and evidence gap; use Approved in simulation only only when the simulation gate is complete, otherwise HOLD. |
| Copilot's critique recommends approval without evidence. | Reject the recommendation. Only the named human reviewer can release an artifact after all gate evidence is complete. |
| An artifact contains more personal detail than its purpose requires. | Remove or aggregate the unnecessary fields in the downstream copy, retain the governed source separately and rerun the accuracy check. |

**Challenge**

Create a reusable one-page release card for your own role with the six C027 gate dimensions and one escalation trigger for each. Keep the card independent of any specific Copilot interface label.

**Reflection**

Which control depended on organisational governance rather than prompt quality, and who owns that control?

> **Note:** The complete lab and its support-file references are in labs/lab-08-*.md. Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

---


### Topic 02 Recap - Mapped to Learning Outcomes

Use this checkpoint to explain what you can now do and identify any lab evidence you still need to repair.

| Learning outcome | Evidence from this topic |
|---|---|
| LO3 - Analyse and Communicate | Bound Excel analysis to named data, inspect formulas and reconcile totals; in Outlook, separate thread facts from generated wording and keep the final send decision with the user. |
| LO4 - Coordinate and Govern | Validate Teams actions against the transcript, preserve ownership and due dates across app handoffs, and use permissions, sensitivity, source checks and human approval as release gates. |

---


## Wrap-Up - The Complete C027 Workflow

The finished output is a traceable work system, not a collection of attractive generated files. Every artifact connects its source, prompt, proposed output, verification evidence and release owner.

**Ground and create**

- Use G-C-S-E to name the goal, audience, evidence boundary and output contract.
- Verify a Chat synthesis before it becomes the factual basis of a Word document.
- Approve the Word brief before PowerPoint turns it into a visual story.

**Analyse and coordinate**

- Keep Excel data grain, formula logic, denominators and control totals visible.
- Separate Outlook thread facts from generated reply wording and review every commitment.
- Tie Teams actions to transcript evidence, named owners and due dates.

**Govern and release**

- Pass only approved versions across app handoffs and reconcile repeated facts.
- Use least privilege, minimum necessary data, sensitivity and recipient checks.
- Choose Approved, Revise or Hold with a named human reviewer and visible limitations.

---


## Next Steps

- Repeat all eight labs from the original source pack without using your completed artifacts.
- Adapt the G-C-S-E prompt card and release gate to one authorised recurring task in your role.
- Create a small cross-app manifest for authoritative files, owners, versions and release states.
- Review Microsoft Support and Learn before delivery because Copilot labels, availability and capabilities continue to change.


## Glossary

- **Copilot Chat** — A Microsoft 365 conversational experience for asking, researching, summarising and creating from permitted context.
- **Grounding** — Adding relevant source context to a prompt so the response is specific to the task.
- **G-C-S-E** — Goal, Context, Source and Expectations - the C027 prompt framework.
- **Handoff contract** — A record of source artifact, version, destination, allowed transformation, owner and verification gate.
- **Microsoft Graph** — The service layer through which Microsoft 365 can surface work context the signed-in user is permitted to access.
- **Observed** — A statement directly supported by the reviewed data or source.
- **Open question** — A material point that the available evidence does not resolve.
- **Release gate** — The source, accuracy, sensitivity, quality, consistency and accountability checks before sharing.
- **Sensitivity label** — A Microsoft Purview label that can classify and protect organisational content according to policy.
- **Source register** — A list of governing files or records with owner, date, purpose, status and access note.
- **Structured reference** — An Excel formula reference that uses table and column names.
- **Transcript** — The text record of meeting speech used as evidence for a generated recap.
