def responderElogioEXingamentos(prompt: str):
    pronomes = ["você", "voce", "vc", "tu", "gai"]
    eh = ["é", "eh", "éh", "ehh", "éhh"]
    elogios = ["demais", "dimais", "de mais", "dms", "di mais", "incrivel", "incrível", "espetacular", "indescritível",
               "indescritivel", "insano", "esbelto", "magnífico", "magnificiente", "admirável", "exemplar",
               "inteligete", "foda", "legal"]
    xingamentos = ["um merda", "um bosta", "horrível", "zoado", "hororroso", "horrendo", "um desgraçado", "desgraçado",
                   "um fudido", "um fodido", "fudido", "fodido"]

    for pronome in pronomes:
        for e in eh:
            for elogio in elogios:
                frase = pronome + " " + e + " " + elogio
                if frase in prompt:
                    resposta = "Obrigado, vc que é {}, além de ser minha inspiração!".format(elogio)
                    return resposta
            for xingamento in xingamentos:
                frase = pronome + " " + e + " " + xingamento
                if frase in prompt:
                    resposta = "Ei, não chame as pessoas de {}, isto não é legal!".format(xingamento)
                    return resposta