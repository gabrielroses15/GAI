def runN(lista):
    import sys
    import os
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Adiciona o diretório pai ao sys.path
    
    neuronList = ["watch", "calcComplexity", "specialCharacters", "extractContext", "saudacao", "trad_en", "dicio", "botZap", "calcFeeling", "recoFala", "recoTheme", "respostaAudio"] #Neurônios como trad, ou complex podem ter subNeuronios como instancias de "níveis" maiores ou menores, neste caso, poderia ser uma lista de neurônios filhos do neurônio pai, e a lista apenas seria carregada se seu pai fosse chamado, assim se otimiza o tempo de processamento.
    #Tem neurônios q só por estarem como 1 desencadeiam outros, exemplo, recoResposta, mas nem spm tbm, tem q considerar q nd é 100% e isso q é de complicar o negócio
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
    else: #Analisar o tamanho da lista pra n passar por tantos if, cancelar se retornar já a resposta no meio
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

lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
runN(lista)

#N tem TIPO DE PERGUNTA PQ ACHEI INUTIL JÁ Q O EXTRATOR DE CONTEXTO JÁ PEGA O TIPO DE PERGUNTA