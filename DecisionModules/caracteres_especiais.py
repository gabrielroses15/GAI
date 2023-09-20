def specialCharacters(prompt: str, tipos: list):
    if "?" in prompt:
        tipos.append("question")
        prompt.replace("?", "")
    if "!" in prompt:
        tipos.append("happy")
        prompt.replace("!", "")
    if "." in prompt:
        prompt.replace(".", "")
    prompt = "".join(prompt)
    return prompt, tipos