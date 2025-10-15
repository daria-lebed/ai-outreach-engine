# AI Outreach Engine – Architecture

**Goal:** Generate personalized cold emails at scale using contact data + AI logic.

### Pipeline
1. Input leads from CSV
2. Normalize lead fields (name, company, ICP notes)
3. Select email template
4. Generate intro + body + CTA
5. Export final messages to CSV

### Modules
- `config` – environment variables (OpenAI key)
- `io` – read/write CSV files
- `templates` – message structures
- `engine` – generation logic
- `utils` – helper functions

### Data Flow
`/data/inputs/leads.csv` → `src/engine` → `/data/outputs/emails.csv`
