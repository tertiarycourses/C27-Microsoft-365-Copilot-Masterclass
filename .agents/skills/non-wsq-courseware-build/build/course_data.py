"""C27 v2.0: one connected Northstar maintenance scenario and C34 visual system."""
TITLE=SHORT_TITLE='Microsoft 365 Copilot Masterclass'
COURSE_CODE='C27'
COURSE_PAGE='https://www.tertiarycourses.com.sg/microsoft-365-copilot-masterclass.html'
GITHUB_REPO='tertiarycourses/C27-Microsoft-365-Copilot-Masterclass'
PROMPTS_PAGE='https://github.com/tertiarycourses/C27-Microsoft-365-Copilot-Masterclass/blob/main/docs/prompts/README.md'
VERSION='v2.0';VERSION_DATE='13 October 2026'
ORG='Tertiary Infotech Academy Pte Ltd';UEN='UEN: 201200696W'
TRAINER='Assigned Tertiary Infotech Academy Trainer';DAYS=1;DAY_MINUTES=480;INSTRUCTIONAL_MINUTES=450
MODE='Instructor-led, hands-on practical labs';DAILY_TIMING='9:30 am - 6:30 pm (1-hour lunch; two 15-minute tea breaks; 7.5 instructional hours)';DARK_THEME=False
VERSION_HISTORY=[('1.0','29 July 2026','Previous Asteron cross-app scenario; retained in archive.','Tertiary Infotech Academy'),('2.0',VERSION_DATE,'Four maintenance topics; eight connected labs, custom Excel/PowerPoint skills, interactive dashboard and management presentation; C34 design.','Tertiary Infotech Academy')]
LEARNING_OUTCOMES=[
'LO1: Integrate Word, Excel, PowerPoint and Outlook Copilot in a coherent maintenance workflow with explicit source grounding and verified prompts.',
'LO2: Create, install, apply and improve a custom maintenance-reporting skill in Excel and PowerPoint, preserving source records and testing reruns.',
'LO3: Create an interactive maintenance dashboard with verified measures, common filter scope, meaningful charts and a demonstrated refresh test.',
'LO4: Continue from the dashboard to a professional management presentation, with evidence-based headlines, source notes, rehearsal and a reviewed handoff draft.']
LO_TITLES=['Connected Copilot workflow','Reusable maintenance skills','Interactive dashboard','Professional presentation']
ICE_BREAKER=['Your name, role and one maintenance reporting task.','Which app holds the work-order source?','Which date and status definitions determine overdue work?','Check which Copilot buttons and skills menus are available in your assigned apps.']
LAB_NOTE='Northstar Facilities, all sites, staff and work orders are fictional. Use the fixed reporting date 2026-09-30; missing facts remain UNKNOWN. Proposals do not change real assignments. Training email drafts are never sent.'
LG_INTRO='This masterclass follows Northstar Facilities from a dirty maintenance export to a reviewed management decision pack. Work-order IDs, categories, sites, current assignments and status definitions stay consistent across every app. The purpose is to make evidence travel accurately through the workflow, while using Copilot for drafting, analysis, reusable instructions and visual communication.'
LG_INTRO2='Study each topic’s concepts before its two labs. Each lab has its own instruction PDF, identical Markdown steps, prompts, synthetic data, templates and a deterministic checkpoint. Carry your own verified outputs forward. A supplied checkpoint allows rejoining but is not evidence that you completed the earlier task. The detailed procedures are here and in labs; the slides teach concepts and show outcomes.'
LG_SETUP=dict(needs=['Assigned Microsoft 365 account with Copilot in Word, Excel, PowerPoint and Outlook; licence and tenant settings checked before class.','Excel desktop Windows or Mac recommended; current apps, English display language for Excel custom skills, assigned OneDrive and AutoSave.','Complete lab folder downloads and a personal work-c027 output folder; all sample data is synthetic.','Copilot skills access in both Excel and PowerPoint. If unavailable, the lab supplies a clearly labelled manual-instruction practice route.'],verify_text='Open one workbook and one Word/PowerPoint template; find each Copilot button. Confirm that the app can select the intended OneDrive reference file. Use the app-created custom skills folder rather than guessing a path. Keep Formulas > Calculation Options > Automatic. Never paste account passwords into a prompt.',conventions=['App-labelled prompts run in the named app; a prompt in one app is not automatically visible to another.','Use Chat only for inspection, Plan for reviewed proposals, and Allow editing for authorised workbook changes when these modes are available.','Log Word, Outlook, PowerPoint and web prompts manually in Prompt_Log.','All comparisons use the same source table, reporting date and filter scope. Missing values remain UNKNOWN; zero closed denominator is N/A.'])
S_EXCEL='https://support.microsoft.com/en-us/excel/copilot/copilot-in-excel-skills'
S_PPT='https://support.microsoft.com/en-us/powerpoint/copilot/copilot-in-powerpoint-skills'
S_WORD='https://support.microsoft.com/en-gb/word/copilot/draft-and-add-content-with-copilot-in-word'
S_FILES='https://support.microsoft.com/en-us/microsoft-365-copilot/file-formats-supported-by-microsoft-365-copilot'
S_DASH='https://support.microsoft.com/en-us/excel/create-and-share-a-dashboard-with-excel-and-microsoft-groups'
S_SLICER='https://support.microsoft.com/en-us/excel/get-started/use-slicers-to-filter-data'
S_SLIDE='https://support.microsoft.com/en-us/powerpoint/copilot/add-a-slide-from-a-file-with-copilot-in-powerpoint'
def sec(lab,title,definition,why,how,example,uses,avoids,sources):
 return dict(lab=lab,title=title,definition=definition,why=why,how=how,example=example,use_when=uses,avoid_when=avoids,sources=sources)
