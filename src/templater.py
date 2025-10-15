def render_email_template(template: str, lead: dict) -> str:
    """
    Simple placeholder replacement for {first_name}, {company}, etc.
    """
    return template.format(
        first_name=lead.get("first_name", ""),
        company=lead.get("company", ""),
        hook_note=lead.get("hook_note", "")
    )


def render_subject_line(lead: dict) -> str:
    """Generate simple subject line"""
    return f"quick one, {lead.get('first_name', '')}"
