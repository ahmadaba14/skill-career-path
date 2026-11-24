# career-path

A skill that builds a personalised 10-year career path from a resume and a few answers. It gives several branching routes, the certifications, licences and study each step needs, and one recommended path with the reasoning.

It works for any field and any country, and it is built for Claude but written so other AI tools can use it too.

## What it does

1. Reads the person's resume or a short description, and notes their country.
2. Asks short questions about anything unclear (goals, limits, country, which view they want). It never guesses about you and uses only what you tell it in the conversation. It waits for your answers before it researches or builds.
3. Reads a reference file for the person's field, then checks the web for current facts and real job posts in their market.
4. Builds 3 to 5 different routes, picks one, and explains why.

**Two views**

| View | What you get | Cost |
|---|---|---|
| Simpler (default) | A chat reply: one recommended path with dated steps, 2 to 4 other paths, how the roles change by year 10, job-post counts, and a Sources list. It ends by asking which path to open and whether you want the detailed version | Lower: roughly 100k tokens in our tests |
| Detailed | An interactive HTML page: full-screen pan-and-zoom graph, a side panel with certifications, study, trade-offs, outlook and sources, and the best path in green | Higher: roughly 160k tokens in our tests |

Every certification, licence and course links to its official page. Every role carries an outlook label (growing, stable, evolving, declining, emerging) and sources. Where it cannot verify something, it says so.

## What is in the folder

```
career-path/
  SKILL.md                    The instructions (start here)
  README.md                   This file
  references/                 One Markdown file per field, plus link and job-post rules
  assets/                     Graph template, data schema, sample data
  scripts/build_graph.py      Builds the HTML page from a JSON file (Python 3, no packages)
```

Fields covered: design and UX, software, data and AI, product, finance, HR, marketing, sales, operations, medicine, nursing and allied health, pharmacy and life sciences, health administration, engineering (mechanical, electrical, civil and others), energy and environment, architecture and construction, research science, education, law and compliance, and a generic fallback for anything else.

## Install

### From GitHub (quickest)

Replace `YOUR-USERNAME` with the GitHub account that hosts this repo.

```bash
npx skills add YOUR-USERNAME/career-path
```

The `skills` command finds `SKILL.md`, detects the AI coding tools you have installed (Claude Code, Codex, Cursor and many more), and installs the skill for each. Useful options:

