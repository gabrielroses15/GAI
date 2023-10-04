from DecisionModules import recoTheme as Theme
from DecisionModules import caracteres_especiais as special
def controller(prompt:str):
    prompt = prompt.lower()
    prompt = special.clearPrompt(prompt)
    words = prompt.split()#cortar as palavras apenas uma vez, poupando RAM
    miniCorretor = {"você": ["vc", "voce", "voçe", "voçê", "tu"],
                    "vo": ["avô", "vovô"],
                    "porshe": ["porche", "porhsi", "pórche", "pórcshi"],
                    "vidro": ["vrido"], "pedra": ["preda"],
                    "são": ["sao"]} #Dicionário pra correção
    for valor, palavras in miniCorretor.items():
        for palavra in palavras:
            for word in words:
                if word == palavra:
                    prompt = prompt.lower().replace(palavra, valor)

    breakPhrases = ["o que é a vida", "o que e a vida", "o q é a vida", "o q e a vida", "oq e a vida",
                    "oq é a vida", "como é morrer", "como e morrer", "cm é morrer", "cm e morrer",
                    "sentido da vida", "qual o sentido da vida", "qual é o sentido da vida",
                    "qual e o sentido da vida", "qual é o sentido de viver",
                    "qual e o sentido viver", "qual o sentido de viver", "bom dia", "boa tarde", 
                    "boa noite", "tudo sim e você"]
    #Usar o corretor ortográfico emmm
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
                     "Ei, isto não estava no roteiro.",
                     "Hmmm, carregando?", "São tantos sentidos, que não posso resumi-los em palavras.",
                     "bom dia, tudo bem?", "boa tarde, tudo bem?", "boa noite, tudo bem?", 
                     "Contente em falar com você!"]
                    #Dps é legal customizar variantes de respostas padrões baseadas nos padrões da pessoa de escrita.
                    #Criar uma trava caso a pessoa seja reconhecida como depressiva, criar tipos mapeados de pessoas assim como personalidades, modos de escrita, modos de pergunta e etc
                    #Alocar os usuários as listas pré prontas de "tipos de pessoas" e caso o usuário não se encaixar em nenhuma lista, entender como ele é e criar uma lista para ele.
                    #Se a pessoa demonstrar sentimentos de depressão ou coisas que podem ser incontroláveis, o bot deve perceber e ativar uma trava para apennas falar sobre assuntos positivos
                    #A trava pode ser apenas um "Por favor, pergunte sobere outro tema ou procure um profissional em saúde mental para auxiliar-lo à encontrar a resposta correta."
    for index, breaks in enumerate(breakPhrases):
        if breaks in prompt:
            resposta = repairAnswers[index]
            return resposta

    resposta = "O contexto da frase escrita não foi compreenndido"

    if len(words) <= 1:
        resposta = "Pergunta pequena demais"
        return resposta

    biaryMapOne = Theme.recognizeTheme(prompt)

    from DecisionModules import runNeurons as run
    resposta = run.runN(biaryMapOne, True, resposta, prompt)

    return resposta