from pathlib import Path
import pandas as pd
from io_csv import load_leads, save_letters
from templater import render_email_template, render_subject_line
from ai_email_generator import generate_ai_email

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "inputs" / "leads_sample.csv"
OUTPUT_PATH = BASE_DIR / "data" / "outputs" / "letters_generated.csv"
AI_OUTPUT_PATH = BASE_DIR / "data" / "outputs" / "letters_ai_generated.csv"

EMAIL_TEMPLATE = (
    "Hi {first_name}, noticed {hook_note}.\n"
    "I build AI-powered outbound + sales ops systems that improve reply rates and pipeline visibility.\n"
    "Worth a quick look?\n"
    "- Daria"
)

def run_template_pipeline():
    leads = load_leads(str(INPUT_PATH))
    letters = []

    for _, row in leads.iterrows():
        lead = row.to_dict()
        subject = render_subject_line(lead)
        message = render_email_template(EMAIL_TEMPLATE, lead)
        letters.append({
            "first_name": lead.get("first_name", ""),
            "email": lead.get("email", ""),
            "company": lead.get("company", ""),
            "subject": subject,
            "message": message
        })

    save_letters(pd.DataFrame(letters), str(OUTPUT_PATH))


def run_ai_pipeline():
    leads = load_leads(str(INPUT_PATH))
    letters = []

    for _, row in leads.iterrows():
        lead = row.to_dict()
        ai_message = generate_ai_email(
            lead.get("first_name", ""),
            lead.get("company", ""),
            lead.get("hook_note", "")
        )
        letters.append({
            "first_name": lead.get("first_name", ""),
            "email": lead.get("email", ""),
            "company": lead.get("company", ""),
            "message": ai_message
        })

    save_letters(pd.DataFrame(letters), str(AI_OUTPUT_PATH))


if __name__ == "__main__":
    print("Running AI Outreach Engine...")
    run_ai_pipeline()
    print("✅ AI emails generated!")
