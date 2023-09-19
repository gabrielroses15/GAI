class decisoes:
    
    def caracteres_especiais(prompt: str, tipos: list):
        if "?" in prompt:
            tipos.append("question")
            prompt.replace("?", "")
        if "!" in prompt:
            tipos.append("happy")
            prompt.replace("!", "")
        if "." in prompt:
            prompt.replace(".", "")
        prompt = "".join(prompt)
        return prompt, tipos
    
    #Função pra retirar o contexto da frase
    def extrair_contexto(prompt: str):
        import spacy
        nlp = spacy.load("pt_core_news_lg")
        doc = nlp(prompt.lower())
        pessoas = []
        pronomes = []
        verbos = []
        pron = ["eu", "tu", "ele", "nós", "vós", "eles", "nos", "vos", "nois", "você", "vc", "voce", "ela", "elx", "ela", "vocês", "vcs", "voces"]
        nomes = ["salomão", "miguel", "gabriel",
        "lucas", "joão", "davi", "pedro", "enzo",
        "gustavo", "eduardo", "nicolas", "yuri", "caio", "vitor",
        "antonio", "vinicius", "william", "paulo",
        "daniel", "marcos", "fernando", "rodrigo", "anderson",
        "andre", "julio", "renan", "valmir",
        "luis", "leonardo", "fabio", "nome", "arthur", "giovanna", "lais", "marina", "raissa", "thiago", "laura",
        "laisa", "sophia", "joao", "henrique", "samuel", "matheus", "luiza",
        "marcela", "leticia", "beatriz", "mirella", "clara", "isabella", "livia",
        "mateus", "guilherme", "marcelo", "jose", "gabriela", "rafaela", "raul",
        "gabrielle", "julia", "victor", "valentina", "viviane", "isabel", "isabelle", "thais",
        "nathalia", "nathalie", "diego", "bruno", "vivian", "marcio", "amanda", "carolina", "erica", "hugo", "joaquin",
        "karina", "lucia", "mario", "nadia", "patricia", "rafael", "sergio", "tomas",
        "ursula", "viviana", "yolanda", "sebastian", "valeria", "xavier",
        "martin", "pablo", "natalia", "manuel", "francisco",
        "ricardo", "veronica", "felipe", "alejandro", "carlos", "fernanda", "diana", "thaynara"]

        for token in doc:
            if token.text in pron:
                pronomes.append(token.text)
            elif token.pos_ == 'PRON' and token.text != "quem": #question
                pessoas.append(token.text)
            elif token.pos_ == 'VERB':
                verbos.append(token.lemma_)#Verbo raiz
            elif token.text == "foi":
                verbos.append(token.lemma_)#Verbo raiz
        if len(pessoas) == 1:
            contexto = ' '.join(pronomes + verbos + pessoas)
        else:
            contexto = ' '.join(pronomes + verbos)
            for pessoa in pessoas:
                contexto = ' '.join("Pessoa = " + pessoa)
        return contexto

    #translate_en
    def trad(text):
        from googletrans import Translator
        translator = Translator()
        translated_text = translator.translate(text, src='auto', dest='en').text
        return translated_text

    #VerificaSaudação en
    def is_saudacao(prompt):
        import spacy
        nlp = spacy.load("pt_core_news_lg")
        doc = nlp(prompt.lower())
        
        saudacoes = ["hi", "hello", "hey"]
        
        for token in doc:
            if token.text in saudacoes:
                return True
        
        return False

    # Início da árvore de Decisão:

    def choose(prompt=str):
        #Criando uma lista de tipos, buscando otimização no entendimento do contexto.
        #Considero que seja melhor dar um append do que verificar tipo a tipo.
        tipos = []

        pronome_encontrado = False
        contexto = []

        #Dicionário de palavras
        key_saudacoes =  ["oiee","oie","oii","oi","eae","olá","ola","salve","e ai","e aí","saudações", 
                    "saudaçoes", "saudacões", "saudacoes", "saudacao", "saudacão"]
        
        key_question = ["quem", "como", "quando", "pq", "onde", "qual"] #final ia "gostaria" "ficaria", porem tem certas chances dependendo do contexto, "eu ficaria com ela mas..." "eu ficaria fazendo?"

        key_thx = ["obrigado", "valeu", "obrigada", "vlw"]

        dicio = [key_saudacoes, key_question, key_thx]
        
        #Início padrão
        saudacao = "Olá, "
        start = "Start inicial"
        
        prompt, tipos = decisoes.caracteres_especiais(prompt, tipos)

        #Verificações baseadas no dicionário

        tamanho_prompt = prompt.split()
        if len(tamanho_prompt) == 1:
            if prompt in key_saudacoes:
                print(prompt.title() + ", Por favor reformule sua frase")
            elif prompt in key_thx:
                print("Denada!")
            elif prompt in key_question:
                print("Por favor, termine de escrever sua pergunta.")
            else:
                print('Vc escreveu "{}", pode reformular por favor?'.format(prompt))
        else:
            palavras = prompt.split()
            for palavra in palavras:
                for lista in dicio:
                    if palavra.lower() in lista:
                        if lista == key_saudacoes:
                            tipos.append("saudacao")
                            saudacao = palavra.title() + ", "
                        elif lista == key_question:
                            tipos.append("question")
                        elif lista == key_thx:
                            tipos.append("thx")
                        break
                if palavra.lower().endswith("ia"):
                    verbos = []
                    verbos.append(palavra)
        
        contexto = decisoes.extrair_contexto(prompt)
        
        #Verifica dia/tarde/noite

        if "bom dia" in prompt.lower():
            tipos.append("dia")

        if "boa tarde" in prompt.lower():
            tipos.append("tarde")

        if "boa noite" in prompt.lower():
            tipos.append("noite")
            
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