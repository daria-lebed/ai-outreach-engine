from pathlib import Path
import pandas as pd
from io_csv import load_leads, save_letters
from templater import render_email_template, render_subject_line

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "inputs" / "leads_sample.csv"
OUTPUT_PATH = BASE_DIR / "data" / "outputs" / "letters_generated.csv"

EMAIL_TEMPLATE = (
    "Hi {first_name}, noticed {hook_note}.\n"
    "I build AI-powered outbound + sales ops systems that improve reply rates and keep pipeline clean.\n"
    "Worth a quick look?\n"
    "- Daria"
)

def run_pipeline():
    leads = load_leads(str(INPUT_PATH))
    letters = []
    for _, row in leads.iterrows():
        d = row.to_dict()
        subject = render_subject_line(d)
        message = render_email_template(EMAIL_TEMPLATE, d)
        letters.append({
            "first_name": d.get("first_name", ""),
            "email": d.get("email", ""),
            "company": d.get("company", ""),
            "subject": subject,
            "message": message
        })
    df = pd.DataFrame(letters)
    save_letters(df, str(OUTPUT_PATH))

if __name__ == "__main__":
    run_pipeline()
    print("DONE")
