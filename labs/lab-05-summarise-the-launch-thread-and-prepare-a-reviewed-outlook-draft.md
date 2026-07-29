# Lab 5 — Summarise the Launch Thread and Prepare a Reviewed Outlook Draft

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Copilot Across Your Everyday Work Apps  
**Maps to:** LO3: summarise a bounded Outlook thread, distinguish confirmed facts from proposals and prepare a reviewed email draft without creating unsupported commitments  
**Duration:** 35 minutes  
**Tools:** Outlook for Microsoft 365 · Copilot in Outlook · asteron-email-thread.md

---

## Goal

Produce a fact-checked launch update draft whose recipients, dates, owners, attachments and unresolved items are explicitly reviewed before any send action.

## What You Will Do

You will create a private synthetic email thread in your own mailbox from the supplied messages, use Copilot to summarise decisions and open questions, then draft a concise internal update. You will verify the thread facts and leave the message unsent for the cross-app review.

## What You Will Build

An Outlook draft titled [DRAFT] Asteron pilot launch update - review required, plus work-c027/C027-Outlook-Thread-Review.md with the verified facts and release checklist

## Prerequisites

- Use only your own training mailbox or a trainer-approved sandbox mailbox.
- Open labs/assets/asteron-email-thread.md and asteron-outlook-review-template.md.
- Copy asteron-outlook-review-template.md to work-c027/C027-Outlook-Thread-Review.md before writing into it.
- Do not send the final update; the required outcome is a reviewed draft.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Create the synthetic thread in your own mailbox. Send Message 1 from asteron-email-thread.md to yourself with subject Asteron pilot launch coordination - synthetic. Paste each supplied message in full, including its synthetic From and Date labels inside the message body. Reply to the same thread with Messages 2 and 3, still addressed only to yourself. Confirm the three messages appear as one thread. For project history, the embedded synthetic labels govern; your real self-send transport metadata records only when the exercise copy was created.

```text
Safety boundary:
Recipient = your own training address only
Subject contains 'synthetic'
No real client, colleague or external address
Use only the supplied message text
```

### 2. Use Summary by Copilot or Copilot Chat in Outlook on the thread. Ask for confirmed decisions, current owners and due dates, superseded information, proposals and open questions in separate sections. Copy the result into work-c027/C027-Outlook-Thread-Review.md.

```text
Summarise this synthetic thread as Confirmed decisions | Owners and current due dates | Superseded information | Proposals | Open questions. Use ISO dates and quote the message date for each item. Do not convert a proposal or pending approval into a commitment.
```

### 3. Compare the summary with all three messages. Correct the data-export due date to 2026-08-13, keep the 2026-08-19 support clinic and room as proposed, and retain the privacy sign-off dependency before any external announcement. Record VERIFIED, REVISE or HOLD beside every item.

```text
Expected distinctions:
FAQ / Nisha Rao / 2026-08-11 = confirmed
Data export / Leon Wu / 2026-08-13 = current; 2026-08-12 superseded
Support clinic / 2026-08-19 14:00 = proposed; room pending
External announcement = HOLD until privacy sign-off
```

### 4. Use Draft with Copilot to create an internal response. Address it only to yourself, prefix the subject with [DRAFT], and require sections for Confirmed, Needs confirmation and Actions. Use coaching to review clarity and tone, but reject any suggestion that changes a fact or commitment.

```text
Draft a concise internal launch update from this verified thread. Separate Confirmed, Needs confirmation and Actions. Preserve current owners and ISO dates. Ask for room confirmation; do not announce externally. Professional, neutral tone, under 180 words. Keep the message in Draft.
```

### 5. Complete the Outlook release checklist in C027-Outlook-Thread-Review.md: To, Cc, subject, facts, commitments, attachments, links, sensitivity, tone and send decision. Save the draft without sending it. Set the release state to HOLD - pending Lab 7 cross-app consistency review.

```text
Required send decision: DO NOT SEND
Required state: HOLD - cross-app review pending
Attachments: none
Recipients: self only
```

## Test It

The mailbox must contain a three-message synthetic self-thread and one unsent draft. The review file must exist in work-c027, state that embedded synthetic sender/date labels govern project history, show 2026-08-13 as the current export date, keep the support clinic proposed and hold external announcement until privacy sign-off. The final draft must be under 180 words, addressed only to self, contain no attachment and remain HOLD - cross-app review pending.

## Checkpoint and Rejoin Point

Leave the email in Draft and save C027-Outlook-Thread-Review.md. Lab 7 compares this draft with the Word brief, PowerPoint deck, Excel workbook and Teams action register.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Outlook does not group the three messages. | Use Reply on the first self-message for Messages 2 and 3 and keep the subject unchanged. |
| Summary by Copilot is unavailable. | Use Copilot Chat in Outlook with the selected synthetic thread if supported. Otherwise use Copilot Chat with asteron-email-thread.md and record that the Outlook summary capability was unavailable. |
| Coaching recommends stronger commitment language. | Keep the verified status. Tone advice never overrides evidence or approval state. |

## Challenge

Create a second version for an executive reader in no more than 90 words. Compare which details can be removed without hiding an owner, due date, dependency or unresolved decision.

## Reflection

Why must thread extraction and reply drafting be reviewed as two separate stages?

---

[← Lab 4](lab-04-analyse-pilot-readiness-and-verify-copilot-formulas-in-excel.md) · [Lab 6 →](lab-06-validate-a-teams-recap-and-create-the-action-register.md)
