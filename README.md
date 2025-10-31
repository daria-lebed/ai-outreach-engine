<p align="center">
  <img src="https://github.com/daria-lebed/ai-outreach-engine/blob/main/docs/your_banner.png" 
       alt="AI Outreach Engine Banner" 
       width="90%">
</p>

<h1 align="center">🤖 AI Outreach Engine</h1>

<p align="center">
  <em>GPT-powered outbound automation — scale outreach without losing personalization</em>
</p>
<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white"></a>
  <a href="https://openai.com/"><img src="https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai&logoColor=white"></a>
  <a href="https://www.hubspot.com/"><img src="https://img.shields.io/badge/HubSpot-CRM-orange?logo=hubspot&logoColor=white"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green"></a>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
  <img src="https://img.shields.io/badge/AI%20RevOps-Automation-purple">
</p>

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

<pre>
ai-outreach-engine/
├── data/
│   ├── inputs/              # Lead lists (CSV)
│   └── outputs/             # AI-generated messages
│
├── docs/                    # Project documentation
│   ├── architecture.md      # System design & workflow
│   └── banner.png           # Visual banner
│
├── src/                     # Core scripts
│   ├── ai_client.py
│   ├── ai_email_generator.py
│   ├── ai_dm_generator.py
│   ├── dm_pipeline.py
│   ├── io_csv.py
│   └── templater.py
│
├── requirements.txt
├── .env.example
└── README.md
</pre>

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/daria-lebed/ai-outreach-engine.git
cd ai-outreach-engine
```

Create virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
# .venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

Configure environment:

```bash
cp .env.example .env
# Add your OPENAI_API_KEY inside .env
```

---

## ▶️ Usage

### Generate personalized cold emails
```bash
python3 src/pipeline.py
```
Output file:
```
data/outputs/emails_generated.csv
```

---

### Generate LinkedIn DMs
```bash
python3 src/dm_pipeline.py
```
Output file:
```
data/outputs/dm_ai_generated.csv
```

---

## 📊 Demo
See `/docs/outreach_demo_report.md` for examples of AI outputs and metrics.


