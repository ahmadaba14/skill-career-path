# Career path: all-in-one instructions

Use this document whenever the user asks about their career path, where they can take their career, what to do next professionally, how to grow or pivot, which certifications, licences or degrees to pursue, or shares a resume or CV and wants direction. Works for any field and any country.

**How this single file works.** Everything the skill needs is below: the main instructions, then the rules for links and job posts, then one reference file per field. Wherever the instructions say `references/<name>.md`, read that section further down. You cannot run scripts in this mode, so give the Simpler view. If the user wants the Detailed view (an interactive graph), tell them it needs the full bundle with Python 3 (see its README), and offer to write the career data as JSON using the field list in the data-schema section so they can build it later.

---

# PART 1: Main instructions


# Career Path

Turn a resume and a few answers about what the person wants into a 10-year map of realistic routes, with one route recommended and explained. People ask this when they feel stuck or at a fork. A good answer shows real options, gives a clear opinion, and says what to study or earn at each step.

**Never guess about the person.** Do not assume their country, goals, limits, budget, family situation, willingness to move, retrain or manage people, or what they mean by a vague phrase. Take facts from what they said or wrote, and ask when something that would change the answer is unclear or missing. Asking costs one message; a wrong guess wastes the whole answer. Use only what the person has given you in this conversation (messages, attachments). Do not fill gaps from stored memory, earlier chats or the account profile, and do not state facts about them that they have not given, even as a question to confirm; ask the question neutrally instead. Licences, credentials, pay and job titles all depend on the country, so it always needs to be known.

## Workflow

1. Gather background (resume, current role, country).
2. Ask short questions about anything unclear, and which view they want. Do not research or build until the key answers are in.
3. Read the matching reference file, then research.
4. Build the paths, pick one, deliver in the chosen view.

### 1. Gather background

Look in the conversation for a resume, CV, LinkedIn text or attachment first, and read attachments before asking again. If nothing is there, ask for a paste or a few lines on current role, years of experience, skills, education, certifications and country. Pull out: current title, field, seniority, key skills, education, credentials held, location.

### 2. Ask first, then commit

Before researching, check what you actually know: country and city, current role and seniority, what they want from the next 10 years, and their limits (time, money, location, people management). Whatever is missing or ambiguous gets asked. The ask is 3 to 5 short questions in one numbered message, each answerable in a line. Add a question for anything else you would otherwise have to guess, such as an unclear job title, a gap or contradiction in the resume, or a goal that could mean two things. Pick from questions like these:

- Which parts of your work do you enjoy most, and which would you drop?
- Lead people, go deeper as a specialist, or run your own thing?
- Would you move city or country, or switch fields?
- How much time and money can you spend on study each year?
- What matters most in 10 years: income, impact, flexibility, stability, status?

Use a structured question or choice tool if your environment has one. Skip only the questions the person has clearly answered. Do not fill an unanswered question with your own guess. If their answers raise a new unclear point, ask one short follow-up round before building. If they tell you to go ahead without answering, proceed, but keep to what they said, list each unconfirmed point at the top as "not confirmed", and keep those points out of the recommended path where you can. In the same message ask which view they want:

- **Detailed view**: an interactive HTML graph with every branch, certifications and study at each step, and the best path highlighted. Uses more time and tokens.
- **Simpler view** (default if they do not choose): a short chat reply with one best path and a short list of others.

### 3. Research

Read the one reference file that fits the field (two for hybrids; `generic-fallback.md` if none fits, and tell the user the field has no dedicated reference yet). Reference files give the usual ladder, pivots, credentials, level gates and a "Role outlook" for the next 10 years. They go stale, so confirm the volatile parts online.

| Person's field | Read |
|---|---|
| UI/UX, product design, graphic, creative | `design-ux.md` |
| Software, data engineering, DevOps, QA, IT | `software-engineering.md` |
| Data science, analytics, ML/AI | `data-ai.md` |
| Product or program management | `product-management.md` |
| Finance, accounting, audit, banking | `finance.md` |
| HR, recruiting, people operations | `hr.md` |
| Marketing, content, brand | `marketing.md` |
| Sales, business development, customer success | `sales-bizdev.md` |
| Operations, supply chain, project management | `operations-supply-chain.md` |
| Doctors, dentists, vets | `medicine-and-surgery.md` |
| Nurses, midwives, physio, radiography, other allied health | `nursing-allied-health.md` |
| Pharmacy, biotech, pharma R&D, clinical research, regulatory | `pharmacy-life-sciences.md` |
| Health administration, informatics, public health | `healthcare.md` |
| Mechanical, electrical, civil, chemical, aerospace engineering | `engineering-physical.md` |
| Energy, environment, sustainability, ESG | `energy-environment.md` |
| Architecture, construction, surveying, planning | `architecture-construction.md` |
| Research scientists, academia (physics, chemistry, biology, maths) | `research-science.md` |
| Teaching, training | `education.md` |
| Law, compliance, policy | `legal-compliance.md` |
| Anything else, or a hybrid | `generic-fallback.md` |

All files are in `references/`. Also read `references/sources-and-providers.md` (link rules and official provider domains by field). Read `references/job-post-research.md` too; it sets the sample size and fetch budget for job posts.

**Keep research lean.** Send independent searches and fetches in the same turn rather than one at a time. Use the standard search mode, and prefer pages that list several postings. Stay inside the budget in `job-post-research.md`, and count it: stop researching after about 25 tool calls for the Detailed view or 12 for the Simpler view, and say what you could not check instead of searching further. Confirm only what is likely to have changed: credential names and fees, in-demand skills, local demand, and whether the roles on the ladder are growing or being replaced. When search results conflict with a reference file, trust the search and say so in a line. Do not invent salary figures; give a range labelled approximate or leave it out.

**Job posts.** Read 5 to 8 current postings in the person's market for each role in the first 5 years of the recommended path and the runner-up (Simpler view: the next one or two steps of the recommended path only). Count repeating requirements and use the counts for skills, certifications and the outlook label. Do not chase postings for roles beyond year 5; base them on the field reference, the level below and trend sources, and say so in the step's `jobPosts.note`.

**Links.** Every certification, course, degree or licence links to its exact official page, and every role and path has 1 to 3 sources. Follow `sources-and-providers.md`: deep links only, never a home page; never write a URL from memory; if you cannot verify a link, leave it out and say it is not verified. For licences and credentials use the person's own country's regulator or body.

### 4. Build the paths

Create 3 to 5 branches that differ in kind: **Deepen** (specialist), **Lead** (management), **Pivot** (adjacent field), **Build** (freelance, consulting, own venture), and optionally **Stretch** (a bold bet, such as another country or going back to school).

- Start every path from the person's real current position.
- Place steps from year 0 to year 10, role steps at least 1.5 years apart.
- Name the certifications, degrees, licences or courses that matter at each step, why, and the rough duration. Prefer those that postings in the person's market name. Do not pad. If a step needs none, say so.
- Fit each path to what they said. If they do not want to manage people, mark Lead a poor fit or leave it out and say why. Do not put a plan the person never mentioned (moving country, a degree, a switch of field, managing people, starting a business) into the recommended path. Other paths may explore them, marked as "only if you want this".
- Be honest about trade-offs and risks.
- **Plan for the roles of 2035.** Check every role against the "Role outlook" section and your web check. Do not park the person for years on a role likely to shrink; route through its successor or keep it as a short stepping stone. Label every role step growing, stable, evolving, declining or emerging, with one sentence on what changes and what replaces it.

Choose one recommended path by comparing paths against their goals, strengths, confirmed demand, how well the roles hold up to 2035, and study cost. Say why it wins and what would change the call. Name a runner-up.

## Output: Simpler view

Reply in chat, short and scannable:

1. **What I am relying on**, in one line: only what the person told you or wrote. Name anything not confirmed.
2. **Recommended path**: a one-line title, then 4 to 6 steps with years and the key certification or licence (as a link to its official page). Then 2 to 3 sentences of rationale tied to their answers. One line on how the roles change by year 10, naming any role likely to be replaced. One line on what the job posts asked for, with counts ("6 of 8 asked for X").
3. **Other paths**: exactly 2 to 4 one-line summaries (never more than 4; merge or drop the weakest).
4. A short "Sources:" list (at most 8 links, including at least one posting) after the main answer.
5. **Close with a question, as the last lines of the reply**: ask which other path they want opened up, and ask whether they want the detailed version, in these words or close to them: "Want the detailed version? It builds an interactive graph with every branch, the certifications and study for each step, and sources. It takes longer and uses more tokens." Do not build the graph until they say yes.

Do not build a graph. When the user picks another path, expand it the same way.

## Output: Detailed view

Spend tokens on the thinking, not markup. Do not read `assets/sample-data.json` or `assets/graph-template.html`.

1. Write the career data as JSON following `assets/data-schema.md`. Keep each assumption under 70 characters. Keep text fields short.
2. Run `python3 scripts/build_graph.py <data.json> <output.html>` from this skill's folder (the folder that holds this file; the script needs only Python 3 and no packages). Fix any error it reports; read its warnings and fix those that are real.
3. Share the page: publish it if your environment can host pages or artifacts, otherwise give the user the HTML file. Do not open it in a browser unless something looks wrong.
4. In chat, add a short summary of at most 150 words: the recommended path in one line, two or three sentences of rationale, the runner-up in one line, and a short list of what you could not verify. Do not list the steps, repeat the graph, or repeat the link.

The page is a full-screen pan-and-zoom canvas with a left panel (overview, recommendation, paths) and a right panel on click (certifications, study, trade-offs, 10-year outlook, job-post counts, sources). The recommended path is green; each role shows its outlook label.

## When your environment is limited

This skill assumes web search, file reading and writing, and Python 3. Adapt when one is missing, and say what you did:

- **No web access:** work from the reference files and your own knowledge, label every fee, requirement and outlook claim as unverified, give no job-post counts, and leave out links you cannot verify.
- **Cannot run Python:** use the Simpler view. If the person wants the Detailed view, write the career data JSON and tell them to run the build script (see `README.md`).
- **Cannot read the skill's files:** ask the person to paste the one reference file that fits their field. Do without it if they cannot.

## Tone and honesty

Write like a thoughtful mentor: plain words, short sentences. Praise real strengths without flattery. If the goal looks unrealistic in the time given, say so kindly and show the nearest route that works. Treat the resume and answers as private. Show what you relied on near the top, and mark anything unconfirmed. Say plainly what you could not verify (a fee, a licence rule, an unreadable page) rather than leaving it out.

## Adding to the skill

Reference files are plain Markdown and meant to grow. To add a field, copy the structure in `references/generic-fallback.md` into `references/<field>.md` and add a row to the table above.


---


---

