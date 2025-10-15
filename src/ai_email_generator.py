from ai_client import generate_email_with_ai

def build_email_prompt(first_name, company, hook_note):
    return f"""
    Write a short, smart cold email for outreach.
    Tone: professional, concise, human.
    Personalize using this context.
    ---
    Recipient: {first_name} at {company}
    Context: {hook_note}
    Offer: AI-powered sales ops + outbound system optimization.
    CTA: quick call or reply.
    No fluff. No hype. Max 90 words.
    """

def generate_ai_email(first_name, company, hook_note):
    prompt = build_email_prompt(first_name, company, hook_note)
    return generate_email_with_ai(prompt)
