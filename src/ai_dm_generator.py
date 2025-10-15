from ai_client import generate_email_with_ai

def build_dm_prompt(first_name, company, hook_note):
    return f"""
    Write a short LinkedIn DM in friendly SaaS tone.
    Style: brief, human, no hype, no buzzwords.
    Personalize using context.
    ---
    Person: {first_name} at {company}
    Context: {hook_note}
    Offer: AI-powered outreach + sales ops cleanup
    Goal: open conversation, not sell
    Max length: 35 words
    """

def generate_ai_dm(first_name, company, hook_note):
    prompt = build_dm_prompt(first_name, company, hook_note)
    return generate_email_with_ai(prompt)
