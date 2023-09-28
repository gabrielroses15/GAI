def specialCharacters(prompt: str, tipos: list):
    if "?" in prompt:
        tipos.append("question")
        prompt = prompt.replace("?", "")
    if "!" in prompt:
        tipos.append("happy")
        prompt = prompt.replace("!", "")
    if "." in prompt:
        prompt = prompt.replace(".", "")
    if "," in prompt:
        prompt = prompt.replace(",", "")
    return prompt, tipos

def clearPrompt(prompt):
    if "?" in prompt:
        prompt = prompt.replace("?", "")
    if "!" in prompt:
        prompt = prompt.replace("!", "")
    if "." in prompt:
        prompt = prompt.replace(".", "")
    if "," in prompt:
        prompt = prompt.replace(",", "")
    return prompt