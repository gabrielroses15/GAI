def runN(lista, respo:str = "runNeurons não obteve resposta, resposta padrão.", prompt:str = "", testing=True):
    resposta = "Sem resposta dada ao runNeurons"
    promptFormatadoPelaArvoreDeGeografia = False
    def carros():
        from DecisionModules.DecisionThrees import ArvoreCarros as Carro
        resposta = Carro.Carro(prompt, respo)
        return resposta
    def esportes():
        from DecisionModules.DecisionThrees import ArvoreEsportes as Esportes
        Esportes.Esportes()
    def casa():
        from DecisionModules.DecisionThrees import ArvoreCasa as Casa
        Casa.Casa()
    def perguntaSimples():
        from DecisionModules.DecisionThrees import ArvorePerguntaSimples as PerguntaSimples
        respo = PerguntaSimples.PerguntaSimples(prompt)
        return respo
    def perguntaMedia():
        from DecisionModules.DecisionThrees import ArvorePerguntaMedia as PerguntaMedia
        resposta = PerguntaMedia.PerguntaMedia(prompt, respo)
        if type(resposta) == list:
            return resposta[0]
    def perguntaDificil():
        from DecisionModules.DecisionThrees import ArvorePerguntaDificil as PerguntaDificil
        resposta = PerguntaDificil.PerguntaDificil(prompt)
        if type(resposta) == list:
            return resposta[1]
    def financas():
        from DecisionModules.DecisionThrees import ArvoreFinancas as Financas
        Financas.Financas()
    def relacionamento():
        from DecisionModules.DecisionThrees import ArvoreRelacionamento as Relacionamento
        Relacionamento.Relacionamento()
    def amor():
        from DecisionModules.DecisionThrees import ArvoreAmor as Amor
        Amor.Amor()
    def sexo():
        from DecisionModules.DecisionThrees import ArvoreSexo as Sexo
        Sexo.Sexo()
    def antiNSFW():
        from DecisionModules.DecisionThrees import ArvoreAntiNSFW as AntiNSFW
        AntiNSFW.AntiNSFW()
    def informacoesSimples():
        from DecisionModules.DecisionThrees import ArvoreInformacoesSimples as InformacoesSimples
        InformacoesSimples.InformacoesSimples()
    def programacao():
        from DecisionModules.DecisionThrees import ArvoreProgramacao as Programacao
        Programacao.Programacao()
    def morte():
        from DecisionModules.DecisionThrees import ArvoreMorte as Morte
        Morte.Morte()
    def arte():
        from DecisionModules.DecisionThrees import ArvoreArte as Arte
        Arte.Arte()
    def historia():
        from DecisionModules.DecisionThrees import ArvoreHistoria as Historia
        Historia.Historia()
    def matematica():
        from DecisionModules.DecisionThrees import ArvoreMatematica as Matematica
        Matematica.Matematica()
    def geografia():
        from DecisionModules.DecisionThrees import ArvoreGeografia as Geografia
        newPrompt = Geografia.Geografia(prompt)
        promptFormatadoPelaArvoreDeGeografia = True
        return newPrompt
    def portugues():
        from DecisionModules.DecisionThrees import ArvorePortugues as Portugues
        Portugues.Portugues()
    def geometria():
        from DecisionModules.DecisionThrees import ArvoreGeometria as Geometria
        Geometria.Geometria()
    def reflexao():
        from DecisionModules.DecisionThrees import ArvoreReflexao as Reflexao
        Reflexao.Reflexao()
    def badVibes():
        from DecisionModules.DecisionThrees import ArvoreBadVibes as BadVibes
        BadVibes.BadVibes()
    def solidao():
        from DecisionModules.DecisionThrees import ArvoreSolidao as Solidao
        Solidao.Solidao()
    def amigos():
        from DecisionModules.DecisionThrees import ArvoreAmigos as Amigos
        Amigos.Amigos()
    def NPCTalk():
        from DecisionModules.DecisionThrees import ArvoreNPCTalk as NPCTalk
        NPCTalk.NPCTalk(prompt)
    def Normal():
        from DecisionModules.DecisionThrees import ArvoreNormal as choose
        resposta = choose.escolhas(prompt, respo, promptFormatadoPelaArvoreDeGeografia, testing)
        if resposta[0] == "resposta":
            return resposta[1]
        return resposta[1]
    chooseList = [carros, esportes, casa, perguntaSimples, perguntaMedia, perguntaDificil, 
        financas, relacionamento, amor, sexo, antiNSFW, informacoesSimples, programacao,
        morte, arte, historia, matematica, geografia, portugues, geometria, reflexao, badVibes,
        solidao, amigos, NPCTalk, Normal]
    index = 0
    contador = lista.count(1)
    if contador > 1:
        respostas = []
        for run in lista:
            if run == 0:
                index += 1
            else:
                retornoDoCodigo = chooseList[index]()
                if type(retornoDoCodigo) == str:
                    respostas.append(retornoDoCodigo)
                elif type(retornoDoCodigo) == list:
                    if retornoDoCodigo[0] == "prompt":
                        prompt = retornoDoCodigo[1]
                index += 1
        return respostas
    else:
        for run in lista:
            if run == 0:
                index += 1
            else:
                retornoDoCodigo = chooseList[index]()
                if type(retornoDoCodigo) == str:
                    resposta = retornoDoCodigo
                elif type(retornoDoCodigo) == list:
                    if retornoDoCodigo[0] == "prompt":
                        prompt = retornoDoCodigo[1]
                index += 1
    # if type(resposta) == str:
    #     print("str")
    # else:
    #     print("o tipo da resposta é", type(resposta))
    return resposta

#N tem TIPO DE PERGUNTA PQ ACHEI INUTIL JÁ Q O EXTRATOR DE CONTEXTO JÁ PEGA O TIPO DE PERGUNTA