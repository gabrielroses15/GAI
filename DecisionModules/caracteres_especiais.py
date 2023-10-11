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

def clearPrompt(prompt:str):
    if "?" in prompt:
        prompt = prompt.replace("?", "")
    if "!" in prompt:
        prompt = prompt.replace("!", "")
    if "." in prompt:
        prompt = prompt.replace(".", "")
    if "," in prompt:
        prompt = prompt.replace(",", "")
    return prompt