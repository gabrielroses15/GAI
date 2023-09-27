from DecisionModules import extrair_contexto as context
from DecisionModules import caracteres_especiais
from DecisionModules import verificaByDicio as verifica
from DecisionModules import calculaComplexidade as complexity

def choose(prompt:str, resposta:str):
    tipos = []
    start = "Tudo bem?"
    
    prompt, tipos = caracteres_especiais.specialCharacters(prompt, tipos) #Utilizar os tipos para melhor compreensão de contexto.
    
    complexidade = complexity.CalcComplex(prompt)
    
    if complexidade == "Por favor reformule.":
        return resposta
    else:
        from DecisionModules import frasesMapeadas as fMap
        banco = fMap.dicio(complexidade)
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
                for chaves, valor in banco.items():
                    if prompt in chaves:
                        resposta = "Pergunta incompleta."
                        break
                    else:
                        resposta = resposta404
            return resposta
        elif complexidade > 1 and complexidade < 10:
            for chaves, valor in banco.items():
                for chave in chaves:
                    if chave in prompt:
                        resposta = valor + " " + prompt.split(chave)[-1].strip()
                        if prompt.split(chave)[-1].strip() == "ele":
                            print("a")
                        return resposta
                    else:
                        resposta = resposta404
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