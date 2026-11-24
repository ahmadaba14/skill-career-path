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
