# 🚀 AI Outreach Engine  
### Modern AI + RevOps system for scalable outbound

This project is part of my AI RevOps System — a set of tools and workflows that combine **revenue operations, AI automation, and GTM execution**.  
The goal: build predictable pipeline without spam, manual work, or chaotic processes.

---

## ✅ What this does

✔ Generates **personalized cold emails**  
✔ Generates **LinkedIn DMs** with AI  
✔ Works from a clean **lead CSV pipeline**  
✔ Uses **context-aware personalization**  
✔ Designed for **B2B SaaS outbound**  
✔ Built to be **modular and expandable**  

---

## 🧠 Why I built it
Most outreach fails because it’s copy/paste spam that ignores context.  
This engine creates **smart outbound**: meaningful, personalized, scalable — without hiring 10 SDRs.

---

## 🔧 Tech Stack
| Layer | Tools |
|------|--------|
| Language | Python |
| AI | OpenAI GPT-4o mini |
| Data | pandas |
| Workflow | modular pipeline |
| Output | CSV templates + AI generation |

---

## 📂 Project Structure

ai-outreach-engine
│
├── data
│   ├── inputs              # Lead lists (CSV)
│   └── outputs             # AI generated messages
├── docs                    # Project documentation
│   ├── architecture.md     # System architecture & workflow
│   └── email_templates.md  # AI outreach message templates
├── src                     # Core code
│   ├── io_csv.py
│   ├── templater.py
│   ├── ai_client.py
│   ├── ai_email_generator.py
│   ├── ai_dm_generator.py
│   ├── pipeline.py
│   └── dm_pipeline.py
├── .env.example
├── requirements.txt
└── README.md

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/daria-lebed/ai-outreach-engine.git
cd ai-outreach-engine

## Create virtual environment & install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt

## Configure environment:
```bash
cp .env.example .env
# Add your OPENAI_API_KEY inside .env


⸻

▶️ Usage

## Generate personalized cold emails
```bash
python3 src/pipeline.py

## Output file:
```bash
data/outputs/emails_generated.csv

## Generate LinkedIn DMs
```bash
python3 src/dm_pipeline.py

## Output file:
```bash
data/outputs/dm_ai_generated.csv


⸻

