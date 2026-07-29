# Lab 8 — Run the Responsible-Use and Privacy Release Gate

**Course:** Microsoft 365 Copilot Masterclass  
**Course Code:** C027  
**Version:** v1.0 (29 July 2026)  
**Topic 2:** Copilot Across Your Everyday Work Apps  
**Maps to:** LO4: apply permission, minimisation, accuracy, sensitivity, transparency and accountability controls to the complete Copilot-assisted workflow  
**Duration:** 45 minutes  
**Tools:** Microsoft 365 · OneDrive or SharePoint sharing controls · Copilot · asteron-sharing-simulation.md

---

## Goal

Produce a final release log that identifies unsafe sharing, records remediation and assigns a human decision to every artifact.

## What You Will Do

You will inspect a simulated sharing and sensitivity scenario for every Asteron artifact, identify an overbroad readiness-data link, minimise copied personal detail and complete the C027 release gate. The default path is a tabletop review; an actual permission change is permitted only in a trainer-authorised sandbox. The exercise ends with simulation-only, Revise or Hold decisions and named owners.

## What You Will Build

work-c027/C027-Asteron-Responsible-Use-Release-Log.docx with artifact-level permission, data, accuracy, audience, transparency, reviewer and release decisions

## Prerequisites

- Labs 1-7 artifacts and cross-app manifest are complete.
- Open labs/assets/asteron-sharing-simulation.md and asteron-release-gate-template.md.
- Treat every person and access setting in the simulation as synthetic; never inspect or modify real group membership unless the trainer explicitly authorises the sandbox path.

> **Data note.** Use only the supplied synthetic Asteron Services data or information you are authorised to process. Do not paste credentials, confidential business material or unnecessary personal data into Copilot.

## Steps

### 1. Create a blank Word document, copy the headings and tables from asteron-release-gate-template.md into it, and save it as work-c027/C027-Asteron-Responsible-Use-Release-Log.docx. Add one row for each of the six manifest artifacts plus the coordination pack. Record intended audience, simulated current access, minimum necessary data, governing source, reviewer and current state. Record Exercise path = Tabletop by default, or Trainer-authorised sandbox only when the trainer has explicitly approved it.

```text
Required artifacts = 7
Checks = Purpose | Access | Minimisation | Accuracy | Sensitivity | Transparency | Reviewer | Decision
```

### 2. Compare the simulated current access with the intended audience. Identify the readiness workbook's organisation-wide link as overbroad and the participant contact list as unnecessary for the coordination pack. Set affected artifacts to HOLD before proposing remediation.

```text
Required findings:
Readiness workbook: intended pilot team; current anyone-in-organisation link -> HOLD
Contact list: not required for stated purpose -> exclude
Outlook draft: self only and unsent -> HOLD until recipient review
Coordination pack: department heads group -> request owner verification
```

### 3. Write the remediation plan. On the default tabletop path, record the requested restriction, authorised owner and missing evidence; do not change a permission or inspect group membership. Remove unnecessary synthetic participant contact fields from your downstream lab copies, request department-heads membership verification from the owner and keep the external announcement blocked until privacy sign-off. Only on an explicitly trainer-authorised sandbox path may you perform and verify the actual permission change on the supplied lab copy.

```text
Remediation evidence to record:
Exercise path and trainer authority, if any
Requested control or actual sandbox change
Owner
Completion date
Before audience
After audience
Evidence gap or verification method
```

### 4. Run the C027 release gate on the coordination pack and Outlook draft. Check Source, Accuracy, Sensitivity, Quality, Consistency and Accountability. In Microsoft 365 Copilot Chat, reference the completed C027-Asteron-Responsible-Use-Release-Log.docx and ask for the critique below. If file reference is unavailable, paste the completed rows into Chat or apply the same checklist manually and record the fallback. Make the final decision yourself and record any generated suggestion as a proposal.

```text
Review this release log for blank evidence, inconsistent states, overbroad audiences, unsupported claims and missing owners. Return findings only; do not change permissions, send messages or approve artifacts.
```

### 5. Record final states. On the tabletop path, the coordination pack may become Approved in simulation only after the requested control, owner and evidence gap are recorded; otherwise keep it HOLD. On a trainer-authorised sandbox path, it may become Approved for controlled sandbox use only after actual evidence is verified. Neither state approves a real organisational release. The Outlook draft may become Reviewed but remains unsent. Add a transparency note describing meaningful Copilot assistance, sources reviewed, limitations and the named human release owner.

```text
Tabletop: Pack = Approved in simulation only, or HOLD when a gate remains unresolved.
Authorised sandbox: Pack = Approved for controlled sandbox use only after verified evidence.
Outlook = Reviewed draft, unsent; external announcement = HOLD until privacy sign-off.
Real organisational release = not granted; release owner = <LEARNER NAME>.
```

## Test It

The release log must contain seven artifact rows and no blank reviewer or decision. It must identify the overbroad readiness link, exclude the unnecessary contact list, record the group-verification request or trainer-authorised sandbox evidence, keep the Outlook message unsent and hold the external announcement pending privacy sign-off. The coordination pack may be Approved in simulation only on the tabletop path or Approved for controlled sandbox use only on an authorised sandbox path after the required evidence is recorded. Real organisational release must remain unapproved, and the log must include a meaningful-AI-assistance note.

## Checkpoint and Rejoin Point

Save the responsible-use release log with the complete work-c027 folder. The package is the final C027 practice checkpoint and can be repeated with another authorised workflow after class. Preserve the exercise path and the statement that no real organisational release was granted.

## Troubleshooting

| If this happens | Fix |
|---|---|
| You cannot change a simulated sharing setting in your environment. | Stay on the tabletop path. Do not seek extra access. Record the current setting, required owner, remediation request and evidence gap; use Approved in simulation only only when the simulation gate is complete, otherwise HOLD. |
| Copilot's critique recommends approval without evidence. | Reject the recommendation. Only the named human reviewer can release an artifact after all gate evidence is complete. |
| An artifact contains more personal detail than its purpose requires. | Remove or aggregate the unnecessary fields in the downstream copy, retain the governed source separately and rerun the accuracy check. |

## Challenge

Create a reusable one-page release card for your own role with the six C027 gate dimensions and one escalation trigger for each. Keep the card independent of any specific Copilot interface label.

## Reflection

Which control depended on organisational governance rather than prompt quality, and who owns that control?

---

[← Lab 7](lab-07-assemble-and-reconcile-the-cross-app-coordination-pack.md) · [Labs index →](README.md)
