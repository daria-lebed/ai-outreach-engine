from pathlib import Path
import pandas as pd
from io_csv import load_leads, save_letters
from templater import render_email_template

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "inputs" / "leads_sample.csv"
OUTPUT_PATH = BASE_DIR / "data" / "outputs" / "dm_generated.csv"

DM_TEMPLATE = (
    "Hi {first_name}, noticed {hook_note}. "
    "I build AI-powered sales ops systems that improve reply rates "
    "without spam tactics. Open to connect?"
)

def run_dm_pipeline():
    leads = load_leads(str(INPUT_PATH))
    messages = []

    for _, row in leads.iterrows():
        lead = row.to_dict()
        message = render_email_template(DM_TEMPLATE, lead)
        messages.append({
            "first_name": lead.get("first_name", ""),
            "linkedin": lead.get("linkedin", ""),
            "message": message
        })

    save_letters(pd.DataFrame(messages), str(OUTPUT_PATH))

if __name__ == "__main__":
    run_dm_pipeline()
    print("✅ LinkedIn messages generated")
