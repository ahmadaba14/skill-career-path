---
name: career-path
description: Build a personalised 10-year career path from a person's resume, current role and interests, with branching routes, recommended certifications and study, and one best-fit path explained. Use this skill whenever the user asks about their career path, where they can take their career, what to do next professionally, how to grow or pivot, "what should I become in 5/10 years", promotion routes, which certifications, licences or degrees to pursue, or shares a resume/CV and wants direction, even if they never say "career path". Works for any field (tech, business, medicine, nursing, engineering, science, trades and more) and any country.
---

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
