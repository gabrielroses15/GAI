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


def clearPrompt(prompt: str, especialCharacters:list=["?", ".", "!", ",", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "-", "+", "=", "*", "&", "%", "$", "#", "@", "~", "`", "^"]):
    for especial in especialCharacters:
        if especial in prompt:
            prompt = prompt.replace(especial, "")
    return prompt
