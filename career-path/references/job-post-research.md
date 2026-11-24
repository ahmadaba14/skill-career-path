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
