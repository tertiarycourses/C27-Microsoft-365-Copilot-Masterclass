# Microsoft 365 Copilot Masterclass - Eight Connected Maintenance Labs

One day, 7.5 instructional hours. v2.0, 13 October 2026.

Northstar Facilities is fictional. Start with 122 raw export rows in Lab 1, clean to 120 unique work orders, and carry the checked 30 September 2026 baseline through the other labs. Two refresh-test rows are used only in a sandbox copy.

[Linked prompt library](https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md) · [Local copy-button prompt page](../docs/prompts/index.html)


## Topic 1: Fundamentals of Microsoft 365 Copilot

### Lab 1: Prepare Work Orders and Draft the Operations Brief

You are Northstar Facilities’ maintenance coordinator. A Q3 export contains repeated IDs and inconsistent category labels. You will clean a copy in Excel, reconcile its controls, and use the verified result to draft a Word operations brief. The same site, status and assignment definitions underpin every later report.

**You build:** Northstar_Clean_Work_Orders.xlsx and Northstar_Operations_Brief.docx, with reconciled counts, reporting scope and a source register.

[Instructions](<./lab-01-excel-to-word/README.md>) · [PDF](<./lab-01-excel-to-word/Lab-01-Instructions.pdf>) · [Prompts](<./lab-01-excel-to-word/prompts.md>) · [Data](<./lab-01-excel-to-word/data/>) · [Templates](<./lab-01-excel-to-word/templates/>) · [Checkpoint](<./lab-01-excel-to-word/checkpoints/>)

### Lab 2: Create the Cross-App Maintenance Update

Continue the verified operations brief from Lab 1. You will turn it into an initial PowerPoint update, then prepare an Outlook reply to a synthetic maintenance thread. You will test how grounding differs between an attached file, a chat transcript and a reviewed summary, and reconcile the same facts across all four apps.

**You build:** Northstar_Initial_Update.pptx, an unsent Outlook draft and Northstar_Cross_App_Evidence.csv with Excel, Word, PowerPoint and Outlook figures reconciled.

[Instructions](<./lab-02-word-to-powerpoint-and-outlook/README.md>) · [PDF](<./lab-02-word-to-powerpoint-and-outlook/Lab-02-Instructions.pdf>) · [Prompts](<./lab-02-word-to-powerpoint-and-outlook/prompts.md>) · [Data](<./lab-02-word-to-powerpoint-and-outlook/data/>) · [Templates](<./lab-02-word-to-powerpoint-and-outlook/templates/>) · [Checkpoint](<./lab-02-word-to-powerpoint-and-outlook/checkpoints/>)


## Topic 2: Create Skills for Microsoft 365 Copilot

### Lab 3: Create a Custom Maintenance Reporting Skill

Capture the maintenance definitions and reporting style as one custom skill. You will ask Microsoft 365 Copilot on the web to write SKILL.md, compare it with a supplied complete template, install it in each app’s own supported skills location, and perform a small smoke test. A skill is reusable instructions, while a prompt is one request and workbook rules govern one file.

**You build:** A reviewed maintenance-reporting/SKILL.md v1, a smoke-test record, and a native-skill or explicitly labelled manual-practice route for each app.

[Instructions](<./lab-03-author-skill-md/README.md>) · [PDF](<./lab-03-author-skill-md/Lab-03-Instructions.pdf>) · [Prompts](<./lab-03-author-skill-md/prompts.md>) · [Data](<./lab-03-author-skill-md/data/>) · [Templates](<./lab-03-author-skill-md/templates/>) · [Checkpoint](<./lab-03-author-skill-md/checkpoints/>)

### Lab 4: Use and Improve the Skill in Excel and PowerPoint

Use the Lab 3 skill to create a verified summary and improve the initial PowerPoint update. Then deliberately test missing inputs and a rerun, tighten the skill to v2, and compare before/after evidence. The target is consistent reporting, not a longer prompt or an unsupported promise of autonomous approval.

**You build:** Northstar_Skill_Report.xlsx with Maintenance_Summary and Assignment_Proposals, Northstar_Skill_Update.pptx, SKILL.md v2 and a before/after improvement log.