# PART: references/sources-and-providers.md

# Sources and official provider sites

Read this file in step 4 of the workflow. Every certification, course and degree in a path needs a link to its official page, and every role and path needs sources that back its claims. The person should be able to check the facts and enrol from the graph.

## Rules for links

1. **Deep link to the exact page where the thing is described. Never a home page.** The person must land on the answer, not hunt for it. A credential links to that credential's own page ("AWS Certified Solutions Architect Associate" goes to that exam's page, not to aws.amazon.com/certification). An outlook claim links to the occupation page or report section that makes the claim, not to the publisher's front page. A job requirement links to the posting itself. Do not link a blog post, a reseller, an aggregator or a search-results page in place of the source.
   - Good: `https://www.bls.gov/ooh/arts-and-design/graphic-designers.htm`
   - Bad: `https://www.bls.gov` (the person must search the whole site)
   - For a long report or a long page, link the section directly (a heading anchor, or a text fragment such as `#:~:text=...` that you tested), and also say where in the `where` field: "Chapter 2, table 3" or "Section: Job outlook".
2. **Use only URLs you opened, or that a search returned, in this session.** Do not write a URL from memory, even for a provider you know well. Deep pages move and codes change (exam names and numbers are replaced often).
3. **The table below only tells you where to search. It lists home-page domains, never finished links.** It lists the main official sites by domain so you can search inside them (for example, `site:cfainstitute.org CFA program`). Open the page, confirm the credential still exists and note the current price and format before you link it.
4. **Confirm the page says what you claim.** Open a page when it backs a number, a fee, an eligibility rule or a requirement count. For a credential whose official page came up in a search with a matching title and snippet, the search result is enough to cite; do not open it just to look. **If you cannot verify a link, leave it out.** Say in the reply that the link is not verified yet. A missing link is better than a wrong one. Never invent a URL to fill a field.
5. **Back each role with 1 to 3 sources** for its outlook, requirements or typical scope, and include real job posts (see `references/job-post-research.md`). Good sources: a professional body page, a labour agency outlook page, a recent industry trend report, an official job-family description from a large employer. Prefer sources from the last 2 years for anything about AI and automation.
6. **Prefer primary sources** (the provider, the regulator, the agency) over commentary. Mark the source's date in the `note` field if it is older than 2 years.
7. **Check the person's country.** Licences and credentials differ by country. Link the local body when there is one (for example, the national accounting institute or the national regulator), not only the global one.

## Where to look: official sites by field

Domains are starting points for searching. Confirm every deep link before use.

