def render_email_template(template, lead):
    return template.format(
        first_name=lead.get("first_name", ""),
        company=lead.get("company", ""),
        hook_note=lead.get("hook_note", "")
    )

def render_subject_line(lead):
    fn = lead.get("first_name", "")
    return "quick one, " + fn if fn else "quick one"
