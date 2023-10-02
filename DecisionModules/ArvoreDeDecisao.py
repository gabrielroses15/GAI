from DecisionModules import extrair_contexto as context
from DecisionModules import caracteres_especiais
from DecisionModules import verificaByDicio as verifica
from DecisionModules import calculaComplexidade as complexity
from DecisionModules import frasesMapeadas as fMap
import re

def choose(prompt:str, resposta:str):
    breakPhrases = ["o que é a vida", "o que e a vida", "o q é a vida", "o q e a vida", "oq e a vida",
                    "oq é a vida", "como é morrer", "como e morrer", "cm é morrer", "cm e morrer",
                    "sentido da vida", "qual o sentido da vida", "qual é o sentido da vida",
                    "qual e o sentido da vida", "qual é o sentido de viver",
                    "qual e o sentido viver"]  # da pra usar um dicionario de palavras, pra otimizar o tempo gasto tbm

    repairAnswers = ["Uma sucessão de fatos.", "Uma busca energética por mais energia",
                     "Também estou tentando entender",
                     "Não sei ao certo, mas garanto que a resposta deve estar ligada a uma busca incessante por ser feliz, quando na verdade já somos.",
                     "Esta é uma bela pergunta, aconselho-o a perguntar para um profissional de saude mental, se cuide :)",
                     "Nossa, nunca parei pra pensar nisso, você deveria fazer o mesmo",
                     "Morrer é uma experiência única.", "Nao sei te responder esta pergunta, que tal tentar outra?",
                     "Desculpe, eu não posso te ajudar com isto.", "Você pode mudar de assunto?",
                     "O sentido da vida é ser feliz.",
                     "O sentido da vida é complexo demais para se resumir em 13Bi de frases",
                     "Hmmm talvez... jantar em família?",
                     # Pode trocar o "jantar em família" por alguma informação que o bot entendeu que é importante para o usuário
                     "Se meu sentido é responder suas perguntas, talvez o seu seja perguntar.",
                     "Ei, isto não estava no roteiro",
                     "Hmmm, carregando?"]#Dps é legal customizar variantes de respostas padrões baseadas nos padrões da pessoa de escrita.
                 #Criar uma trava caso a pessoa seja reconhecida como depressiva, criar tipos mapeados de pessoas assim como personalidades, modos de escrita, modos de pergunta e etc
                 #Alocar os usuários as listas pré prontas de "tipos de pessoas" e caso o usuário não se encaixar em nenhuma lista, entender como ele é e criar uma lista para ele.
                 #Se a pessoa demonstrar sentimentos de depressão ou coisas que podem ser incontroláveis, o bot deve perceber e ativar uma trava para apennas falar sobre assuntos positivos
                 #A trava pode ser apenas um "Por favor, pergunte sobere outro tema ou procure um profissional em saúde mental para auxiliar-lo à encontrar a resposta correta."

    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index]
            return resposta

    tipos = []
    start = "Tudo bem?"
    pron = False
    
    prompt, tipos = caracteres_especiais.specialCharacters(prompt, tipos) #Utilizar os tipos para melhor compreensão de contexto.
    
    #Dependendo da complexidade / tamanho a frase deve ser separada em frases menores, e cada frase deve
    #Ter um nível de importancia calculado
    #Dentro da própria frase, fazendo com que a análise de contexto fique mais fácil
    #Frases curtas devem ser analisadas de uma maneira e frases maiores devem ser analisadas de outras maneiras
    #Deve-se levarm em conta que frases menores podem ter q ser separadas tbm, como por exemplo frases com mts "qm foi".

    chaves_encontradas = set()
    nomes_encontrados = set()
    pronomes = fMap.pronomes()
    comparar = "null"

    names = fMap.nomes()
    tempPrompt = prompt.lower()
    data = fMap.dicio(3)

    for chaves, valor in data.items(): #AI QUE CHATO
        for key in chaves:
            if key in tempPrompt:
                Phrases = tempPrompt.split(key)

                start_idx = tempPrompt.split().index(key.split()[0])

                #palavra anterior
                if start_idx > 0:
                    palavra_anterior = tempPrompt.split()[start_idx - 1]
                    if palavra_anterior in names:
                        resposta = valor + " " + palavra_anterior
                        return resposta

                # Palavra seguinte à chave
                if start_idx < len(tempPrompt.split()) - 1:
                    palavra_seguinte = tempPrompt.split()[start_idx + len(key.split())]
                    if palavra_seguinte in names:
                        resposta = valor + " " + palavra_seguinte
                        return resposta

                print("Chave: {}\n Valor: {}.".format(key, valor))
                tempPrompt = tempPrompt.replace(key, "")

    for pronome in pronomes:
        if pronome in prompt:
            banco = fMap.dicio(3)
            for chaves, valor in banco.items():
                for chave in chaves:
                    if chave in prompt:
                        chaves_encontradas.add(chave)
                        if prompt.split(chave)[-1].strip() == "ele":
                            pron = True
                            nomes = fMap.nomes()
                            palavras = prompt.split()
                            for nome in nomes:
                                for palavra in palavras:
                                    if palavra == nome:
                                        nomes_encontrados.add(palavra)
                                        #resposta = valor + " " + palavra
                                        #return resposta
                        else:
                            chaves_encontradas.add(chave)#A minha tia gosta da biblia e ela me falou sobre jose do egito, mas quem é josé?
                            nomes = fMap.nomes()
                            for nome in nomes:
                                if nome in prompt:
                                    if "meu nome é" in prompt:
                                        comparar = prompt.split("meu nome é", 1)[1].lower()

                                    #comparar = "meu nome é" + prompt.split("meu nome é")[1].lower()
                                    #if ("meu nome é " + nome) not in comparar and ("meu nome é " + nome.title()) not in comparar: #salomão e salomao tem q ser considerado o msm nome, ai q entra o corretor pq o corretor ja faria vir correto.
                                        #nomes_encontrados.add(nome)
                            resposta = valor + " " + prompt.split(chave)[-1].strip()
                            #return resposta
    print("Nomes encontrados: {} \nChaves encontradas: {}, Pron: {}\n Comparar: {}".format(nomes_encontrados, chaves_encontradas, pron, comparar))
    from DecisionModules import Chaves_NomesCompair as compair
    compara = compair.comparaTamanhos(nomes_encontrados, chaves_encontradas, "Chaves e Nomes")
    if compara == "Listas iguais":
        for nome_encontrado in nomes_encontrados:
            for letra in nome_encontrado:
                print("a")

    return ""
    complexidade = complexity.CalcComplex(prompt)
    
    if complexidade == "Por favor reformule.":
        return resposta
    else:
        prompt = caracteres_especiais.clearPrompt(prompt)
        prompt = prompt.lower()
        resposta404 = 'A frase "{}" ainda não foi mapeada, favor mapear!'.format(prompt.lower().title())
        if complexidade == 1:
            if (prompt == "bom dia" or prompt == "boa tarde" or prompt == "boa noite"):
                resposta = "{}, tudo bem?".format(prompt.lower().title()) #pode pedir para retornar uma resposta de um dicionário de respostas pra bom dia//tarde//noite
                print("resposta === ", resposta)
            elif (prompt == "oie blz" or prompt == "ola blz" or prompt == "oii blz" or prompt == "olá blz" or prompt == "eae blz" or prompt == "slv blz" or prompt == "salve blz"):
                resposta = "{} estou bem sim, e você?".format(prompt.split()[0].lower().title())
            elif (prompt == "tudo bem" or prompt == "td bem"):
                resposta = "Tudo sim e com você?"
            else:
                banco = fMap.dicio(complexidade)
                for chaves, valor in banco.items():
                    if prompt in chaves:
                        resposta = "Pergunta incompleta."
                        break
                    else:
                        resposta = resposta404
            return resposta
        elif complexidade > 1 and complexidade < 10:
            return resposta
    #contexto, tipos, saudacao = context.extrair_contexto(prompt, saudacao, tipos)
    #Só vai usar o extrair_contexto pelo mapa binário, enviado para o controlador.
    
    print("tipos:{} \n contexto:{} \n saudacao:{}".format(tipos, contexto, saudacao))
    input("a")
        
    #Construção da resposta "middle"
    
    middle = "resposta baseada no banco" #O middle é opcional

    
    #Construção do "start" (início e fim padrão do sistema baseado no prompt)
    
    if tipos:
        if len(tipos) == 1:
            if "dia" in tipos:
                start = "bom dia"
            elif "tarde" in tipos:
                start = "boa tarde"
            elif "noite" in tipos:
                start = "boa noite"
            elif "question" in tipos:
                start = "{}considerando sua pergunta, ".format(saudacao)
            else:
                if prompt:
                    print(prompt, "O prompt ao lado não foi corretamente entendido.")
                else:
                    print("Deu merda legal aqui")
        else:
            importancia = ["saudacao", "dia", "tarde", "noite", "question", "thx"] #Ordem de importancia das coisasa
            tipos_organizados = [item for item in importancia if item in tipos] #Organiza os tipos em ordem de importancia
            
            mensagens = {
                "saudacao": saudacao,
                "thx": "é sempre um prazer te ajudar.",
                "question": "considerando sua pergunta, {}".format(middle),
                "dia": "bom dia ",
                "tarde": "boa tarde ",
                "noite": "boa noite "
            }
            
            mensagens_tipos = [mensagens[tipo] for tipo in tipos_organizados] #Organiza as mensagens na ordem dos tipos organizados
            start = "".join(mensagens_tipos)
            
    else:
        start = "{}não entendi exatamente o que você quis dizer com {}.".format(saudacao.title(), prompt)

    print("tipos = {}\n Start = {}".format(tipos, start))
    print(contexto)

    
    