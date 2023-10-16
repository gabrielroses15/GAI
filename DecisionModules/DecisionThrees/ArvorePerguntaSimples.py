def PerguntaSimples(prompt):
    corrigir = {"quem é você": ["qm é vc", "qm é você", "qm é voce", "quem e você", "quem é voce"],
                "o que é você": ["o que é vc", "o q é vc", "o que e vc", "oq é vc", "oq e vc"],
                "de onde você veio": ["de onde vc veio", "d ond vc veio", "de onde voce veio"]}

    for valor, frases in corrigir.items():
        for frase in frases:
            if frase in prompt:
                prompt = prompt.replace(frase, valor)

    if "quem é você" in prompt:
        resposta = "Sou um bot feito para responder perguntas difíceis, como esta."
    elif "o que é você" in prompt:
        resposta = "Sou uma inteligência artificial."
    elif "de onde você veio" in prompt:
        resposta = "Não sei também, mas provavelmentne da idéia de dentro da mente de alguém."
    else:
        resposta = "perguntaSimples não reconhecida."
        
    return resposta