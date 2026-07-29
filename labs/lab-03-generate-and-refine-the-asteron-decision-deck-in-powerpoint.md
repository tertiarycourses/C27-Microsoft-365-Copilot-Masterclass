# Lab 3 — Generate and Refine the Asteron Decision Deck in PowerPoint

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 1:** Getting Started with Microsoft 365 Copilot  
**Maps to:** LO2: generate a presentation from an approved Word source, refine the narrative and verify facts, visuals, accessibility and speaker notes before use  
**Duration:** 40 minutes  
**Tools:** PowerPoint for Microsoft 365 · Copilot in PowerPoint · C027-Asteron-Launch-Brief-v1.0.docx

---

## Goal

Create a concise six-slide decision deck that preserves the approved Word brief and makes the remaining decision visible without inventing evidence.

## What You Will Do

You will use the approved Lab 2 Word brief to generate a PowerPoint draft for department heads. You will compare every factual slide with the source, replace generic or misleading content, refine one slide from a referenced file and complete an accessibility and release check.

## What You Will Build

work-c027/C027-Asteron-Decision-Deck-v1.0.pptx with six decision-oriented slides, concise speaker notes, source notes and a Reviewed for internal presentation status

## Prerequisites

- Lab 2 Word brief is saved in OneDrive and marked Approved for deck handoff.
- Open labs/assets/asteron-deck-spec.md and keep the Lab 1 source register available.
- Use only synthetic Asteron files and approved built-in or licensed visual assets.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Open PowerPoint, start a new presentation and use Copilot to create a presentation from C027-Asteron-Launch-Brief-v1.0.docx. Request exactly six slides for department heads. Save the result immediately as work-c027/C027-Asteron-Decision-Deck-v1.0.pptx.

```text
Create a six-slide internal decision presentation from the referenced approved Word brief. Use concise titles, one message per slide and speaker notes. Do not add facts not present in the source.
```

### 2. Compare the generated structure with the deck specification. Rename, reorder, add or remove slides until the sequence is exactly: decision, scope, readiness, timeline, risks and next actions. Keep the support-clinic room visibly unresolved. Because verified numerical readiness measures are not created until Lab 4, slide 3 must show dependencies and status only; add no readiness numbers in this lab.

```text
Required sequence:
1. Decision needed
2. Pilot scope
3. Readiness snapshot
4. Timeline and owners
5. Risks and open question
6. Next actions
```

### 3. For slides 2-6, compare every date, number, owner and status with the Word brief and source register. Add a small source note in the speaker notes using Source_ID values. Remove or rewrite any content that cannot be traced.

```text
Required facts:
20 internal participants · five departments · 2026-08-18 launch
Nisha Rao / 2026-08-11 · Leon Wu / 2026-08-13
external announcement waits for privacy sign-off
support clinic room remains open
```

### 4. Refine slide 4 by asking Copilot to rewrite the existing timeline. If Copilot creates a new timeline slide, move it into position 4 and delete the superseded slide so the deck remains exactly six slides. Keep four milestones only. Replace decorative imagery that could be mistaken for real Asteron evidence with a simple editable timeline or icon-based process.

```text
Create a four-milestone timeline from the referenced brief: FAQ due 2026-08-11; data export due 2026-08-13; privacy sign-off before external announcement; pilot launch 2026-08-18. Do not add a confirmed support-clinic milestone.
```

### 5. Run Review > Check Accessibility in PowerPoint. Resolve each fixable issue and record the Accessibility Checker result, including any accepted limitation, in the final notes. Then confirm a single message per slide, readable text, strong contrast, logical reading order, meaningful alternative text, concise speaker notes and no unsupported image. In the file properties or final notes, record status Reviewed for internal presentation, reviewer and date.

```text
Release check:
Story | Facts | Visual evidence | Accessibility | Speaker notes | Audience | Reviewer | State
```

## Test It

The deck must contain exactly six slides in the required sequence. All repeated facts must match the approved Word brief, slide 3 must show dependencies/status without numerical readiness measures, slide 4 must contain only the four approved milestones, and no visual may imply real customer evidence. Each factual slide must have a Source_ID note. The final notes must record the Accessibility Checker result, and the final state must be Reviewed for internal presentation.

## Checkpoint and Rejoin Point

Save and close the six-slide deck. Labs 7 and 8 will check it against the other app outputs. Keep the approved Word brief unchanged as the governing narrative source.

## Troubleshooting

| If this happens | Fix |
|---|---|
| Create from file is unavailable or the Word file is not listed. | Confirm the file is saved to OneDrive, the correct account is active and Copilot is enabled. If necessary, create the six-slide structure manually and use Copilot to draft one slide at a time from the brief. |
| Copilot creates more or fewer than six slides. | Keep only the required sequence and merge duplicate content. Do not add slides merely to preserve generated text. |
| A generated image is irrelevant or misleading. | Remove it and use an editable shape, icon or timeline that communicates structure without pretending to be evidence. |

## Challenge

Use Copilot to propose two alternative titles for slide 1: one neutral and one action-oriented. Choose the title that best reflects the actual decision without overstating urgency or certainty.

## Reflection

Which part of the Word brief required the greatest transformation to work as a slide, and what had to remain unchanged?

---

[← Lab 2](lab-02-draft-and-approve-the-asteron-launch-brief-in-word.md) · [Lab 4 →](lab-04-analyse-pilot-readiness-and-verify-copilot-formulas-in-excel.md)
