def dicio(complexity):
    if complexity < 1 :
       return "Erro na classificação de complexidade da frase."
    else:
        if complexity > 1 and complexity < 10:
            frases_mapeadas = {("quem foi", "quem era", "qm era", "qm foi"): "biografia de", ("história de", "história do", "historia da", "história di", "história du", "historia do", "história de", "historia da", "história di", "historia du", "hist da", "hist de", "hist di", "hist di", "hist do", "hist du"): "história"}
            return frases_mapeadas