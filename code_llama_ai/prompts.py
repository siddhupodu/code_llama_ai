PROMPT_TEMPLATES = {
    "default": "You are an AI assistant. Answer the following question:\n{question}",
}

def get_prompt(template_name: str, **kwargs) -> str:
    template = PROMPT_TEMPLATES.get(template_name, PROMPT_TEMPLATES["default"])
    return template.format(**kwargs) 