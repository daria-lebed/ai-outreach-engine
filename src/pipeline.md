# Outreach Pipeline

### Goal
Generate personalized cold email messages from lead data.

---

### Pipeline Steps
1. Load data from `/data/inputs/leads.csv`
2. Validate fields (name, company, hook_note)
3. Apply text pre-processing (clean names, lowercase emails)
4. Choose template (A/B)
5. Generate {intro + value + CTA} using personalization
6. Export results to `/data/outputs/letters_{date}.csv`

---

### Output Fields
- email
- first_name
- company
- subject_line
- message_body

---

### Edge Cases
- missing name → skip
- duplicate lead → skip
- invalid email → skip
