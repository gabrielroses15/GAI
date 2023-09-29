from DecisionModules import extrair_contexto as context
from DecisionModules import caracteres_especiais
from DecisionModules import verificaByDicio as verifica
from DecisionModules import calculaComplexidade as complexity
from DecisionModules import frasesMapeadas as fMap
import re

def choose(prompt:str, resposta:str):
    tipos = []
    start = "Tudo bem?"
    
    prompt, tipos = caracteres_especiais.specialCharacters(prompt, tipos) #Utilizar os tipos para melhor compreensão de contexto.
    
    #Dependendo da complexidade / tamanho a frase deve ser separada em frases menores, e cada frase deve
    #Ter um nível de importancia calculado
    #Dentro da própria frase, fazendo com que a análise de contexto fique mais fácil
    #Frases curtas devem ser analisadas de uma maneira e frases maiores devem ser analisadas de outras maneiras
    #Deve-se levarm em conta que frases menores podem ter q ser separadas tbm, como por exemplo frases com mts "qm foi".

    chaves_encontradas = set()
    nomes_encontrados = set()
    pronomes = fMap.pronomes()
    for pronome in pronomes:
        if pronome in prompt:
            banco = fMap.dicio(3)
            for chaves, valor in banco.items():
                for chave in chaves:
                    if chave in prompt:
                        if (chave+pronome) in prompt:
                            print("a")
                        if prompt.split(chave)[-1].strip() == "ele":
                            nomes = fMap.nomes()
                            palavras = prompt.split()
                            for nome in nomes:
                                for palavra in palavras:
                                    if palavra == nome:
                                        resposta = valor + " " + palavra
                                        return resposta
                        else:
                            chaves_encontradas.add(chave)
                            nomes = fMap.nomes()
                            for nome in nomes:
                                if nome in prompt:
                                    if (chave+pronome) in prompt:
                                        print("a")
                                    try:
                                        comparar = "meu nome é" + prompt.split("meu nome é")[1].lower()
                                    except:
                                        pass
                                    if ("meu nome é " + nome) not in comparar and ("meu nome é " + nome.title()) not in comparar: #salomão e salomao tem q ser considerado o msm nome, ai q entra o corretor pq o corretor ja faria vir correto.
                                        nomes_encontrados.add(nome)
                            resposta = valor + " " + prompt.split(chave)[-1].strip()
                            #return resposta
    print("Nomes encontrados: {} \nChaves encontradas: {}".format(nomes_encontrados, chaves_encontradas))
    from DecisionModules import Chaves_NomesCompair as compair
    compara = compair.comparaTamanhos(nomes_encontrados, chaves_encontradas, "Chaves e Nomes")
    if compara == "Listas iguais":
        for nome_encontrado in nomes_encontrados:
            for letra in nome_encontrado:
                print(letra)


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