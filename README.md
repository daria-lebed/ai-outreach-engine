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
