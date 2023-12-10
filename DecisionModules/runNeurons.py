def runN(lista, tree:bool = False, respo:str = "runNeurons não obteve resposta, resposta padrão.", prompt:str = "", testing=True):

    if tree == False:
        resposta = "Sem resposta dada ao runNeurons"
        import sys
        import os
        
        sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
        
        neuronList = ["watch", "calcComplexity", "specialCharacters", "extractContext", "saudacao", "trad_en", "dicio", "botZap", "calcFeeling", "recoFala", "recoTheme", "respostaAudio"]
        activatedNeurons = []
        
        if len(lista) == len(neuronList):
            for index, num in enumerate(lista):
                if num != 1 and num != 0:
                    print("O número {} não corresponde ao padrão binário esperado".format(num))
                else:
                    if num == 1:
                        activatedNeurons.append(neuronList[index])
        elif len(lista) < len(neuronList):
            print("Faltam números na lista passada")
        elif len(lista) > len(neuronList):
            print("Os números da lista passada excedem o número de neurônios")
        
        if activatedNeurons == []:
            print("Nenhum neurônio foi ativado.")
        else:
            if "watch" in activatedNeurons:
                import assisteVideo as watch
                #watch.transcrever_video(url)#Vai ter q fzr uma REQUISIÇÃO pedindo o url pqp kkkkkkk
            if "calcComplexity" in activatedNeurons:
                import calculaComplexidade as calc
                #calc.CalcComplex(prompt, tipos)#Vai ter q fzr uma REQUISIÇÃO pedindo o url pqp kkkkkkk
            if "specialCharacters" in activatedNeurons:
                import caracteres_especiais as specialCharacters
                #specialCharacters.specialCharacters(prompt, tipos)#Vai ter q fzr uma REQUISIÇÃO pedindo o url pqp kkkkkkk
            if "extractContext" in activatedNeurons:
                import extrair_contexto as context
                #context.extrair_contexto(prompt, tipos, complexidade, resposta)#Vai ter q fzr uma REQUISIÇÃO pedindo o url pqp kkkkkkk
            if "saudacao" in activatedNeurons:
                import is_saudacao
                #is_saudacao.is_saudacao(prompt)#Vai ter q fzr uma REQUISIÇÃO pedindo o url pqp kkkkkkk
            if "trad_en" in activatedNeurons:
                import translate_en
                #translate_en.trad(text)
            if "dicio" in activatedNeurons:
                import verificaByDicio as dicio
                #dicio.verificaByDicio(prompt, tipos, saudacao)
            if "botZap" in activatedNeurons:
                import botTeste as botZap
                #botZap.bot()
            if "calcFeeling" in activatedNeurons:
                import CalculaSentimento as calcFeeling
                #calcFeeling.CalcFeeling(text)
            if "recoFala" in activatedNeurons: #atrelar ao respostaAudio
                import RecoFala as recoFala
                #recoFala.voiceRecord(passagem)
            if "recoTheme" in activatedNeurons:
                import RecoTheme as recoTheme
                #recoTheme.RecoKeys(texto)
            if "respostaAudio" in activatedNeurons: #atrelar a fala
                import Resposta_Audio as respostaAudio
                #respostaAudio.AwnswerAudio
    else:
        resposta = "Sem resposta dada ao runNeurons"
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
        def Normal(testing:bool=False):
            from DecisionModules.DecisionThrees import ArvoreNormal as choose
            resposta = choose.escolhas(prompt, respo, testing)
            if resposta[0] == "resposta":
                return resposta[1]
            return resposta[1]
            # from DecisionModules.DecisionThrees import ArvoreDeDecisao as choose
            # resposta = choose.choose(prompt, respo)
            # return resposta
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
                    if type(chooseList[index]()) == str:
                        resposta = chooseList[index]()
                    elif type(chooseList[index]()) == list:
                        if chooseList[index]()[0] == "prompt":
                            prompt = chooseList[index]()[1]
                    index += 1
                    respostas.append(resposta)
            return respostas
        else:
            for run in lista:
                if run == 0:
                    index += 1
                else:
                    if type(chooseList[index]()) == str:
                        resposta = chooseList[index]()
                    elif type(chooseList[index]()) == list:
                        if chooseList[index]()[0] == "prompt":
                            prompt = chooseList[index]()[1]
                    index += 1
    # if type(resposta) == str:
    #     print("str")
    # else:
    #     print("o tipo da resposta é", type(resposta))
    return resposta

#N tem TIPO DE PERGUNTA PQ ACHEI INUTIL JÁ Q O EXTRATOR DE CONTEXTO JÁ PEGA O TIPO DE PERGUNTA