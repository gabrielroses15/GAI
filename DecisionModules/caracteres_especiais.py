def clearPrompt(prompt: str, especialCharacters:list=["?", ".", "!", ",", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "<", ">", "/", "\\", "|", "_", "-", "+", "=", "*", "&", "%", "$", "#", "@", "~", "`", "^"]):
    for especial in especialCharacters:
        if especial in prompt:
            prompt = prompt.replace(especial, "")
    return prompt