### Cross-field outlook and labour data
| Source | Domain | Use for |
|---|---|---|
| World Economic Forum, Future of Jobs | weforum.org | Roles growing and shrinking, global |
| US Bureau of Labor Statistics, Occupational Outlook Handbook | bls.gov/ooh | Outlook, education, pay for US roles |
| O*NET | onetonline.org | Skills and tasks by occupation |
| National labour agency or ministry | (search for the person's country) | Local demand and licensing |
| Coursera and edX | coursera.org, edx.org | University-backed courses and degrees |

### Design and UX
| Provider | Domain |
|---|---|
| Google Career Certificates | grow.google/certificates |
| Nielsen Norman Group | nngroup.com |
| Interaction Design Foundation | interaction-design.org |
| IAAP (accessibility) | accessibilityassociation.org |

### Software, cloud, security, data
| Provider | Domain |
|---|---|
| AWS Certification | aws.amazon.com/certification |
| Microsoft credentials | learn.microsoft.com/credentials |
| Google Cloud certification | cloud.google.com/learn/certification |
| Linux Foundation (CKA, CKAD) | training.linuxfoundation.org |
| CompTIA | comptia.org |
| ISC2 (CISSP) | isc2.org |
| OffSec (OSCP) | offsec.com |
| ISACA (CISA, CISM) | isaca.org |
| Databricks | databricks.com |
| Snowflake | snowflake.com |
| The Open Group (TOGAF) | opengroup.org |

### Product, project, operations
| Provider | Domain |
|---|---|
| PMI (PMP, CAPM) | pmi.org |
| PeopleCert (PRINCE2) | peoplecert.org |
| Scrum.org | scrum.org |
| Scrum Alliance | scrumalliance.org |
| ASCM (CSCP, CPIM) | ascm.org |
| ASQ (Six Sigma) | asq.org |
| CIPS (procurement) | cips.org |

### Finance, audit, risk
| Provider | Domain |
|---|---|
| ACCA | accaglobal.com |
| ICAEW | icaew.com |
| AICPA and CIMA | aicpa-cima.com |
| CFA Institute | cfainstitute.org |
| GARP (FRM) | garp.org |
| The IIA (CIA) | theiia.org |
| IMA (CMA) | imanet.org |
| ACAMS (AML) | acams.org |
| ACFE (CFE) | acfe.com |

### HR and learning
| Provider | Domain |
|---|---|
| SHRM | shrm.org |
| HRCI | hrci.org |
| CIPD | cipd.org |
| WorldatWork | worldatwork.com |
| ATD | td.org |
| ICF (coaching) | coachingfederation.org |

### Marketing and sales
| Provider | Domain |
|---|---|
| HubSpot Academy | academy.hubspot.com |
| Google Skillshop | skillshop.withgoogle.com |
| CIM | cim.co.uk |
| Salesforce Trailhead | trailhead.salesforce.com |

### Legal and privacy
| Provider | Domain |
|---|---|
| IAPP (CIPP, CIPM, CIPT) | iapp.org |

### Health, science and engineering (examples; the person's own country's body comes first)
| Provider | Domain |
|---|---|
| NCSBN (NCLEX-RN) | ncsbn.org |
| USMLE, ACGME, ECFMG | usmle.org, acgme.org, ecfmg.org |
| UK GMC, NMC, HCPC, GPhC | gmc-uk.org, nmc.org.uk, hcpc-uk.org, pharmacyregulation.org |
| AHPRA (Australia) | ahpra.gov.au |
| Medical Council of Canada | mcc.ca |
| ACRP, SoCRA (clinical research) | acrpnet.org, socra.org |
| RAPS (regulatory affairs) | raps.org |
| NCEES (FE, PE) | ncees.org |
| Engineering Council (UK chartered) | engc.org.uk |
| IEEE, ASME | ieee.org, asme.org |
| RICS, RIBA, NCARB | rics.org, architecture.com, ncarb.org |
| AEE (energy manager) | aeecenter.org |
| GRI, IFRS Foundation (ISSB) | globalreporting.org, ifrs.org |
| Washington Accord signatories | ieagreements.org |

For healthcare, education, engineering and legal licensing, the right source is the person's own national regulator or professional body. Search for it by country. Do not guess it.


---

# PART: references/job-post-research.md

# Job-post research

Reference files describe roles in general. Job posts show what employers ask for now, in the person's market. Use a small, well-chosen sample: counts from 5 to 8 postings are enough to set requirements, and each extra posting costs tokens.

## Scope and budget

- **Detailed view:** 5 to 8 postings for each role in the first 5 years of the recommended path and the runner-up. 3 to 5 for the next step on each other path. At most about 20 page fetches in total.
- **Simpler view:** 5 to 6 postings for the next one or two steps of the recommended path only. At most about 8 page fetches in total.
- **Beyond year 5** (senior, director, executive), do not look for postings. They are rarely posted and thin samples mislead. Base those steps on the field reference, the level below and trend sources, and say so in `jobPosts.note`.
- If two roles on a path are close in level, one shared sample covers both.

## Method

1. **Pick the market.** Use the person's country and city, plus any country they said they might move to. Ask if you do not know. Do not assume a region; requirements and titles differ by market.
2. **Search once per role and market** (for example, "<role> job <city>"). Run the searches for different roles in the same turn. Prefer pages that list several postings with their requirements (employer careers pages, large boards, local boards found by search) so one fetch gives many postings. Boards that need a sign-in or block automated reading are off limits; use another source.
3. **Read only the requirements.** Open a posting only when the search snippet does not show its requirements. Do not open expired or duplicate postings.
4. **Extract and count.** For each posting note the title, years asked, must-have skills, certifications or licences, whether AI tools are mentioned, and stated pay if any. Then count repeats ("6 of 8 ask for X").
5. **Use the counts.** Requirements in most postings go into the role's skills and "what gets you here". A credential named in several postings goes on the step with its official link. New titles, missing old titles and new tools are evidence for the outlook label.
6. **Compare with the resume.** The gap between the resume and the counted requirements is the study plan for the next step.

## Recording the evidence

- Put the counts in the role node's `jobPosts` field (see `assets/data-schema.md`): postings reviewed, market, month, and the top 3 to 5 requirements with counts.
- Add 1 or 2 of the best postings to the node's `sources` with `kind: "job post"`, the exact URL and where the requirements sit.
- If you read fewer than 5 readable postings, say so in `jobPosts.note` and give the counts less weight. Many postings are old or undated; say that when it applies.

## Limits and care

- Do not use paid scraping or job-data tools unless the person asks for a larger study and accepts the cost.
- Summarise requirements in your own words. Do not copy posting text; if you quote, stay under 15 words.
- Do not collect names or emails of recruiters or hiring managers.
- Do not invent postings or counts. If you read 7, the data says 7.
- Pay: use it only when the posting states it, give the currency and period, and treat it as a range for that market.


---

# PART: references/architecture-construction.md

# Architecture, construction and the built environment

Architects, civil and structural engineers on building projects, quantity surveyors, construction managers, urban planners and facilities professionals. Licences differ by country; check the person's own.

## Typical ladder
- Architecture: Part 1 or graduate -> architectural assistant -> licensed architect -> senior or project architect -> associate or director -> partner
- Construction: Site engineer or assistant -> project engineer -> project manager -> senior PM or construction director -> head of delivery
- Surveying and cost: Graduate -> quantity surveyor -> senior -> commercial manager -> director
- Planning and urban design: Planner -> senior planner -> principal -> head of planning

## Common pivots
- **Architect to computational design, BIM or digital delivery**: needs scripting and BIM skills.
- **Design to project or development management**: needs commercial skills.
- **Construction to property development**: needs finance and legal basics.
- **Construction to sustainability, retrofit or energy**: needs building-physics knowledge.
- **Moving countries**: licences differ widely; check recognition, exams and experience rules.

## Credentials and learning
- Licences: architect registration by country (examples: NCARB and state boards, ARB in the UK), chartered bodies (RICS, CIOB, RIBA, ICE)
- Project: PMP, NEC and FIDIC contract training
- BIM and digital: Revit, Dynamo, ISO 19650 training
- Sustainability: LEED, BREEAM, Passivhaus designer

## What separates levels
- Graduate to licensed: logged experience hours and exams.
- Licensed to senior: owning projects and clients.
- Senior to partner: winning work and running the practice.

## Skills in demand
- Retrofit and low-carbon design
- BIM, digital twins, modular and offsite construction
- Cost and contract management

## Role outlook: next 10 years
- **Growing:** Retrofit and energy-efficiency specialists, BIM and digital delivery leads, infrastructure and water engineers, modular construction managers.
- **Evolving:** Generative tools draft layouts and drawings quickly; designers move to briefing, review and coordination. Sites adopt drones, sensors and digital twins.
- **Shrinking or being replaced:** Manual drafting, repeated take-off and routine coordination tasks. Successors are digital delivery and computational design roles.
- **Emerging:** Computational designer, offsite manufacturing engineer, building-performance analyst.
- **Planning rule:** Construction follows interest rates and public spending. Pair any path with a cycle-resistant skill (retrofit, infrastructure, digital delivery).

## Risks and watch-outs
- Cyclical; layoffs in downturns.
- Long licensing routes and low early pay in architecture.


---

# PART: references/data-ai.md

# Data and AI

Covers data analysis, business intelligence, data science, data engineering, machine learning and AI engineering.

## Typical ladder
- Analyst track: Data analyst -> Senior analyst -> Analytics lead -> Head of analytics -> Chief data officer
- Data science: Data scientist -> Senior -> Staff -> Principal; or lead -> manager -> director
- Data engineering: Data engineer -> Senior -> Staff/architect -> Head of data platform
- ML / AI engineering: ML engineer -> Senior -> Staff -> Principal or head of AI; research scientist track for PhD-level work

## Common pivots
- **Analyst to data scientist or analytics engineer**: add statistics, Python and modelling or dbt-style engineering.
- **Software engineer to ML/AI engineer**: add ML fundamentals and evaluation skills.
- **Data to product management**: transfers metrics sense; needs product discovery.
- **Data to consulting or strategy**: transfers analysis; needs communication.
- **Domain expert to data role** (finance, health, marketing): domain depth is the edge.

## Credentials and learning
Verify names, fees and relevance before recommending; this field changes quickly.
- Cloud data certs: AWS Data Engineer / ML Specialty, Azure DP-203 / AI-102 (check current codes), Google Professional Data Engineer / ML Engineer
- Databricks and Snowflake certifications for platform roles
- BI tools: Power BI (PL-300), Tableau certifications
- Statistics and ML: university-level courses, open courseware, and a few real projects
- Master's or PhD: useful for research and some ML roles, and for skilled-migration routes; not required for most analyst or engineering roles.

## What separates levels
- Junior to mid: delivers accurate analysis or pipelines from a clear brief.
- Mid to senior: frames the problem, chooses methods, and makes stakeholders act on the result.
- Senior to staff: sets technical direction and standards across teams.
- Lead to head: owns data strategy, governance and the business case for data work.

## Skills in demand
- SQL and Python, at depth
- Data modelling and pipeline reliability
- LLM application building, evaluation, and safety
- Experimentation and causal thinking
- Communication: turning results into decisions

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** AI/ML engineering, data engineering, AI evaluation and safety, analytics engineering, data governance and privacy.
- **Evolving:** Data analysts become decision analysts using natural-language BI tools. The data scientist title splits into applied ML, experimentation and causal analysis, and AI engineering.
- **Shrinking or being replaced:** Dashboard-and-report-only analyst roles, basic modelling roles, and manual data cleaning or labelling. Their successors are analytics engineers and decision scientists who frame the question and own the answer.
- **Emerging:** LLM evaluation and red-team specialist, AI product analyst, data-for-AI engineer, AI governance analyst, synthetic data specialist.
- **Planning rule:** Favour paths that move toward problem framing, engineering depth or domain expertise. Pure reporting paths should be flagged.

## Risks and watch-outs
- "Data scientist" titles are inconsistent across companies; read the actual job content.
- Basic reporting and simple modelling are increasingly automated; framing and engineering depth gain value.
- Entry roles are competitive; real projects with real data help more than course lists.


---

# PART: references/design-ux.md

# Design / UX

Covers UI/UX, product design, visual and brand design, design systems, and design engineering.

## Typical ladder
- Individual-contributor track: Junior designer -> Designer -> Senior designer -> Staff designer -> Principal designer (about 2 to 4 years per step)
- Lead track: Senior designer -> Design lead -> Design manager -> Head/Director of design -> VP Design / Chief Design Officer
- Specialist tracks: Design systems designer, UX researcher, content designer, interaction/motion designer, accessibility specialist
- Hybrid track: Design engineer / UX engineer (design plus production frontend code)

## Common pivots
- **Product management**: transfers user empathy and product sense; needs metrics, roadmapping and stakeholder work.
- **Design engineering / frontend engineering**: transfers component thinking and craft; needs strong JavaScript/TypeScript, framework and testing skills.
- **UX research**: transfers user focus; needs research methods and some statistics.
- **Design systems lead**: transfers consistency and tokens thinking; needs governance and engineering partnership.
- **Brand / creative direction**: transfers visual craft; needs storytelling and team leadership.
- **Freelance / studio**: transfers delivery skills; needs sales, pricing, contracts.
- **AI product design**: transfers interaction design; needs fluency with AI behaviours, prompting and evaluation of AI outputs.

## Credentials and learning
Design hiring rewards portfolios far more than certificates. Credentials help most for career changers and for roles in large or regulated organisations. Verify current names, prices and availability before recommending.
- Google UX Design Certificate: good entry signal for career changers; weak signal for experienced designers.
- Nielsen Norman Group UX Certification: respected by practising designers; paid per course, adds up.
- Interaction Design Foundation courses: affordable way to fill theory gaps.
- Accessibility: IAAP certifications (for example, CPACC / WAS) help for accessibility-focused roles and regulated sectors.
- Frontend skills: official framework docs and a few shipped projects count for more than a certificate.
- Product skills: product management courses or PSPO/CSPO-type certifications help for the PM pivot.
- Master's in HCI or design: worth it for research roles, some countries' skilled-migration points, or academic routes; rarely needed for craft growth.

## What separates levels
- Junior to mid: ships polished screens without close guidance.
- Mid to senior: owns an end-to-end problem, shows measurable outcomes, explains decisions to non-designers.
- Senior to staff/lead: shapes the problem itself, sets standards across teams, grows other designers.
- Lead to director: owns strategy, hiring, budget and the design team's relationship with the business.

## Skills in demand
- Design systems and design tokens at scale
- Design-to-code fluency (HTML/CSS, React, component libraries)
- Data-informed design (reading analytics, running experiments)
- AI-assisted workflows and designing AI-powered interfaces
- Accessibility (WCAG) and inclusive design
- Complex product areas: dashboards, B2B SaaS, enterprise, fintech, health

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** design systems and design engineering, accessibility, UX research tied to business decisions, service design for complex products, AI product and interaction design.
- **Evolving:** The UI designer who only produces screens becomes a product designer who prototypes in code and directs AI tools. UX writer becomes content designer who shapes how AI products speak and behave. Researchers move from running every study by hand to designing studies that AI helps analyse.
- **Shrinking or being replaced:** Screens-only UI production, pixel and asset production, basic wireframing and layout work, and entry roles built around those tasks. Their successors are product designers and design engineers who orchestrate AI generation and own quality.
- **Emerging (next 3 to 10 years):** AI interaction / agent experience designer, design technologist, behaviour and prompt designer, design ops with AI governance, voice and spatial interface designer (slower to mature).
- **Planning rule:** Expect "designer" to include prototyping in code and judging AI output by year 5. A 10-year path that ends in a pure visual-production role needs a flag.

## Risks and watch-outs
- Entry-level design roles are crowded; a strong portfolio and real project work matter more than courses.
- Generic visual-only roles are the most exposed to AI tooling; research, systems, strategy and engineering overlap are safer.
- Design leadership roles are scarce; many strong designers stay senior ICs by choice, which is a good path.
- Agency, in-house and startup careers differ in pace and pay; ask the person which they prefer.


---

# PART: references/education.md

# Education, academia and training

Covers school teaching, higher education, academic research, corporate training and instructional design, and education technology.

## Typical ladder
- School: Teacher -> Senior teacher / head of department -> Vice principal -> Principal -> District or system leadership
- Higher education: Lecturer / assistant professor -> Associate professor -> Professor -> Dean or department chair -> Provost or president
- Research: Postdoc -> Research fellow / assistant professor -> Principal investigator -> Research director
- Corporate training: Trainer -> Senior trainer -> L&D manager -> Head of learning
- Instructional design: Designer -> Senior designer -> Lead -> Head of learning experience

## Common pivots
- **Teacher to instructional design or edtech**: transfers pedagogy; needs tools, project and product skills.
- **Academic to industry research or data roles**: transfers methods; needs applied portfolio and industry vocabulary.
- **Teacher to school leadership**: needs management and policy skills.
- **Teacher to corporate L&D**: transfers teaching craft; needs business context.
- **Educator to curriculum, content, or product roles**: transfers subject depth.

## Credentials and learning
Requirements are mostly regulated and local. Verify teaching licensure, degree equivalence and accreditation rules for the person's country.
- Teaching licence or certification in the home system, plus international options (for example, PGCE, IB or Cambridge training)
- Master's and PhD for higher education and research; check which journals and publications matter in the field
- Instructional design: ATD certifications, ID certificate programs, and a portfolio of learning projects
- Educational leadership qualifications for principal tracks
- Learning technology skills: authoring tools and learning platform administration.

## What separates levels
- Teacher to senior: improves others' teaching as well as one's own results.
- Senior to leader: manages staff, budgets and school culture.
- Academic ranks: publications, grants and teaching records decide promotion.
- Corporate learning: ability to link learning to business results.

## Skills in demand
- Digital and blended learning design
- Data use for learner outcomes
- AI literacy and AI-assisted teaching and content design
- Assessment design
- Grant writing and research funding skills

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** Learning experience design, special education, vocational and skills training, learning analytics, edtech product roles, AI-literate teaching.
- **Evolving:** Teachers become facilitators and mentors who use AI tutors. Lecturers move toward blended delivery. L&D moves toward skills architecture and credentialing.
- **Shrinking or being replaced:** Rote content delivery and basic tutoring, administrative grading roles, and some traditional course-development roles. Their successors are learning designers and coaches who work with AI tools.
- **Emerging:** AI learning designer, learning data analyst, AI pedagogy specialist, micro-credential designer.
- **Planning rule:** Human mentoring, assessment design and subject depth stay valuable. Flag paths that rely only on delivering standard content.

## Risks and watch-outs
- Academic jobs are scarce in many fields; be honest about odds and show industry alternatives.
- Pay in public education is often fixed by scale; leadership or industry moves change income more than seniority.
- International moves often need local licensing or recognition.


---

# PART: references/energy-environment.md

# Energy, environment and sustainability

Energy engineers and analysts, environmental scientists and consultants, sustainability and ESG roles, climate and water professionals. Policy and funding shape demand, so check the person's country.

## Typical ladder
- Technical: Analyst or graduate engineer -> engineer or consultant -> senior -> principal or technical lead -> head of discipline
- Sustainability: Coordinator or analyst -> manager -> senior manager -> head or director of sustainability -> chief sustainability officer
- Consulting: Analyst -> consultant -> senior consultant -> manager -> principal or partner
- Energy trading and markets: Analyst -> trader or originator -> senior -> head of desk

## Common pivots
- **Oil, gas or maritime to renewables, grid or hydrogen**: transfers process, safety and project skills; needs power-system or renewable knowledge.
- **Environmental science to ESG reporting or climate risk**: needs reporting standards and data skills.
- **Engineering to energy consulting or policy**: needs economics and writing.
- **Sustainability to finance** (green finance, climate risk): needs finance basics.
- **Operations to energy management**: needs ISO 50001 style training.

## Credentials and learning
- Energy: Certified Energy Manager (AEE), PE or chartered status, EIT bodies, power-system and renewables courses
- ESG and reporting: GRI, ISSB and CSRD training, GHG Protocol courses, FSA credential from SASB or IFRS Foundation, CFA ESG certificate
- Environmental: professional registration in the person's country (examples: CEnv in the UK), GIS and modelling skills
- Master's in energy systems, environmental management or sustainability; MBA for leadership.

## What separates levels
- Analyst to manager: owning a client or reporting cycle with defensible numbers.
- Manager to head: strategy, budget and board influence; regulation and data governance.

## Skills in demand
- Carbon accounting and climate data
- Grid integration, storage and renewables project development
- Energy efficiency and building decarbonisation
- Regulatory reporting (CSRD, ISSB, national schemes)

## Role outlook: next 10 years
- **Growing:** Renewable project development, grid and storage engineering, energy efficiency, carbon accounting, climate risk analysis.
- **Evolving:** ESG reporting moves from voluntary to regulated, which makes it compliance-heavy and data-heavy. Fossil-fuel roles shift to transition roles, at different speeds in different regions.
- **Shrinking or being replaced:** Narrow voluntary-report writing and some fossil-fuel operations roles. Successors are regulated reporting, data and transition roles.
- **Emerging:** Hydrogen economy roles, carbon removal engineer, climate data scientist, nature and biodiversity analyst.
- **Planning rule:** Demand follows policy and funding, so it varies by country and election cycle. Check current rules, and prefer roles that serve both regulation and cost savings.

## Risks and watch-outs
- Policy change can slow or stop projects; prefer paths with several employer types.
- ESG job titles have been cut in some markets; check postings.


---

# PART: references/engineering-physical.md

# Engineering (mechanical, electrical, civil, chemical, aerospace and similar)

Physical-world engineers. Software engineers use `software-engineering.md`. Chartered or professional licences matter in some fields and countries, so check them.

## Typical ladder
- Individual-contributor track: Graduate or junior engineer -> engineer -> senior engineer -> principal or technical specialist -> fellow or chief engineer
- Management track: Engineer -> team lead -> engineering manager -> department head -> director or VP of engineering
- Project track: Engineer -> project engineer -> project manager -> programme manager -> director
- Licensed track (civil, structural, electrical power and others): graduate -> licence (PE, chartered engineer or equivalent) -> signing engineer -> principal

## Common pivots
- **Engineer to project or programme management**: needs PM training (PMP or equivalent).
- **Engineer to energy, sustainability or climate roles**: needs a domain update.
- **Engineer to data, automation or digital engineering**: needs coding, simulation or controls skills.
- **Engineer to product or technical sales**: needs commercial skills.
- **Engineer to consulting or owner's engineer**: needs breadth and a licence.
- **Moving countries**: licences and accreditations recognise each other only partly (Washington Accord helps for degrees); check each target country.

## Credentials and learning
- Licences: FE and PE (US), chartered engineer through Engineering Council bodies (UK), registered engineer schemes elsewhere. Verify with the licensing body.
- Project and quality: PMP, Six Sigma, safety certifications
- Domain: functional safety, HVAC, power systems, process safety, structural design software
- Digital: CAD, simulation, MATLAB or Python, PLC and controls
- Master's for specialist or research roles; MBA for management.

## What separates levels
- Junior to engineer: working independently within standards.
- Engineer to senior: owning a design or system and its risks.
- Senior to principal: technical authority, sign-off and mentoring.
- Engineer to manager: people, schedule and budget.

## Skills in demand
- Electrification, power systems, batteries, grid, renewable energy
- Automation, robotics, controls, digital twins
- Simulation, data skills, AI-assisted design

## Role outlook: next 10 years
- **Growing:** Power and grid engineers, electrification and battery engineers, renewable energy, automation and controls, infrastructure and water, semiconductor manufacturing.
- **Evolving:** Generative design and simulation tools speed routine drawing and analysis; engineers spend more time on requirements, verification and judgement. Digital twins change maintenance work.
- **Shrinking or being replaced:** Manual drafting and routine calculation roles; some fossil-fuel plant roles in regions phasing them out. Successors are design-automation and energy-transition roles.
- **Emerging:** Hydrogen and carbon capture engineer, battery systems engineer, robotics integrator, AI-assisted design lead.
- **Planning rule:** Engineering roles tied to regulation and physical safety are stable; use the growth fields as the destination, and say which industry the person ends up in.

## Risks and watch-outs
- Industry cycles (oil, construction, aerospace) cause layoffs; keep skills portable.
- Licences are national; moving countries may need extra exams or years.


---

# PART: references/finance.md

# Finance

Covers accounting, audit, corporate finance and FP&A, banking, investment management, risk, and fintech.

## Typical ladder
- Corporate finance: Analyst -> Senior analyst -> Finance manager -> Senior manager / Controller -> Finance director -> VP Finance -> CFO
- Accounting / audit: Associate -> Senior -> Manager -> Senior manager -> Partner (in a firm), or Controller -> CFO (in industry)
- Banking / investment: Analyst -> Associate -> VP -> Director -> Managing director (steps are tied to fixed cycles at many banks)
- Asset management: Research analyst -> Senior analyst -> Portfolio manager -> Chief investment officer
- Risk and compliance: Analyst -> Risk manager -> Head of risk -> Chief risk officer

## Common pivots
- **Audit to industry finance**: very common after 3 to 5 years; transfers rigour and controls knowledge.
- **Finance to data/analytics**: transfers modelling; needs SQL, Python, BI tools.
- **Finance to strategy or consulting**: transfers analysis; needs structured problem solving and often an MBA.
- **Finance to fintech product**: transfers domain knowledge; needs product skills.
- **Accounting to tax, forensic, or advisory**: transfers standards knowledge; needs specialist training.

## Credentials and learning
Credentials carry unusual weight in finance. Many are licences or gates for promotion. Verify exam structure, fees and local equivalents before recommending, since requirements differ by country.
- Accounting: CPA (US), ACCA, ICAEW ACA, CA (various countries), CMA for management accounting
- Investment: CFA (three levels, multi-year commitment), FRM for risk, CAIA for alternatives
- Treasury and corporate finance: CTP, and ACCA/CMA coursework
- Internal audit and controls: CIA, CISA, CRMA
- Financial planning: CFP
- Compliance: ACAMS (AML), and local regulatory exams
- Skills: advanced Excel and financial modelling certificates, SQL, Python, Power BI/Tableau
- MBA: helps for the move into senior leadership, strategy, or a change of industry; less useful for a pure technical career with CFA/CPA.

## What separates levels
- Analyst to senior: accuracy, speed, and independent work on models and reports.
- Senior to manager: reviews others' work and owns a deliverable with stakeholders.
- Manager to director: owns planning and business partnering, not only reporting.
- Director to CFO: capital allocation, investor/board relationships, and strategy.

## Skills in demand
- Financial modelling and FP&A with automation
- Data analysis (SQL, Python) and BI
- ESG and sustainability reporting
- Regulatory knowledge: IFRS/GAAP, AML, local rules
- Finance automation and AI-assisted analysis

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** FP&A business partnering, risk and model governance, sustainability reporting and assurance, financial data and analytics, regulatory technology, AI governance in finance.
- **Evolving:** Accountants shift toward advisory and controls over automated systems. Analysts review AI-drafted analysis rather than building every model by hand. Auditors audit algorithms and continuous data feeds, not only samples.
- **Shrinking or being replaced:** Data-entry bookkeeping, accounts payable/receivable processing, basic reconciliation, routine tax preparation, junior reporting roles, and some branch banking roles. Their successors are finance automation leads and analysts who handle exceptions and judgement.
- **Emerging:** Finance automation lead, AI model risk specialist, sustainability assurance specialist, FinOps (cloud cost) analyst, financial data product manager.
- **Planning rule:** Credentials such as CPA, ACCA and CFA stay valuable for judgement and sign-off roles. Check that a path adds analytics or advisory skill, not only compliance processing.

## Risks and watch-outs
- Credentials take years and cost real money; confirm the employer or market values them before committing.
- Routine bookkeeping and reporting are being automated; analysis, judgement and advisory work hold value.
- Banking has long hours and up-or-out cycles; ask about lifestyle priorities.
- Licences may not transfer across countries; check recognition if the person might move.


---

# PART: references/generic-fallback.md

# Generic fallback (and template for new reference files)

Use this file when the person's field has no dedicated reference, or as the template when adding one. Every field file follows the same sections so the skill can read any of them the same way.

## How to build paths for an unfamiliar field

1. Find the field's usual ladder with a quick web search ("[field] career ladder", "[field] job levels"). Look at 2 or 3 employers' public job families if you can.
2. Identify the **gate** at each level: the thing that decides if someone moves up (a licence, a portfolio, a team to lead, a revenue number, a published result).
3. Look for **adjacent fields** that reuse at least half of the person's skills. These make the best pivots.
4. Check which **credentials** employers actually ask for in job ads in the person's market. Skip the rest.
5. Note the **risks**: shrinking demand, automation, licensing barriers, saturated entry levels.
6. Work out the **10-year outlook** for each role on the ladder (see "Role outlook" below). Search for recent reports on how AI and automation affect the field ("[field] jobs future", "[field] roles automation", the WEF Future of Jobs report, national labour agency forecasts). Sort every role into growing, evolving, shrinking or emerging, and name the successor of any role that is shrinking.

## Reference file template

```
# <Field>

## Typical ladder
- Individual-contributor track: level -> level -> level (typical years at each)
- Lead / management track: level -> level -> level
- Executive ceiling: what the top role is called

## Common pivots
- Adjacent field: what transfers, what must be learned

## Credentials and learning
- Credential: who values it, rough cost and time, when it pays off
- (Always tell the skill to verify names, prices and availability on the web)

## What separates levels
- Junior to mid, mid to senior, senior to lead: the real gate at each

## Skills in demand
- Short list, with the shift happening now (for example, AI tooling)

## Role outlook: next 10 years
- Growing: roles with rising demand
- Evolving: role -> how the work changes (what the person will do differently)
- Shrinking or being replaced: role -> the role that replaces it
- Emerging: new roles that do not exist at scale yet
- Planning rule: what a 10-year path in this field must include to stay safe

## Risks and watch-outs
- Honest downsides of the field or its common paths
```

## Generic timing guide

Use these only when nothing field-specific is known. They are rough and vary by company and country.

- Entry to mid-level: 2 to 3 years
- Mid-level to senior: 3 to 5 years
- Senior to lead or manager: 2 to 4 years
- Lead to director: 4 to 6 years
- A pivot into a new field usually costs 1 to 2 years of seniority, then catches up faster than a fresh start.

## Generic credential guidance

- A degree matters most at the start of a career and at the point of switching to a regulated field.
- A professional certification pays off when job ads ask for it by name, or when it is a licence.
- A portfolio or a shipped result usually beats a certificate in creative and technical fields.
- A part-time master's or MBA makes sense for a move into senior management or a new industry, and rarely for a deepening move in a skilled craft.

## Judging the outlook of a role

Use these questions when the field file has no answer:
- Is the core task routine, rule-based and done on a screen? That work is the most exposed to automation.
- Does the role depend on judgement, trust, physical presence, regulation or accountability? That work holds up better.
- Does the role grow when AI is adopted (building, supervising, auditing and governing AI)? Those roles are likely to grow.
- Who is the likely successor? Name it. A person in a shrinking role needs a bridge to the successor, not a warning alone.
- How fast could change happen here? Regulated fields (health, law, education) move slower than software or marketing. Say so.


---

# PART: references/healthcare.md

# Healthcare

Covers non-clinical and system-level health roles (administration, health informatics, public health, digital health, health policy), and is the general overview for health. Clinical roles have their own files: `medicine-and-surgery.md`, `nursing-allied-health.md`, `pharmacy-life-sciences.md`. Health is licensed and regulated, so rules differ sharply by country. Always check the person's country and licensing body before recommending anything.

## Typical ladder
- Nursing: Registered nurse -> Senior/charge nurse -> Nurse manager -> Director of nursing -> Chief nursing officer; clinical specialist or nurse practitioner as a clinical branch
- Pharmacy: Pharmacist -> Clinical or senior pharmacist -> Pharmacy manager -> Director of pharmacy; industry roles (regulatory affairs, medical affairs)
- Medicine: Residency / specialty training -> Consultant/attending -> Department head -> Medical director -> Chief medical officer
- Administration: Coordinator -> Manager -> Director -> Hospital or health-system executive
- Health informatics: Analyst -> Informatics specialist -> Lead -> Chief medical informatics officer

## Common pivots
- **Clinical to health informatics or digital health**: transfers clinical insight; needs data and systems skills.
- **Clinical to industry** (pharma, devices, medical affairs): transfers clinical knowledge; needs industry exposure.
- **Clinical to administration or leadership**: needs management and finance training.
- **Clinical to teaching or research**: needs advanced degrees.
- **Clinical to consulting or health policy**: needs analytical skills.

## Credentials and learning
Credentials are licences and regulated specialties; follow local rules exactly and verify them on the regulator's site.
- Specialty certifications from national boards or colleges
- Advanced practice qualifications (nurse practitioner, clinical specialist)
- Master's in public health (MPH), health administration (MHA), or health informatics
- Quality and safety: Lean, Six Sigma Healthcare, patient safety courses
- Leadership programs for clinical managers
- MBA with a health focus for executive tracks.

## What separates levels
- Early to experienced clinician: independent judgement and consistent outcomes.
- Clinician to leader: managing people, budgets and quality, not only patients.
- Leader to executive: system-level strategy, regulation and finance.

## Skills in demand
- Digital health, telemedicine, and clinical data skills
- Care coordination and quality improvement
- Leadership and change management
- Specialised clinical skills in areas with shortages
- Understanding of AI tools in clinical workflows

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** Nursing and allied health (ageing populations), geriatrics, mental health, clinical informatics, genomics and precision medicine, home care and remote monitoring.
- **Evolving:** Clinicians use AI for documentation and decision support. Radiology and pathology shift toward AI-supervised reading. Pharmacists move toward clinical roles as dispensing becomes automated.
- **Shrinking or being replaced:** Medical transcription, manual coding and billing, routine admin and scheduling, some dispensing tasks. Their successors are health data and informatics specialists.
- **Emerging:** Clinical AI governance and safety lead, digital health product roles, remote care coordinator, health data engineer, expanded genetic counselling.
- **Planning rule:** Healthcare changes more slowly because of regulation and licensing. Say so, and avoid predicting fast disappearance of licensed clinical roles.

## Risks and watch-outs
- Licensing barriers make moves across countries slow and costly; check recognition and exam requirements early.
- Burnout is real in clinical roles; ask about workload tolerance as part of the interview.
- Give no medical advice in this skill; it only covers career direction.


---

# PART: references/hr.md

# HR / People

Covers generalist HR, recruiting and talent acquisition, compensation and benefits, learning and development, HR operations and analytics, and organisational development.

## Typical ladder
- Generalist track: HR coordinator -> HR generalist -> HR business partner -> Senior HRBP -> Head of HR -> CHRO
- Talent acquisition: Recruiter -> Senior recruiter -> TA lead -> Head of talent -> VP People
- Specialist tracks: Compensation and benefits analyst -> manager -> director; L&D specialist -> manager -> head of learning; People analytics analyst -> lead
- Operations track: HR operations / HRIS analyst -> manager -> director of people operations

## Common pivots
- **HR to people analytics / data**: transfers domain knowledge; needs SQL, statistics, BI.
- **HR to organisational development or change management**: transfers people insight; needs consulting skills.
- **Recruiting to sales or business development**: transfers persuasion and pipeline habits.
- **HR to operations or general management**: transfers people leadership; needs P&L experience.
- **HR to consulting or fractional HR**: transfers expertise; needs a network and sales skills.
- **HR to HR-tech product**: transfers user knowledge; needs product skills.

## Credentials and learning
Verify names, fees and local recognition before recommending.
- SHRM-CP / SHRM-SCP (US-centric, widely recognised)
- HRCI: PHR / SPHR / GPHR
- CIPD (UK, Ireland, parts of Asia, Middle East and Africa), Levels 3 to 7
- Local labour-law and professional body qualifications
- Compensation: WorldatWork credentials (CCP)
- L&D: ATD certifications (CPTD)
- Coaching: ICF credentials
- People analytics: courses in SQL, Python, Power BI/Tableau
- Master's in HRM, organisational psychology, or an MBA: helps for senior leadership and consulting.

## What separates levels
- Coordinator to generalist: handles the full employee lifecycle without hand-holding.
- Generalist to HRBP: advises leaders using data, not only process knowledge.
- HRBP to head of HR: designs people strategy tied to business goals; handles hard employee relations and legal risk.
- Head to CHRO: board-level influence, culture, workforce planning and cost.

## Skills in demand
- People analytics and workforce planning
- HR technology and automation (HRIS, ATS, AI-assisted screening with fairness checks)
- Employment law and compliance in the person's country
- Change management and organisational design
- Skills-based hiring and internal mobility

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** People analytics, workforce and skills planning, employee experience, employment law and AI-in-hiring compliance, reskilling and L&D.
- **Evolving:** Recruiters become sourcing and assessment strategists who work alongside AI screening. HR generalists become HR partners supported by self-service tools and AI assistants. L&D moves from course delivery to skills architecture.
- **Shrinking or being replaced:** HR admin and ticket handling, resume screening, interview scheduling, payroll data entry, basic helpdesk. Their successors are HR operations and automation owners and people analysts.
- **Emerging:** Skills and workforce strategist, HR automation / HRIS product owner, algorithmic fairness auditor for hiring, internal talent marketplace manager.
- **Planning rule:** Strong paths add data skill and business partnering by mid-career. Pure administrative HR paths need a flag.

## Risks and watch-outs
- Administrative HR work is being automated; strategic, advisory and analytical skills protect a career.
- Credentials vary by region; a UK-style CIPD path may mean little in a market that prefers SHRM.
- HR sometimes struggles to show business impact; paths that build measurable results (retention, time-to-hire, cost) move faster.


---

# PART: references/legal-compliance.md

# Law, compliance and policy

Covers practising lawyers, in-house counsel, paralegals, compliance and risk officers, privacy and data protection, and public policy. Law is licensed and local. Check the person's jurisdiction and bar or regulator rules before recommending anything.

## Typical ladder
- Law firm: Associate -> Senior associate -> Counsel -> Partner
- In-house: Legal counsel -> Senior counsel -> Head of legal / deputy general counsel -> General counsel -> Chief legal officer
- Compliance: Analyst -> Compliance officer -> Compliance manager -> Head of compliance -> Chief compliance officer
- Privacy / data protection: Analyst -> Privacy officer -> Data protection officer -> Head of privacy
- Policy: Analyst -> Senior policy adviser -> Director of policy

## Common pivots
- **Law firm to in-house**: common after 4 to 7 years; needs business sense and cost awareness.
- **Lawyer to compliance, privacy, or AI governance**: transfers legal analysis; needs operational frameworks.
- **Lawyer to contracts and commercial management, or legal operations**: needs process and tools skills.
- **Lawyer to policy, government, or advocacy**: needs political and public-affairs skills.
- **Lawyer to business or founder roles**: needs commercial experience.

## Credentials and learning
Verify local qualifications and recognition before recommending.
- Law degree and bar or licensing exams in the jurisdiction; routes to qualify abroad (for example, via conversion exams) are slow and costly
- LLM for specialisation or for a pathway to another jurisdiction
- Privacy: IAPP certifications (CIPP, CIPM, CIPT)
- Compliance: CAMS, CCEP, CFE
- AI governance and risk: emerging certificates and frameworks; verify quality before recommending
- Legal tech and legal operations short courses.

## What separates levels
- Junior to senior associate: independent work with fewer corrections.
- Senior to partner or head: originating clients or owning company-wide legal risk, plus leadership.
- Compliance roles: building programs and regulator relationships, not only checking rules.

## Skills in demand
- Data protection and AI regulation
- Contract automation and legal technology
- Commercial and business judgement
- Regulatory expertise in fast-moving areas (fintech, health, crypto, AI)
- Clear writing for non-lawyers

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** Privacy, AI governance and regulation, compliance in fintech and health, legal operations, contract management, ESG compliance.
- **Evolving:** Research and first-draft review are increasingly automated. Lawyers focus on judgement, negotiation and client advice. Paralegals move toward legal technology and operations.
- **Shrinking or being replaced:** Document review, routine contract drafting, basic legal research, and manual compliance sampling. Their successors are legal technologists and algorithmic compliance auditors.
- **Emerging:** AI governance counsel, legal engineer / legal technologist, algorithmic compliance auditor, privacy engineer.
- **Planning rule:** Licensing keeps core legal roles protected, but the junior pipeline is changing. Show how the person builds judgement-heavy experience early.

## Risks and watch-outs
- Qualifications rarely transfer between countries without extra exams.
- Law-firm hours and partnership odds are tough; present in-house and compliance routes as real alternatives.
- This skill gives career direction only, not legal advice.


---

# PART: references/marketing.md

# Marketing

Covers brand, content, performance and growth marketing, SEO, product marketing, communications and PR.

## Typical ladder
- Generalist: Coordinator -> Specialist -> Manager -> Senior manager -> Director -> VP Marketing -> CMO
- Performance / growth: Specialist -> Growth manager -> Head of growth -> VP Growth
- Content / SEO: Writer or SEO specialist -> Senior -> Content or SEO lead -> Head of content
- Product marketing: PMM -> Senior PMM -> Director of PMM -> Head of marketing
- Comms / PR: Associate -> Account manager -> Director of communications

## Common pivots
- **Marketing to product management**: transfers customer insight; needs product discovery and technical fluency.
- **Marketing to data / analytics**: transfers measurement mindset; needs SQL and analytics tools.
- **Marketing to sales or revenue operations**: transfers funnel knowledge.
- **Content to UX writing or content design**: transfers writing craft.
- **Agency to in-house, or in-house to freelance**: changes pace, pay and risk.

## Credentials and learning
Results and portfolios count most. Verify names and fees before recommending.
- Google Ads and Analytics certifications (check the current GA4 offerings)
- Meta Blueprint
- HubSpot Academy certifications (low cost, widely recognised for inbound)
- CIM qualifications (UK-centred), and local professional body awards
- SEO and analytics tool certifications
- MBA or a master's in marketing: useful for CMO tracks or a change of industry.

## What separates levels
- Specialist to manager: runs campaigns independently and ties them to results.
- Manager to director: owns budget, team and strategy, not only execution.
- Director to CMO: connects marketing to revenue and brand at the company level.

## Skills in demand
- Measurement and attribution
- AI-assisted content and creative workflows, with editorial quality control
- Lifecycle and retention marketing
- Product-led growth
- Brand strategy in crowded markets

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** Brand strategy, product marketing, lifecycle and CRM, marketing analytics, community and creator partnerships, optimisation for AI answer engines.
- **Evolving:** Content marketers become editors and strategists who direct AI drafts and add original insight. SEO expands into search plus AI-answer visibility. Performance marketers become creative strategists and automation managers as ad platforms automate bidding.
- **Shrinking or being replaced:** High-volume copy production, routine social posting and scheduling, manual media buying and bid management, stock imagery and basic graphic production. Their successors are brand strategists and marketing automation engineers.
- **Emerging:** GEO/AEO specialist, marketing automation engineer, AI creative director, creator-partnership manager, brand trust and authenticity lead.
- **Planning rule:** Favour paths that build original research, brand judgement or measurement skill over channel operation alone.

## Risks and watch-outs
- Entry-level content production is under pressure from AI; strategy, original research and distribution skills hold value.
- Channel skills age quickly; recommend learning habits as well as certificates.
- Marketing salaries vary widely by company stage and market.


---

# PART: references/medicine-and-surgery.md

# Medicine, dentistry and veterinary

Physicians, surgeons, dentists and vets. Training routes are fixed by country and decided by exams and match or selection systems, so check the person's country and the country they might move to before drawing any path. Career direction only; no medical advice.

## Typical ladder
- Physician (examples): Medical school -> internship or foundation years -> residency or specialty training (3 to 7 years) -> attending or consultant -> division or department lead -> medical director -> chief medical officer
- Academic branch: clinician-scientist -> associate professor -> professor, chair
- Dentistry and veterinary: degree -> licence -> associate -> practice owner or specialist (after residency)

## Common pivots
- **Clinical to health tech, digital health or clinical informatics**: clinical judgement transfers; needs product, data and regulatory skills.
- **Clinical to pharma or device industry** (medical affairs, clinical development, drug safety): needs industry exposure; an MD is valued.
- **Clinical to management**: medical director, hospital executive; needs finance and leadership training (MBA, MHA, physician-leader programs).
- **Clinical to consulting, health policy, public health**: needs analytical skills (MPH helps).
- **Clinical to medical education or research**: needs a research record and often a PhD or MSc.

## Credentials and learning
Licences and specialty boards are the credentials. Verify them on the regulator's site for the country.
- Examples by country: USMLE and ACGME residencies (US), GMC registration and specialty training (UK), AMC and the specialist colleges (Australia), MCCQE and Royal College or CFPC (Canada), national licensing exams elsewhere
- Moving countries: foreign graduates usually need credential verification, exams, language tests and sometimes repeat training. Plan 1 to 3 years and check pass rates and match odds.
- Add-ons: MPH, MBA or MHA, health informatics, medical education certificates, clinical research training (GCP)

## What separates levels
- Trainee to specialist: passing specialty exams and getting a training post. Posts are competitive and capped by country.
- Specialist to leader: running a service, budget, quality and people, not only patients.
- Leader to executive: system strategy, finance and regulation.

## Skills in demand
- Specialties with shortages (primary care, psychiatry, geriatrics, anaesthesia in many countries)
- Digital health, telemedicine, data and AI literacy
- Quality improvement and patient safety, leadership

## Role outlook: next 10 years
Directional, from trend reports. Confirm with fresh sources before telling someone a role is shrinking.
- **Growing:** Primary care, geriatrics, mental health, palliative care, genomics and precision medicine, remote and home-based care.
- **Evolving:** Ambient AI scribes cut documentation time. Radiology, pathology and dermatology shift to AI-assisted reading, with doctors supervising. Specialists spend more time on complex cases and decisions.
- **Shrinking or being replaced:** Medical transcription, manual coding and routine triage tasks. Successors are clinical informatics and health data roles.
- **Emerging:** Clinical AI safety and governance lead, digital health medical director, physician-engineer roles, genomic medicine specialist.
- **Planning rule:** Licensed physician roles change slowly and stay protected by regulation. Do not predict fast disappearance. Do show how AI changes daily work.

## Risks and watch-outs
- Training places are capped, and cross-border moves are slow and costly.
- Burnout and long training years; ask about workload and family limits.


---

# PART: references/nursing-allied-health.md

# Nursing and allied health

Nurses, midwives, physiotherapists, radiographers, paramedics, therapists, lab scientists, dietitians and similar licensed clinicians. Rules differ by country; check the person's regulator and the regulator of any country they might move to.

## Typical ladder
- Nursing: Registered nurse -> senior or charge nurse -> clinical specialist or nurse practitioner (clinical branch) or nurse manager (leadership branch) -> director of nursing -> chief nursing officer
- Allied health: Graduate clinician -> senior clinician -> advanced practitioner or specialist -> team lead or service manager -> head of profession or director
- Education branch: clinical educator -> lecturer -> programme lead

## Common pivots
- **Bedside to advanced practice** (nurse practitioner, advanced clinical practitioner): needs a master's and supervised hours.
- **Clinical to informatics or digital health**: needs data and systems skills; nurse informaticist is a recognised route.
- **Clinical to industry** (clinical specialist, medical device or pharma roles): needs product knowledge and some travel.
- **Clinical to leadership, quality or patient safety**: needs management training.
- **Clinical to education or research**: needs a master's, often a PhD.
- **Moving abroad**: strong demand for nurses in many countries, but each needs registration, an English or local language test and sometimes a competency exam.

## Credentials and learning
Verify each on the regulator's site.
- Licences: examples are NCLEX-RN and state boards (US), NMC registration (UK), AHPRA (Australia), provincial colleges (Canada), national boards elsewhere. Allied professions have their own regulators (for example HCPC in the UK).
- Specialty certifications from national bodies (critical care, oncology, perioperative and others)
- Master's: nurse practitioner, advanced practice, MPH, MHA, health informatics, education
- Quality and leadership: Lean healthcare, patient safety courses, leadership programmes

## What separates levels
- Graduate to senior: independent judgement and consistent outcomes.
- Senior to specialist: advanced qualification and a clinical niche.
- Clinician to manager: staffing, budgets, quality, people.

## Skills in demand
- Critical care, mental health, geriatrics, community and home care
- Digital tools, remote monitoring, data use
- Leadership and change management

## Role outlook: next 10 years
- **Growing:** Nursing and allied health in most countries (ageing populations, shortages), nurse practitioners and advanced practitioners, mental health, community and home care.
- **Evolving:** AI documentation and monitoring tools take admin time; clinicians spend more on assessment, coordination and patient contact. Tasks shift down to assistants and up to advanced practice.
- **Shrinking or being replaced:** Routine paperwork, manual charting and some scheduling tasks, absorbed by software and support roles.
- **Emerging:** Virtual ward nurse, remote care coordinator, nurse informaticist, clinical AI safety roles.
- **Planning rule:** Demand is strong and licensing protects the roles. The risk is burnout and pay, not replacement. Plan for advanced practice or a specialty to widen options.

## Risks and watch-outs
- Burnout and shift work; ask what workload the person can sustain.
- Overseas recruitment rules and visa pathways change; check current ones.


---

# PART: references/operations-supply-chain.md

# Operations, supply chain and project management

## Typical ladder
- Operations: Operations analyst/coordinator -> Operations manager -> Senior manager -> Director of operations -> VP Operations -> COO
- Supply chain: Planner/buyer -> Supply chain manager -> Senior manager -> Director -> VP Supply Chain -> CSCO
- Project management: Project coordinator -> Project manager -> Senior PM -> Program manager -> Head of PMO
- Process improvement: Analyst -> Continuous improvement lead -> Director of excellence

## Common pivots
- **Operations to product or program management**: transfers process and delivery skill.
- **Operations to consulting**: transfers problem solving; often needs an MBA.
- **Supply chain to procurement strategy or analytics**: needs data skills.
- **Project management to product, strategy, or general management**: needs P&L and strategy exposure.
- **Operations to founder**: transfers building systems.

## Credentials and learning
Verify names, fees and local recognition before recommending.
- Project management: PMP, PRINCE2, CAPM, PMI-ACP
- Lean and Six Sigma: Green Belt, Black Belt
- Supply chain: APICS/ASCM CSCP, CPIM, CLTD; CIPS for procurement
- Analytics: SQL, Power BI, Excel modelling, supply chain planning tools
- MBA or a master's in operations or supply chain: helps for director and COO tracks.

## What separates levels
- Coordinator to manager: owns a process or project and its results.
- Manager to director: owns budget, vendors, and cross-functional trade-offs.
- Director to COO: balances cost, speed, quality and risk for the whole company.

## Skills in demand
- Supply chain resilience and risk planning
- Automation and data-driven planning
- Vendor and contract management
- Sustainability and compliance reporting
- Stakeholder communication

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** Supply chain resilience and risk, procurement strategy, sustainability and compliance, analytics-driven planning, automation and process engineering.
- **Evolving:** Planners become exception managers over automated planning. Project managers move toward program and product delivery with AI scheduling. Operations managers orchestrate people and automation together.
- **Shrinking or being replaced:** Manual scheduling and coordination, order entry, status-report project coordinators, and basic expediting. Their successors are control-tower analysts and process automation leads.
- **Emerging:** Supply-chain control tower analyst, automation and process orchestration lead, AI operations manager, sustainable supply chain lead.
- **Planning rule:** Strong paths add analytics, negotiation or automation skill. Coordination-only paths need a flag.

## Risks and watch-outs
- Routine coordination work is being automated; analysis, negotiation and leadership keep value.
- Some sectors (logistics, manufacturing) depend on region and economic cycles.
- Certifications count heavily in some markets and little in others; check job ads.


---

# PART: references/pharmacy-life-sciences.md

# Pharmacy, biotech and life sciences

Pharmacists, pharma and biotech scientists, clinical research, regulatory affairs, medical affairs, quality and manufacturing roles. Pharmacy practice is licensed by country; industry roles are mostly not.

## Typical ladder
- Pharmacy practice: Pharmacist -> senior or clinical pharmacist -> pharmacy manager or advanced practice -> director of pharmacy
- R&D: Research associate -> scientist -> senior scientist -> principal scientist -> associate director -> director, head of research
- Clinical research: Clinical research associate (CRA) -> senior CRA -> clinical trial manager -> associate director -> head of clinical operations
- Regulatory, quality and medical affairs: associate -> specialist -> manager -> director -> vice president
- Manufacturing and quality: technician or operator -> engineer or analyst -> supervisor -> head of quality or operations

## Common pivots
- **Pharmacy to industry** (regulatory, medical affairs, pharmacovigilance): needs industry exposure.
- **Bench science to regulatory, clinical or quality**: needs the right GxP training.
- **Science to data or bioinformatics**: needs coding and statistics.
- **Science to consulting, venture or business development**: needs commercial skills.
- **Industry to biotech start-up**: needs a risk appetite and breadth.

## Credentials and learning
- Pharmacy licences: PharmD and board exams (US), GPhC registration (UK), national regulators elsewhere. Verify on the regulator's site.
- PhD or MSc for research tracks; postdoc is common in some research roles but not needed for most industry paths.
- Clinical research: ICH-GCP training, ACRP or SoCRA certification
- Regulatory: RAPS RAC certification, regulatory affairs master's
- Quality: ASQ certifications, GMP and GxP training
- Bioinformatics and data: coursework, portfolio
- Add an MBA or business training for management or business development.

## What separates levels
- Junior to scientist: independent experimental design and results.
- Scientist to principal: scientific leadership and a recognised area.
- Specialist to manager: running studies, submissions or teams to timelines and budgets.

## Skills in demand
- Biologics, cell and gene therapy, mRNA and precision medicine
- Computational biology, data science, AI in drug discovery
- Regulatory strategy, pharmacovigilance, quality systems

## Role outlook: next 10 years
- **Growing:** Biologics and advanced therapy roles, bioinformatics and computational biology, regulatory and safety roles, clinical pharmacy.
- **Evolving:** AI speeds target finding and trial design; scientists supervise models and interpret results. Pharmacists move from dispensing to clinical services as dispensing automates.
- **Shrinking or being replaced:** Manual data entry and routine lab or dispensing tasks. Successors are automation, data and clinical service roles.
- **Emerging:** AI-driven drug discovery scientist, real-world evidence analyst, digital trial manager, cell therapy manufacturing specialist.
- **Planning rule:** Industry follows funding cycles; layoffs hit biotech in downturns. Add a skill that works across companies (regulatory, data, quality).

## Risks and watch-outs
- Biotech funding swings; keep a second option.
- Long PhD and postdoc routes may not pay back for industry roles; check postings.


---

# PART: references/product-management.md

# Product and program management

Covers product management, technical product management, product operations, and program/portfolio management.

## Typical ladder
- Product track: Associate PM -> PM -> Senior PM -> Group PM / Principal PM -> Director of Product -> VP Product -> CPO
- Technical PM track: TPM -> Senior TPM -> Principal TPM -> Director of Technical Programs
- Program management: Coordinator -> Program manager -> Senior program manager -> Head of PMO / Director of Programs
- Founder route: PM -> founder, or PM -> general manager of a business unit

## Common pivots
- **From design, engineering, data, or marketing into PM**: each brings a strength; the gap is usually prioritisation and business metrics.
- **PM to general management or founding**: needs P&L, sales and hiring experience.
- **PM to strategy or consulting**: transfers structured thinking.
- **PM to growth or marketing leadership**: transfers experimentation and customer insight.
- **Product ops or analytics**: transfers process and data skills.

## Credentials and learning
Credentials matter less than a record of shipped products. Verify names and fees before recommending.
- Scrum.org PSPO, Scrum Alliance CSPO: cheap signals for agile settings
- Pragmatic Institute and other product training: useful for structure
- PMP, PgMP, and PMI credentials: valued in program and project roles, especially in large or government-linked organisations
- SAFe Product Owner/Product Manager: valued in large enterprises that use SAFe
- MBA: helps with the jump to director-level or general management; many top PMs do not have one.

## What separates levels
- APM to PM: owns a feature area and ships.
- PM to senior: owns a product line, sets strategy, and shows results in metrics.
- Senior to group or director: manages managers, owns portfolio trade-offs and the business outcome.
- Director to CPO: company strategy, board-level communication, and organisation design.

## Skills in demand
- Discovery and customer research
- Data literacy and experimentation
- Working with AI features: evaluating quality, cost and risk
- Stakeholder management and clear writing
- Pricing and go-to-market understanding

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** AI product managers, technical and platform PMs, growth PMs with strong experimentation skills.
- **Evolving:** PMs prototype with AI, run discovery faster and cover more design and analytics work as teams get smaller ("product builder"). Technical depth counts for more.
- **Shrinking or being replaced:** Coordinator-style project managers, pure backlog-grooming and ticket-writing roles, scrum-master-only roles, and manual status-reporting program roles. Their successors are product owners and engineers who plan with automated tools.
- **Emerging:** AI product owner, agent product manager, product operations lead with automation, product engineer hybrid.
- **Planning rule:** Treat "delivery coordination" as the exposed part of PM and program work. Strong paths add strategy, data or technical credibility.

## Risks and watch-outs
- PM roles are scarce at junior level; many people enter through an internal move from another function.
- "PM" varies from mini-CEO to project coordinator; check the scope before recommending a path.
- Authority without direct reports means influence skills decide success.


---

# PART: references/research-science.md

# Research and academic science (physics, chemistry, biology, maths and similar)

Researchers, postdocs, lecturers and scientists in universities, institutes and industry labs. For clinical medicine use `medicine-and-surgery.md`; for pharma and biotech use `pharmacy-life-sciences.md`.

## Typical ladder
- Academic: PhD -> postdoc (one to three posts) -> assistant professor or independent group leader -> associate professor -> full professor -> department head or dean
- Research staff: research assistant -> research scientist -> senior scientist or staff scientist -> principal investigator in some institutes
- Industry research: scientist -> senior -> principal -> research director

## Common pivots
- **Academia to industry R&D**: needs applied results and teamwork; a PhD is valued.
- **Academia to data science, quant or AI roles**: needs coding, statistics and portfolio.
- **Science to policy, consulting or science writing**: needs communication skills.
- **Science to teaching or education**: needs a teaching credential in some countries.
- **Science to technology transfer, patents or venture**: needs legal or commercial training.
- **Science to regulatory or quality roles**: needs standards training.

## Credentials and learning
- PhD is the core; fellowships (Marie Curie, national research councils, NIH, NSF) fund the postdoc stage. Verify names and deadlines.
- Teaching qualifications for lecturers (for example Advanced HE fellowship)
- Data and coding skills (Python, R), statistics, machine learning
- Patent and technology transfer courses; project management for large grants

## What separates levels
- PhD to postdoc: publications and a clear research line.
- Postdoc to faculty: independent funding, a vision and a record. Posts are far fewer than candidates.
- Industry scientist to leader: delivery to timelines and people leadership.

## Skills in demand
- Computational and data skills in every field
- Lab automation and AI-assisted analysis
- Grant writing and communication

## Role outlook: next 10 years
- **Growing:** Computational biology, AI for science, quantum, materials and battery research, climate science, research software engineering.
- **Evolving:** AI changes literature review, data analysis and hypothesis generation; researchers need to supervise it. Funding concentrates in priority areas.
- **Shrinking or being replaced:** Routine lab and analysis tasks automated by robots and models. Successors are automation, data and research-software roles.
- **Emerging:** AI for science researcher, lab automation scientist, research data steward.
- **Planning rule:** Academic posts are scarce; plan an industry or applied exit alongside any academic path, and say so.

## Risks and watch-outs
- Short postdoc contracts and low pay; family and location limits matter.
- Funding changes in the person's country can close programmes.


---

# PART: references/sales-bizdev.md

# Sales, business development and customer success

## Typical ladder
- Sales: Sales development rep (SDR) -> Account executive -> Senior AE -> Sales manager -> Director of sales -> VP Sales -> Chief revenue officer
- Enterprise / strategic: AE -> Enterprise AE -> Strategic account director
- Business development: BD associate -> BD manager -> Director of partnerships -> VP BD
- Customer success: CSM -> Senior CSM -> CS manager -> Director of CS -> VP Customer Success
- Sales engineering: Sales engineer -> Senior -> Principal or manager

## Common pivots
- **Sales to product marketing or product management**: transfers customer knowledge.
- **Sales to revenue operations**: transfers pipeline understanding; needs systems and analytics.
- **Customer success to account management or product**: transfers retention insight.
- **Technical person to sales engineering**: transfers depth; needs presenting and discovery skills.
- **Sales to founder**: transfers selling; needs product and hiring skills.

## Credentials and learning
Quota results beat credentials. Verify names and fees before recommending.
- Sales methodologies: MEDDICC, Challenger, SPIN, Sandler training (often paid by employers)
- Salesforce and HubSpot certifications for revenue operations and admin paths
- Customer success: Gainsight or CS-focused programs
- Negotiation: Harvard PON or similar short programs
- MBA: helps for executive tracks or moves into general management.

## What separates levels
- SDR to AE: closes deals, not only meetings.
- AE to senior: handles larger, longer deals and forecasts accurately.
- Rep to manager: grows other people's results, which is a different skill from selling.
- Manager to VP/CRO: owns strategy, hiring, territories and the revenue number.

## Skills in demand
- Consultative and technical selling
- Data-driven pipeline management
- Using AI tools for research and outreach, with a human voice
- Partnership and ecosystem sales
- Customer retention and expansion

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** Enterprise and strategic account executives, sales engineers, customer success and expansion roles, partnerships and ecosystem roles, revenue operations.
- **Evolving:** The SDR role shrinks and merges into higher-skill hybrid roles as AI handles prospecting and outreach. AEs become more consultative. CSMs become proactive advisors using AI health signals.
- **Shrinking or being replaced:** High-volume cold-outreach SDR work, lead research and data entry, transactional inside sales, and tier-1 support. Their successors are revenue operations specialists and AI-supported consultants.
- **Emerging:** Go-to-market engineer, AI sales operations lead, solutions consultant, partner ecosystem manager.
- **Planning rule:** Entry-level SDR is a risky starting point for a 10-year plan. Show how the person reaches a consultative or technical role.

## Risks and watch-outs
- Pay depends on quota and market cycles; ask about the person's tolerance for variable income.
- Burnout is common in high-volume outbound roles.
- Success is easy to measure, so strong sellers can move fast; weak results are just as visible.


---

# PART: references/software-engineering.md

# Software engineering

Covers frontend, backend, full-stack, mobile, DevOps/SRE, QA, security and general IT engineering. For data science and ML, also read `data-ai.md`.

## Typical ladder
- Individual-contributor track: Junior -> Mid -> Senior -> Staff -> Principal -> Distinguished (about 2 to 4 years per step until senior, then slower)
- Management track: Senior -> Tech lead -> Engineering manager -> Senior manager / Director -> VP Engineering -> CTO
- Architecture track: Senior -> Solutions/Software architect -> Enterprise architect
- Specialist tracks: Security engineer, SRE/platform engineer, performance engineer, embedded systems engineer

## Common pivots
- **Product management**: transfers technical credibility; needs discovery, prioritisation and communication.
- **Data / ML engineering**: transfers programming and systems skills; needs statistics, data tooling and ML basics.
- **Solutions engineering / developer relations**: transfers technical depth; needs presenting and customer skills.
- **Security**: transfers systems knowledge; needs threat modelling and security tooling.
- **Founding or freelancing**: transfers building ability; needs sales, product sense, and tolerance for risk.
- **Design engineering**: transfers frontend skill; needs design sensibility and systems thinking.

## Credentials and learning
Experience and shipped work count most. Certifications help in cloud, security, and enterprise or government settings. Verify names, prices and validity periods before recommending.
- Cloud: AWS (Solutions Architect Associate/Professional, Developer), Azure (AZ-204, AZ-305), Google Cloud (Associate/Professional Cloud Architect)
- Kubernetes: CKA / CKAD
- Security: CompTIA Security+, CISSP (needs years of experience), OSCP for offensive roles
- Architecture and process: TOGAF for enterprise architecture; Scrum or SAFe credentials for delivery roles
- Language/framework certifications: occasionally asked by outsourcing firms, rarely by product companies
- Degrees: a BS in computer science helps with visas and big employers; a master's helps for ML research, some migration routes and certain countries' skilled-worker points; it rarely matters for pure software craft.

## What separates levels
- Junior to mid: finishes well-scoped tasks reliably.
- Mid to senior: owns features end to end, handles ambiguity, reviews others' code well.
- Senior to staff: shapes technical direction across teams, solves problems nobody assigned.
- Staff to principal: influences the whole organisation's technology and strategy.
- Senior to manager: trades building for growing people; many engineers try it and go back, which is normal.

## Skills in demand
- Cloud and platform engineering, infrastructure as code
- AI-assisted development and building features on top of LLMs and agents
- TypeScript, Python, Go, Rust (depending on the domain)
- System design, observability, reliability
- Security awareness across the stack

## Role outlook: next 10 years
Directional views from industry trend reports, not forecasts. Confirm with fresh sources (for example, the WEF Future of Jobs report, national labour agencies, current job-ad trends) before telling the person a role is dying or rising.

- **Growing:** AI/ML engineering, platform engineering, security, reliability, data engineering, edge and embedded systems.
- **Evolving:** Software engineers increasingly direct AI coding agents and spend more time on specs, architecture, review and testing. QA becomes quality engineering. DevOps becomes platform engineering. The frontend/backend split blurs into "product engineer".
- **Shrinking or being replaced:** Routine CRUD and boilerplate coding, manual testing, ticket-driven sysadmin work, and junior tasks such as simple bug fixes. Their successors are engineers who own outcomes end to end and supervise automated work.
- **Emerging:** AI agent engineer / agent ops, LLM evaluation engineer, AI security engineer, AI platform engineer, forward-deployed engineer.
- **Planning rule:** Paths should add depth in system design, security, data or domain knowledge by mid-career. A path that relies on routine implementation skill alone is the riskiest.

## Risks and watch-outs
- Junior hiring is competitive in many markets; depth in a specialty and visible projects help.
- Routine coding is changing fast with AI tooling; judgement, system design and ownership gain value.
- Outsourcing and services firms follow a different ladder from product companies; ask which the person is in and wants.
- Management is not a promotion for everyone; present the specialist route as an equal option.


---

# PART: assets/data-schema.md (only for the Detailed view)

# Career data schema

Write one JSON file in this shape, then run `scripts/build_graph.py`. Do not read `sample-data.json`; it is a large example used for tests, and this page is enough.

```json
{
  "person": {
    "name": "Alex",
    "currentRole": "UI/UX Designer",
    "summary": "One or two sentences on background and strengths"
  },
  "horizonYears": 10,
  "assumptions": ["Short sentence", "Short sentence"],
  "recommendedPathId": "deepen",
  "rationale": "Two to four sentences: why this path wins for this person, and what would change the call.",
  "runnerUpPathId": "lead",
  "paths": [
    {
      "id": "deepen",
      "title": "Design engineering specialist",
      "tagline": "One line on what this path is",
      "fit": "Strong | Good | Mixed | Poor",
      "forksFrom": { "pathId": "other-path-id", "nodeId": "node-id" },
      "tradeoffs": "One or two honest sentences on the hard parts",
      "sources": [ { "title": "Source title", "url": "https://source-page" } ],
      "nodes": [
        {
          "id": "deepen-1",
          "type": "role",
          "title": "Senior Design Engineer",
          "year": 2.5,
          "summary": "What this step is and why it follows",
          "gate": "What decides if you get here",
          "outlook": "growing | stable | evolving | declining | emerging",
          "outlookNote": "One sentence: how this role changes by year 10, and what replaces it if it shrinks",
          "skills": ["Skill one", "Skill two"],
          "certs": [
            { "name": "Credential name", "provider": "Provider name", "url": "https://official-provider-page", "why": "Why it matters at this step", "duration": "3 months", "cost": "approx. USD 300" }
          ],
          "jobPosts": {
            "reviewed": 12,
            "market": "Toronto / remote",
            "asOf": "2026-11",
            "requirements": [ { "text": "React and TypeScript", "count": "10 of 12" } ],
            "note": "Optional: caveats, such as a small sample"
          },
          "sources": [
            { "title": "Page title", "url": "https://exact-page-or-section", "kind": "job post | report | credential | agency", "where": "Section or page where the claim sits", "note": "What it supports (optional)" }
          ]
        },
        {
          "id": "deepen-cert-1",
          "type": "cert",
          "title": "Credential name",
          "provider": "Provider name",
          "url": "https://official-provider-page",
          "year": 1,
          "summary": "Why now"
        },
        {
          "id": "deepen-edu-1",
          "type": "education",
          "title": "Part-time master's in HCI",
          "year": 4,
          "summary": "Why and how long"
        }
      ]
    }
  ]
}
```

## Field rules

- `year` runs from 0 to `horizonYears`. Year 0 is today. Role nodes need at least 1.5 years between them on the same path so labels do not overlap.
- `type` is `role` (large circle, label below), `cert` (diamond, label above) or `education` (square, label above). Use `cert` and `education` nodes for stand-alone learning steps. Attach `certs` to a role node to list credentials that support that role.
- Give every `role` node an `outlook` and an `outlookNote`. `declining` marks a role likely to shrink or be replaced. `emerging` marks a role that does not exist at scale yet. `cert` and `education` nodes do not need one.
- Keep node titles under about 28 characters. The side panel carries the long text.
- Put nodes in year order within each path.
- Use 3 to 5 paths. Mark exactly one as `recommendedPathId`.
- `forksFrom` is optional. Leave it out and the path starts from the current position. Use it when a path branches off a step on another path (for example, a pivot after year 3).
- `fit` is the match with the person's stated goals, not a score.
- `assumptions` shows at the top of the page, so the person can correct them. Keep each one under 70 characters, for example "Stays in current city for 3 years, then moves".
- `jobPosts` is required for role steps in the first 5 years of the recommended path and the runner-up. For roles beyond year 5, leave it out or give `reviewed: 0` with a `note` saying the step rests on the field reference.
- Skip salary numbers unless you sourced them.

## Links and sources

- **Deep links only.** A link must open the exact page that holds the information, never a home page, a general listing or a search page. For a long document, link the section and name it in `where`. The builder warns about home-page links.
- Every role node needs `jobPosts` (counts from the postings you read, see `references/job-post-research.md`) and a posting or board page in its `sources` (with `kind: "job post"`).
- Every certification, course and degree needs a `url` that points to the **official provider page for that exact credential** (the awarding body or the course host), not a blog, a reseller or a search-result page. Put it on each item in a role's `certs` list and on stand-alone `cert` and `education` nodes.
- Every role node needs `sources`: 1 to 3 pages that back its outlook, requirements or typical scope (a job-family page, a labour agency report, an industry trend report, a professional body page). Every path needs `sources` too, for its overall case.
- Use only URLs you opened or that a search returned in this session. Never write a URL from memory. If you cannot verify a link, leave `url` out; the page then shows "official link not verified yet" and the builder warns you. A missing link is better than a wrong one.
- Links open in a new tab. Only http and https links are shown.