[Instructions](<./lab-04-repeatable-reporting/README.md>) · [PDF](<./lab-04-repeatable-reporting/Lab-04-Instructions.pdf>) · [Prompts](<./lab-04-repeatable-reporting/prompts.md>) · [Data](<./lab-04-repeatable-reporting/data/>) · [Templates](<./lab-04-repeatable-reporting/templates/>) · [Checkpoint](<./lab-04-repeatable-reporting/checkpoints/>)


## Topic 3: Create an Interactive Dashboard with Excel Copilot

### Lab 5: Build Maintenance Dashboard Measures and Charts

Use Excel Copilot to plan a maintenance dashboard for operations managers. Define the measures before designing the charts, then build source-linked KPI cards and a status, category and site chart. You will distinguish stock measures such as current backlog from flows such as closures, and avoid calling category frequency a root cause.

**You build:** Northstar_Dashboard.xlsx with a Dashboard layout, six verified measures, three labelled charts and a measure dictionary ready for Lab 6 filters.

[Instructions](<./lab-05-design-and-build/README.md>) · [PDF](<./lab-05-design-and-build/Lab-05-Instructions.pdf>) · [Prompts](<./lab-05-design-and-build/prompts.md>) · [Data](<./lab-05-design-and-build/data/>) · [Templates](<./lab-05-design-and-build/templates/>) · [Checkpoint](<./lab-05-design-and-build/checkpoints/>)

### Lab 6: Make the Dashboard Interactive and Prove Refresh

Continue Lab 5 by making four dropdown selectors control every KPI and chart. Test a single site, a zero-denominator selection and a combined category/owner filter. Then append two synthetic work orders in a sandbox copy and prove the dashboard expands. Optional PivotTable slicers use one source and shared connections; the portable dropdown route is the required working dashboard.

**You build:** Northstar_Dashboard.xlsx with four working filters plus Northstar_Dashboard_Refresh_Test.xlsx, filter evidence and a verified baseline snapshot for PowerPoint.

[Instructions](<./lab-06-filters-and-refresh/README.md>) · [PDF](<./lab-06-filters-and-refresh/Lab-06-Instructions.pdf>) · [Prompts](<./lab-06-filters-and-refresh/prompts.md>) · [Data](<./lab-06-filters-and-refresh/data/>) · [Templates](<./lab-06-filters-and-refresh/templates/>) · [Checkpoint](<./lab-06-filters-and-refresh/checkpoints/>)


## Topic 4: Create a Professional Presentation with PowerPoint Copilot

### Lab 7: Turn Dashboard Evidence into a Management Story

Continue the baseline dashboard from Topic 3. Build a slide evidence register and a Word presentation brief before asking PowerPoint Copilot for an eight-slide management deck. The story connects work-order status, site backlog, service delivery and assignment proposals to a specific decision; it does not introduce unsupported savings or causes.

**You build:** Northstar_Presentation_Brief.docx, Northstar_Management_Draft.pptx and a slide-by-slide evidence register tied to the 120-row dashboard snapshot.

[Instructions](<./lab-07-dashboard-to-presentation/README.md>) · [PDF](<./lab-07-dashboard-to-presentation/Lab-07-Instructions.pdf>) · [Prompts](<./lab-07-dashboard-to-presentation/prompts.md>) · [Data](<./lab-07-dashboard-to-presentation/data/>) · [Templates](<./lab-07-dashboard-to-presentation/templates/>) · [Checkpoint](<./lab-07-dashboard-to-presentation/checkpoints/>)

### Lab 8: Refine and Present the Maintenance Decision Deck

Refine the management deck using the same custom skill and reviewed dashboard evidence. Improve hierarchy, consistency and speaker notes, test the story in a short rehearsal, and prepare a reviewed Outlook handoff draft. The final pack preserves the distinction between a static presentation snapshot, a refreshable dashboard and a manager’s unmade decision.

**You build:** Northstar_Management_Final.pptx/PDF, a rehearsal record, final evidence register and unsent Outlook handoff draft with accurate artifact links.

[Instructions](<./lab-08-professional-handoff/README.md>) · [PDF](<./lab-08-professional-handoff/Lab-08-Instructions.pdf>) · [Prompts](<./lab-08-professional-handoff/prompts.md>) · [Data](<./lab-08-professional-handoff/data/>) · [Templates](<./lab-08-professional-handoff/templates/>) · [Checkpoint](<./lab-08-professional-handoff/checkpoints/>)


Northstar Facilities, all sites, staff and work orders are fictional. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.