- `-g` installs for your user account instead of only the current project.
- `-a claude-code` installs for one tool only (swap in another tool's name).
- `--list` shows what is in the repo without installing.

Example: `npx skills add YOUR-USERNAME/career-path -g -a claude-code`

Note: this command needs Node.js, and the tool collects anonymous usage data (see its own docs to opt out).

### Fallback: clone with git (Claude Code, no extra tools)

```bash
git clone https://github.com/YOUR-USERNAME/career-path ~/.claude/skills/career-path
```

The folder must be named `career-path`. Update later with `git pull` inside that folder. For one project only, clone into `.claude/skills/career-path` in that project instead.

### Other ways to install

**Claude (claude.ai, Claude desktop, Claude Code)**
- claude.ai or desktop: open Settings, then Capabilities or Skills, and upload `career-path.skill`.
- Claude Code: unzip `career-path.skill` into `~/.claude/skills/` (user-wide) or `.claude/skills/` (one project). The folder must be named `career-path`.

**Tools that read `SKILL.md` folders** (several coding agents follow this open format): copy the `career-path/` folder into that tool's skills directory. Check the tool's docs for the path.

**OpenAI Codex CLI and other tools that read `AGENTS.md`**
1. Copy `career-path/` into your project, for example `tools/career-path/`.
2. Copy `adapters/AGENTS.md` into the project root, or append it to the file you already have. Edit the path inside it if you used another folder.

**Gemini CLI**: copy `career-path/` into your project and put `adapters/GEMINI.md` in the project root (edit the path inside if needed).

**Cursor**: copy `career-path/` into your project and `adapters/cursor-career-path.mdc` into `.cursor/rules/`.

**Chat apps with no file access (ChatGPT, Gemini, Copilot, others)**
1. Open `all-in-one/career-path-all-in-one.md`. It holds the instructions and every reference file in one document, about 30k tokens.
2. Paste it as the first message, or add it to a custom GPT, Gem or project as instructions or knowledge.
3. Then say what you want, for example "Where can I take my career?" and attach your resume.
4. In this mode you get the Simpler view. For the Detailed view use a tool that can run Python, or follow "Build the graph yourself" below.

## Example prompts

You do not need a special phrase. Any question about your career direction triggers the skill. These prompts get better answers because they give the skill what it asks for anyway: your role, your country, your limits and what you want.

**Quick start (Simpler view)**
- "Where can I take my career over the next 10 years? Here is my resume." (attach it)
- "I'm a nurse in Manchester with 6 years in ICU. What are my options, and which one would you pick?"
- "I'm a backend developer in Sao Paulo with 5 years in fintech. Keep it short, no graph."

**Full map (Detailed view)**
- "Build me the full graph. I'm a mechanical engineer in Houston, 8 years in oil and gas." (you get the interactive page)
- "Give me the detailed view with certifications and study for each step. Resume attached."

**Give your answers up front (skips the questions)**
- "I like system design and hard production problems, I don't want to manage people, I can move to Portugal or the Netherlands, I can study 6 hours a week on a modest budget, and income matters most. Where does this go in 10 years?"

**Think through a switch**
- "I'm a doctor in Melbourne, four years out of medical school. Should I go for specialty training or move toward industry?"
- "I'm a second engineer on tankers and want to come ashore in 2 to 3 years. What is realistic?"
- "I'm an accountant in audit and I'm tired of fieldwork. What else could I do with my skills?"

**Ask about one thing at a time**
- "Which certifications actually matter for a product manager in Germany?"
- "Will my role still exist in 10 years? If not, what replaces it?"
- "Open up the second path in more detail." (after a first answer)
- "Now build the detailed graph for the path you recommended."

**Tips for better answers**
- Say your country and city. Licences, pay and job titles depend on it.
- Share a resume or paste your work history. It saves the opening questions.
- Say what you will not do (nights, managing people, moving) and what you must keep (income, flexibility, family time).
- Give your real study time and budget. The skill sizes each step to them.
- Ask for the Detailed view only when you want the full map. The Simpler view costs less and often answers the question.
- Ask it to challenge the pick: "What would make you change your recommendation?"

## What the tool needs

| Needs | Used for | Without it |
|---|---|---|
| Web search and page reading | Current credentials, fees, job posts, outlook | The skill works from its reference files, labels everything unverified and gives no posting counts |
| Reading files in the skill folder | References and templates | Paste the one reference file for your field |
| Python 3 (standard library only) | Building the Detailed graph page | Use the Simpler view, or build the graph yourself |

## Build the graph yourself

If the AI wrote a career data JSON file but cannot run code:

```
python3 scripts/build_graph.py my-career.json my-career.html
```

Open `my-career.html` in any browser. The script checks the data and prints warnings, for example a home-page link where a specific page is needed. The JSON format is in `assets/data-schema.md`.

## Add or change a field

Reference files are plain Markdown. To add a field, copy the structure of `references/generic-fallback.md` into `references/<field>.md`, then add a row to the table in `SKILL.md` (and in `adapters/` if you use them). The "Role outlook" section is the most useful part: list which roles grow, change, shrink or are new, and what replaces the shrinking ones. Refresh these every year or so, since AI is changing them fast.

## How well it works

We tested it against the same prompts without the skill, using five people in different fields and countries: a UK ICU nurse, an Australian doctor, a Brazilian backend developer, a Houston mechanical engineer and a Croatian marine engineer. With the skill, all 40 checks passed. Without it, 10 of 40 passed, mostly because the plain replies had no sources, links or posting counts. A later round checked the ask-first rule on a vague request and the closing offer of the detailed version; the skill passed all of those checks too.

Limits to know about:
- Each case ran once, so treat the result as a small sample.
- Tests ran in Claude. The other tools are supported by design, but we have not tested them.
- Many job posts are closed or undated when read, so counts show what employers asked over the past year, not open vacancies.
- Reference files are directional views of a field, not forecasts. The skill confirms the volatile parts online when it can.
- Pay, fees and licence rules change. The skill leaves out figures it cannot source.

## Privacy

The skill uses the resume and answers only to build the path. It does not need accounts or keys.

## Not career, legal or medical advice

The output is a planning aid. For licences, visas and regulated professions, check the regulator's own page before you commit time or money.
