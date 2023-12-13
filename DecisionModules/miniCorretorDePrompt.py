def corrigirPrompt(prompt: str, words: list):
    miniCorretor = {"você": ["vc", "voce", "voçe", "voçê", "tu"],
                    "vo": ["avô", "vovô"],
                    "porshe": ["porche", "porhsi", "pórche", "pórcshi"],
                    "vidro": ["vrido"], "pedra": ["preda"],
                    "são": ["sao"],
                    "qual é o seu nome": ["qual o seu nome", "qual e o seu nome",
                                          "qual é o seu nm", "cual é o seu nome",
                                          "cual e o seu nome", "cual é u seu nome",
                                          "cual e u seu nome", "qual é seu nome",
                                          "qual seu nome"],
                    "napoleão": ["napoleao", "nápoleao", "nápoleão", "napoliao", "napoleão bonaparte", "bonaparte"]}
    for valor, palavras in miniCorretor.items():
        for palavra in palavras:
            for word in words:
                if word == palavra:
                    prompt = prompt.lower().replace(palavra, valor)
    return prompt