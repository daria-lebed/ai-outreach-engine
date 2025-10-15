from pathlib import Path
import pandas as pd
from io_csv import load_leads, save_letters
from ai_dm_generator import generate_ai_dm

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_PATH = BASE_DIR / "data" / "inputs" / "leads_sample.csv"
AI_DM_OUTPUT_PATH = BASE_DIR / "data" / "outputs" / "dm_ai_generated.csv"

def run_ai_dm_pipeline():
    leads = load_leads(str(INPUT_PATH))
    messages = []

    for _, row in leads.iterrows():
        lead = row.to_dict()
        dm_text = generate_ai_dm(
            lead.get("first_name", ""),
            lead.get("company", ""),
            lead.get("hook_note", "")
        )
        messages.append({
            "first_name": lead.get("first_name", ""),
            "linkedin": lead.get("linkedin", ""),
            "company": lead.get("company", ""),
            "message": dm_text
        })

    save_letters(pd.DataFrame(messages), str(AI_DM_OUTPUT_PATH))

if __name__ == "__main__":
    print("🔷 Generating AI LinkedIn DMs...")
    run_ai_dm_pipeline()
    print("✅ AI LinkedIn DMs generated!")

if __name__ == "__main__":
    run_dm_pipeline()
    print("✅ LinkedIn messages generated")
