from io_csv import load_leads, save_letters
from templater import render_email_template, render_subject_line
import pandas as pd

EMAIL_TEMPLATE = """Hi {first_name}, noticed {hook_note}.
I build AI-powered outbound + sales ops systems that improve reply rates and keep pipeline clean.
Worth a quick look?
– Daria
"""

def run_pipeline(input_path, output_path):
    leads = load_leads(input_path)
    letters = []

    for _, row in leads.iterrows():
        lead = row.to_dict()
        subject = render_subject_line(lead)
        message = render_email_template(EMAIL_TEMPLATE, lead)
        letters.append({
            "first_name": lead.get("first_name"),
            "email": lead.get("email"),
            "company": lead.get("company"),
            "subject": subject,
            "message": message
        })

    df = pd.DataFrame(letters)
    save_letters(df, output_path)


if __name__ == "__main__":
    run_pipeline("../data/inputs/leads_sample.csv", "../data/outputs/letters_generated.csv")
