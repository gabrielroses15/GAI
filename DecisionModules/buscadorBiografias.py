def buscarPorBiografiasNaFrase(respostaFinal:str):
    retorno = ""
    biografiasEncontradas = 0
    deEcontrados = 0
    index = 0
    while index < len(respostaFinal.split()):
        plvr = respostaFinal.split()[index]
        if respostaFinal.split()[index] == "biografia":
            biografiasEncontradas += 1
            if biografiasEncontradas > 1:
                plvr = ""
        elif respostaFinal.split()[index] == "de":
            deEcontrados += 1
            if deEcontrados == 2:
                plvr = "e"
            elif deEcontrados > 2:
                plvr = ","
        retorno = retorno + " " + plvr
        index += 1
    retorno = retorno.replace("  ", " ")
    return "resposta", retorno