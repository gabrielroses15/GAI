from DecisionModules import extrair_contexto as context
from DecisionModules import caracteres_especiais
from DecisionModules import verificaByDicio as verifica
from DecisionModules import calculaComplexidade as complexity

def choose(prompt):
    tipos = []
    resposta = "Por favor reformule."
    start = "Tudo bem?"
    
    complexidade = complexity.CalcComplex(prompt, tipos)
    
    if complexidade == "Por favor reformule.":
        return resposta
    else:
        if complexidade == 1:
            contexto, resposta = context.extrair_contexto(prompt, tipos, complexidade, resposta)
            if contexto == "responder":
                #Inclusive vale a penar já deixar mapeado frases de coplexidade nível 1 pra não demorar na resposta de coisas simples.
                return resposta
        
        if "A frase " in contexto and "ainda não foi mapeada, favor mapear!" in contexto:
                resposta = prompt
                return resposta
    #prompt, tipos = caracteres_especiais.specialCharacters(prompt, tipos)
    
    #contexto, tipos, saudacao = context.extrair_contexto(prompt, saudacao, tipos)
    
    print("tipos:{} \n contexto:{} \n saudacao:{}".format(tipos, contexto, saudacao))
    input("a")
        
    #Construção da resposta "middle"
    
    middle = "resposta baseada no banco"

    
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