SECTIONS=[
sec(1,'Grounding Across Microsoft 365',
'Grounding gives an AI request the specific evidence it should use. A work-grounded Copilot experience can use permitted organisational content; a file-grounded request uses selected files or supplied text. Neither makes an inaccessible file available merely because its local path is typed into a prompt. Word, Excel, PowerPoint and Outlook have different current-document and file-reference experiences. Treat each app handoff as a new grounding task.',
'A maintenance figure can be correct in Excel yet become wrong in an email when the source, reporting date or filter scope changes. Explicit grounding prevents unsupported owner assignments, stale reporting periods and invented approvals from entering the pack. A Copilot response is a draft or hypothesis until the underlying evidence has been checked.',
['Identify the authoritative work-order table.','Provide goal, context, source and expected output.','Review against the named evidence.','Pass a verified snapshot to the next app.'],
['Excel analyses tblWorkOrders; Word receives the checked summary.','PowerPoint receives the reviewed Word brief; Outlook receives the same checked values.','An Excel chat transcript is not an automatic PowerPoint data source.'],
['The source is accessible and the output has an explicit audience.'],['The prompt assumes access to another app chat or local path.'],[S_FILES,S_WORD]),
sec(1,'Work-Order Grain and Reporting Measures',
'A row represents one work order, identified by Work_Order_ID. Site, job category, priority, status and current assignment are dimensions used to group or filter records. Measures are defined calculations. The source is a snapshot at 30 September 2026: current backlog excludes Closed and Cancelled; overdue backlog also has a Due_Date before that date. Closed orders are counted separately from jobs still in the queue.',
'An exact duplicated export row changes counts and cost without representing new work. Normalising a category spelling must not change the business meaning or assign a missing owner. Named Excel tables and structured references let formulas expand when legitimate new rows are appended. Preserve the raw export so a cleaning decision can be traced.',
['Define one ID per work order.','Find exact repeated export records.','Standardise labels without inventing facts.','Reconcile cleaned counts and cost.'],
['122 raw rows contain 120 distinct work-order IDs.','Total = Closed + Cancelled + Backlog after exact duplicate removal.','Due on 30 September is not overdue at the 30 September snapshot.'],
['You have consistent IDs and a fixed reporting date.'],['Duplicate IDs contain conflicting records or reporting scope is unknown.'],[S_DASH]),
sec(2,'Prompts and Verified App Handoffs',
'A useful prompt combines the intended goal, operational context, named source and output expectations. The handoff object is a verified artifact, such as a Word brief with a checked metric table and source links. It is not an assumption that another app can remember the preceding conversation. For maintenance, expectations should specify exact dates, status vocabulary, current versus proposed assignments and missing-value behaviour.',
'The same number may have different meaning when a chart counts all work orders while an email calls it open backlog. A cross-app evidence register records the claim, value, source table, filter scope and date. This provides a small reproducible contract for each output and lets a reviewer identify a mismatch before it becomes a management decision.',
['Write the goal and audience.','Attach or select the actual source.','Specify definitions and missing-value behaviour.','Reconcile the returned claims.'],
['Goal: draft a maintenance update for the operations manager.','Source: reviewed Northstar operations brief, all filters All, 30 September.','Expectation: label assignment suggestions as proposals and leave unknown approvals UNKNOWN.'],
['A reviewed brief can be selected or its checked text pasted.'],['Only an unverified summary is available.'],[S_WORD,S_SLIDE,S_FILES]),
sec(2,'Outlook Drafting and Operational Decisions',
'Copilot can help structure a draft email from supplied context. A synthetic text thread is quoted context, not a live Outlook conversation; the course explicitly uses it that way. The writer remains responsible for recipients, claims, attachments, tone and the distinction between a proposed action and an approved instruction. Saving a draft does not send it or authorise a work-order change.',
'An apparently routine update can accidentally promise technician reassignment or imply that a manager approved a recovery plan. Current assignment is recorded data; proposed assignment is a separate planning output. Available hours are one input to planning, not evidence of approval or guaranteed productivity. The final email should request the decision rather than claim it has happened.',
['Provide the synthetic thread and checked facts.','Draft a concise update.','Review recipients, facts and action wording.','Save the unsent draft and evidence.'],
['Current owner blank; proposed owner Aisha remains unapproved.','A draft addressed to example.invalid is a training artifact.','The handoff says decision requested, not decision approved.'],
['You can check the evidence and review the draft before use.'],['The task would imply a real approval or send without review.'],[S_FILES]),
sec(3,'Skills, Prompts and Workbook Rules',
'A prompt is one request. A custom skill is a reusable set of instructions that tells Copilot when and how to perform a recurring task. SKILL.md contains required YAML name and description followed by the instructions. Each skill needs its own folder with a matching name. Workbook-specific rules describe constraints for one workbook; a skill can carry the same maintenance process across repeated reports and supported apps.',
'The skill makes stable definitions and review boundaries reusable: backlog excludes two terminal statuses, overdue uses a fixed date, missing owners stay missing and output reruns do not duplicate sheets. It does not supply absent work-order data or turn an unsupported app feature into an available one. Skill availability must be verified separately in the app where it will run.',
['Identify a recurring task.','Separate stable rules from current inputs.','Write name, description and instructions.','Install, invoke and inspect the result.'],
['maintenance-reporting contains definitions and output boundaries.','Each request still supplies this month’s source, date and scope.','Native skill use and pasted manual instructions are recorded differently.'],
['The same reporting method recurs and can be tested.'],['Inputs or desired behaviour are still undefined.'],[S_EXCEL,S_PPT]),
sec(3,'Custom Skill Discovery in Each App',
'Excel uses its Manage plugins & skills interface and an app-created OneDrive skills folder. PowerPoint uses Choose skills and Manage skills with an Add skill/upload route or its own custom skills folder. The app UI resolves the supported folder; a guessed universal path is unreliable. Refresh and enable the skill, then verify the exact name in each app before invoking it by @mention or the menu.',
'Folder-name/frontmatter mismatches, an extra .txt extension, unavailable licence features and disabled skills can all prevent discovery. A web Copilot authoring conversation can produce the complete Markdown text, but the learner still saves, installs and tests it. Excel cannot log the web chat automatically. Clear installation evidence prevents confusing a manually pasted policy with a native reusable skill.',
['Save complete UTF-8 SKILL.md.','Use the app-created skills location.','Refresh and verify the matching name.','Run and record a smoke test.'],
['Folder maintenance-reporting matches YAML name maintenance-reporting.','Excel and PowerPoint both show the skill before native invocation.','If a menu is absent, manual practice is labelled feature unavailable.'],
['The app exposes its supported skill installation controls.'],['A missing menu is being treated as successful installation.'],[S_EXCEL,S_PPT]),
sec(4,'Repeatability and Safe Skill Reruns',
'Repeatability means the same verified inputs and method yield equivalent business measures and a controlled output structure. A safe rerun preserves source IDs, statuses, assignments and unrelated sheets. It creates or replaces only explicitly named outputs after review. The concept is similar to idempotence: rerunning should not append duplicate summaries, inflate totals or silently destroy a learner’s unrelated work.',
'Reporting skills may be used every week or month, so uncontrolled output accumulation quickly creates conflicting summaries. An input guard asks for missing data; a replacement guard identifies the output to change. Test those guards using a copy and compare row count, sums, sheet inventory and output measures before and after, rather than relying on Copilot saying it was careful.',
['Capture the source fingerprint and outputs.','Request a reviewed rerun plan.','Replace only named output areas.','Compare source and measures again.'],
['120 source IDs remain 120 after rerunning Maintenance_Summary.','Missing report date causes a clarification request, not invented numbers.','A second output sheet is a defect when replacement was requested.'],
['Named output boundaries and reconciliation checks exist.'],['The skill can overwrite source rows or unrelated sheets.'],[S_EXCEL,S_PPT]),
sec(4,'Assignment Proposals and Capacity Evidence',
'Assignment planning combines the work category, existing owner, estimated hours, technician primary category and available hours. These inputs help generate a proposal; they do not prove complete operational suitability, approved schedules or safety authorisation. Keep Current_Assigned_To separate from Proposed_Assigned_To and use an explicit manager-decision field. Missing evidence is UNKNOWN, not a confident allocation.',
'The same skill can improve Excel analysis and PowerPoint wording by preserving this boundary. Excel shows category/capacity checks and assumptions in a proposals sheet; PowerPoint explains the findings and requests a decision. A polished visual must not conceal uncertain capacity or make the proposed owner look like the current owner.',
['Identify unassigned backlog.','Compare category and available hours.','Record the proposal and assumptions.','Request the manager decision.'],
['Unassigned work is counted only within nonterminal statuses.','Available hours minus proposed effort is a planning check.','The source Assigned_To stays unchanged until a real authorised operational update.'],
['A manager can review the proposal and missing constraints.'],['The report claims automatic approval or verified safety qualification.'],[S_EXCEL,S_PPT]),
sec(5,'Dashboard Measures and Denominators',
'A dashboard measure needs a business definition, numerator, denominator where relevant, date rule and filter scope. Total orders describes the selected portfolio. Backlog is the selected nonterminal work. Overdue is a subset of backlog. On-time closure rate describes Closed rows only: closed on or before their due date divided by Closed rows. Recorded cost sums selected Cost_SGD; it is not a budget variance or inferred savings.',
'Changing the denominator can make an attractive rate meaningless. If the selected data contains no Closed rows, the on-time rate is N/A because it is undefined; a displayed 0% would falsely suggest failed delivery. A Measures dictionary and independent control sheet make the definitions inspectable. A fixed reporting date gives reproducible comparisons, while TODAY would change the snapshot over time.',
['Define source fields and scope.','Compute count and denominator.','Handle empty selections explicitly.','Reconcile against controls.'],
['Closed-only rate is different from closed/total completion share.','A due-today backlog item is not overdue under a strict before-date rule.','All selected status/chart counts reconcile to total selected work orders.'],
['Measures have agreed definitions and evidence.'],['A zero denominator is being represented as a measured 0%.'],[S_DASH]),
sec(5,'Visual Dashboard Design for Maintenance',
'A dashboard should make an operational decision easier. KPI cards summarise magnitude; bar charts compare sites, categories or status counts. Labels, units and source/date context define what each visual means. Site backlog and total orders by site answer different questions and must have different names. Use a line chart for a genuine ordered time series, not unordered site names.',
'Consistent chart scales, short labels, whitespace and limited accents help a manager compare the work queue quickly. Colour alone is insufficient to distinguish statuses. A category count is evidence of frequency, not a causal diagnosis; a busy site is not necessarily performing badly. Choose the visual based on the question and include the limitation that prevents overinterpretation.',
['Name the maintenance decision.','Choose the measure and comparison.','Use an appropriate labelled chart.','Check meaning and readability.'],
['Status count chart shows the portfolio mix.','Site backlog chart excludes Closed and Cancelled.','A category count does not establish the root cause of overdue jobs.'],
['The visual has a clear audience and question.'],['Decorative charts hide an ambiguous metric.'],[S_DASH]),
sec(6,'One Filter Scope for Every Visual',
'Interactive means a learner-controlled selection changes the evidence shown. This course’s portable route uses four dropdowns and formula measures with AND logic. All bypasses one dimension only. Every KPI and chart uses the same selected rows. Optional slicers filter connected PivotTables; they do not automatically alter unrelated formulas or every table on the sheet. PivotTables sharing a slicer need the same source.',
'A dashboard can appear interactive while only one chart changes. Test a single-site selection, a combined category/owner selection and an empty selection. Check the displayed scope and compare every chart total with the selected total. Worksheet AutoFilter and formula-selector filters are different mechanisms; hiding source rows does not prove that formulas have changed scope.',
['Define the selector cells.','Apply the same AND mask everywhere.','Test each control and edge case.','Reconcile selected chart and KPI totals.'],
['Woodlands Hub plus All in other selectors isolates that site.','Status New gives zero Closed and N/A closure rate.','A slicer must connect to every intended PivotTable.'],
['All output calculations follow the same scope.'],['A selector only changes a decorative title or one chart.'],[S_SLICER,S_DASH]),
sec(6,'Refresh Tests and Static Snapshots',
'A refresh test deliberately introduces known new records and verifies the expected delta. Table references should expand when rows are appended; PivotTables additionally need a refresh and valid source extent. The course adds two rows in a sandbox copy so the live baseline remains 120 rows. A Word/PDF/PowerPoint snapshot freezes evidence and does not automatically update when the Excel dashboard changes.',
'A correct dashboard today may fail after the next export if formulas reference a fixed cell range. Known delta testing reveals that failure. Preserving a separate baseline prevents a test record from contaminating the management pack. A snapshot should record source, as-at date, filters and version so its claims remain interpretable after the workbook is refreshed.',
['Save an isolated sandbox copy.','Append known unique test rows.','Recalculate and verify expected deltas.','Handoff the untouched baseline.'],
['Two test rows increase total by2 and recorded cost byS$400.','Only one new row adds to backlog/overdue; the other adds to on-time Closed.','The final deck uses the untouched 120-row baseline, not the test copy.'],
['A predictable change can be checked independently.'],['Test rows are being mixed into the report without disclosure.'],[S_DASH]),
sec(7,'From Dashboard Evidence to a Decision Story',
'A management presentation transforms evidence into a sequence of observations, implications, proposed actions and a decision request. Each slide needs one defensible headline and a register entry linking the claim to its measure, source, reporting date and filter scope. A chart contains data; the headline interprets it. That interpretation must stay within what the data supports.',
'Copilot can accelerate outlines and drafting, but a persuasive invented conclusion is still wrong. Before generating the deck, use Word to organise an eight-slide brief with a supporting chart and limitation for each claim. This explicit bridge makes the Excel-to-PowerPoint handoff reliable and avoids assuming a workbook can be used by every presentation-generation mode.',
['Freeze the verified dashboard snapshot.','Register each proposed claim.','Write a reviewed Word brief.','Generate and reconcile the deck.'],
['Backlog by site supports prioritisation, not a proven cause.','Available-hours evidence supports a capacity discussion, not confirmed allocation.','The final slide asks management to decide on a proposed plan.'],
['Every headline has a checked measure and clear scope.'],['The story introduces savings, causes or approvals absent from evidence.'],[S_WORD,S_SLIDE,S_FILES]),
sec(7,'Charts, Templates and Source Provenance',
'A template supplies slide layouts, typography and colours; it does not supply correct facts. PowerPoint Copilot can draft slides from selected supported files. Reviewed Word briefs are a reliable narrative input for this course. Excel charts may be embedded for editing or pasted as images; both are copies of a reporting state unless a separate supported link is deliberately configured and tested.',
'Approximate AI-generated charts can contradict source values while looking plausible. Replace them with reviewed charts or verified tables and keep source/date notes. Distinguish all-work-order counts from backlog-only counts. A professional presentation uses consistent units and chart semantics, not just a consistent palette.',
['Select the reviewed brief.','Apply the existing template.','Insert verified charts or tables.','Record source and snapshot scope.'],
['An editable embedded chart remains a copy rather than a tested live link.','An image is labelled as a snapshot at 30 September.','All eight slides use one reviewed baseline.'],
['The chart object or image can be verified against the register.'],['A visual is assumed accurate because Copilot produced it.'],[S_SLIDE,S_FILES]),
sec(8,'Professional Refinement and Rehearsal',
'Refinement improves the clarity of the existing evidence without changing its meaning. Claim-led titles, short visible text, readable axes, consistent chart styles and concise speaker notes help an audience understand the maintenance decision. Rehearsal tests whether the audience can identify the reporting scope, the key finding and the decision required. It produces observed feedback, not a fabricated checklist completion.',
'A well-designed deck can still fail when the speaker’s notes contain different numbers or a proposal is spoken as an approved action. Review notes as part of the evidence pack and inspect the exported PDF at presentation size. Exporting can alter layout or font rendering, so the PDF must be opened and checked rather than assumed identical to the source.',
['Audit the draft against evidence.','Apply reviewed design changes.','Rehearse and record actual feedback.','Inspect PPTX and exported PDF.'],
['One message per slide; chart labels remain readable.','A 45-second note explains evidence and limitation.','Partner feedback leads to one recorded revision.'],
['The message and decision can be understood quickly.'],['Polish hides an unsupported claim or unreadable chart.'],[S_PPT]),
sec(8,'Reviewed Handoff and Artifact Lifecycle',
'The final pack contains an interactive Excel dashboard, a fixed reporting brief, a static PowerPoint/PDF snapshot, the custom skill and a reviewed communication draft. These artifacts have different lifecycles. The dashboard may refresh; the skill defines a method; the presentation records a dated claim set. Link each file accurately and preserve the evidence register so a later reader knows what was reviewed.',
'Updating one artifact without the others creates inconsistent communication. Reconcile the final pack and explicitly state that actions remain proposed and the email remains a draft. Versioned source and archived superseded artifacts let the team revisit an earlier report without confusing it with the current one. A missing link is UNKNOWN until an actual accessible link is supplied.',
['Reconcile final artifacts.','Record actual filenames and links.','Review the handoff draft.','Preserve the dated snapshot and skill.'],
['PowerPoint and PDF both show eight slides/pages from the same baseline.','Outlook does not claim a missing attachment was sent.','The next update reruns the method with new verified inputs.'],
['Current versions and review evidence are explicit.'],['A refreshed dashboard is assumed to rewrite an old presentation.'],[S_FILES,S_PPT])]
TOPICS=[]
for n,title,subtitle,concepts in [
(1,'Fundamentals of Microsoft 365 Copilot','One verified maintenance workflow across four apps',[('Grounding','Select actual sources in every app.'),('Work orders','IDs, status, category, site and current assignment.'),('Prompts','Goal, context, source and expectations.'),('Handoffs','Reconcile Word, Excel, slides and draft email.')]),
(2,'Create Skills for Microsoft 365 Copilot','A reusable method for Excel and PowerPoint',[('SKILL.md','Matching folder/name and reusable instructions.'),('Discovery','Install and verify separately in each app.'),('Repeatability','Input guards and controlled reruns.'),('Proposals','Preserve source owners and evidence boundaries.')]),
(3,'Create an Interactive Dashboard with Excel Copilot','From definitions to filters and refresh evidence',[('Measures','Counts, backlog, overdue, on-time rate and cost.'),('Visuals','Choose charts by maintenance question.'),('Interactions','One filter scope for every chart and KPI.'),('Refresh','Known deltas in an isolated test copy.')]),
(4,'Create a Professional Presentation with PowerPoint Copilot','Continue the dashboard into a decision pack',[('Evidence story','Observation, implication, action and decision.'),('Charts','Reviewed values, provenance and snapshot date.'),('Refinement','Hierarchy, notes and actual rehearsal feedback.'),('Handoff','Reconciled pack and unsent communication.')])]:
 TOPICS.append(dict(num=n,code=str(n),title=title,subtitle=subtitle,concepts=concepts,sections=[s for s in SECTIONS if (s['lab']-1)//2+1==n]))
TOPIC_RECAPS={1:[('LO1','Same work-order evidence across four apps.'),('Verify','120 clean IDs and reconciled brief/update/draft.')],2:[('LO2','Skill authoring, discovery, use and revision proven.'),('Verify','Preserved source plus missing-input and rerun tests.')],3:[('LO3','Six measures and three charts share four filters.'),('Verify','Baseline controls and known refresh deltas.')],4:[('LO4','Eight-slide evidence story and reviewed handoff.'),('Verify','PDF, notes, register and actual rehearsal agree.')]}
DAY_THEMES={1:'Maintenance workflow, custom skills, interactive dashboard and professional management presentation'}
def SCHEDULE(lab_titles):
 from datetime import datetime,timedelta
 blocks=[(15,'admin','Welcome, learning outcomes, app access and Northstar scenario')]
 durations=[35,35,40,40,50,50,45,45]
 for n,d in enumerate(durations,1):
  blocks.append((10,'topic',f'Topic {(n-1)//2+1}: concepts for Lab {n}'))
  blocks.append((d,'lab',lab_titles([n])))
  if n==1:blocks.append((15,'break','Tea break'))
  if n==3:blocks.append((60,'lunch','Lunch'))
  if n==5:blocks.append((15,'break','Tea break'))
 blocks.append((15,'recap','LO1-LO4 recap, evidence handoff and questions'))
 now=datetime(2026,10,13,9,30);rows=[]
 for mins,kind,text in blocks:
  end=now+timedelta(minutes=mins);rows.append((now.strftime('%H:%M'),end.strftime('%H:%M'),mins,kind,text));now=end
 assert sum(m for _,_,m,k,_ in rows if k!='lunch')==480
 assert sum(m for _,_,m,k,_ in rows if k not in ('lunch','break'))==450
 return {1:(DAY_THEMES[1],rows)}
GLOSSARY=[('Grounding','Supplying accessible evidence for the current request.'),('Backlog','Selected work with Status neither Closed nor Cancelled.'),('Overdue','Backlog due strictly before the fixed reporting date.'),('Skill','Reusable instructions in a matching folder and SKILL.md file.'),('Snapshot','A dated, scoped copy of verified evidence.'),('Structured reference','A formula reference to a named Excel table or its columns.'),('Denominator','The population used to calculate a rate.'),('Proposed assignment','A suggested owner awaiting a real manager decision.')]
NEXT_STEPS=dict(title='Your Next Maintenance Report',items=['Use a copy and a new explicit reporting date.','Supply verified source/date/scope and test skill reruns.','Reconcile every claim and decision boundary.'])
LG_GLOSSARY=GLOSSARY
THANK_YOU=dict(title='Thank You',subtitle='Keep your maintenance evidence connected.')

# Full explanations remain in the LG; concise concept cards keep C34 slides readable.
for section in SECTIONS:
    first=section['definition'].split('. ')[0]+'.'
    why=section['why'].split('. ')[0]+'.'
    section['brief']=dict(what=first,why=why,check=section['example'][0],flow=dict(title=section['title'],steps=section['how']),prompts=['Name the source, reporting date and selected scope.','Explain the result using checked evidence.'],verify=section['example'][1:],try_title='Apply the Concept',try_head='PROMPT PRINCIPLES',check_head='EVIDENCE TO CHECK')
