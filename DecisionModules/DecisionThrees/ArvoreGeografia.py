def Geografia(prompt):
    from DecisionModules import frasesMapeadas as fMap
    nomes = fMap.nomes()
    if "rua de" in prompt:
        prompt = prompt.replace("rua de", "rua")
    prompt = prompt.replace("dona", "")
    prompt = prompt.replace("dom", "")
    prompt = prompt.replace("don", "")
    prompt = prompt.replace("  ", " ")
    prompt = prompt.replace("joao", "joão")
    prompt = prompt.replace("são", "")
    geoList = ["avenida", "rua", "local", "quadra", "mercado", "hospital"]
    nomes_encontrados = []
    palavras = prompt.lower().split()

    for nome in nomes:
        frase = "padaria do {}".format(nome)
        if frase in prompt:
            prompt = prompt.replace(frase, "")
        for item in geoList:
            frase = "{} {}".format(item, nome)
            if frase in prompt:
                frase = frase = "{} {} e".format(item, nome)
                if frase in prompt:
                    nomes_encontrados.append(nome)
                    index_nome = palavras.index(nome)
                    x = 1
                    while True:
                        if palavras[index_nome+x] == "e":
                            x += 1
                            for name in nomes:
                                if palavras[index_nome+x] == name:
                                    nomes_encontrados.append(name)
                                    x += 1
                        else:
                            break
                    for find in nomes_encontrados:
                        if item + " " + find in prompt:
                            prompt = prompt.replace(item + " " + find, "")
                else:
                    prompt = prompt.replace(frase, "")

    prompt2 = ["prompt", prompt.replace("  ", "")]
    return prompt2