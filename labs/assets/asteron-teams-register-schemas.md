# Asteron Teams Register Schemas

Create four worksheets and Excel tables in `C027-Teams-Action-Register.xlsx`.

## Decisions — `tblDecisions`

`Decision_ID | Decision | Evidence | Status | Reviewer | Release_State`

## Actions — `tblActions`

`Action_ID | Deliverable | Owner | Due_Date | Evidence | Status | Reviewer | Release_State`

## Proposals — `tblProposals`

`Proposal_ID | Proposal | Proposed_By | Target_Date | Evidence | Resolution_Owner | Status`

## Open Questions — `tblOpenQuestions`

`Question_ID | Question | Resolution_Owner | Due_Date | Evidence | Status`

Use `Confirmed`, `Proposed` or `Open` only when the cited meeting evidence supports that state. Use `HOLD` when evidence is missing.
