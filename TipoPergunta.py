class QuestionNeuron:
    def __init__(self):
        # Dicionário de palavras-chave para cada tipo de pergunta
        self.keywords = {
            "quem": ["quem", "alguém"],
            "quando": ["quando"],
            "porque": ["porque", "motivo", "razão", "por que", "por quê", "porquê", "pq"],
            "como": ["como"],
            "quanto": ["quanto"],
            "onde": ["onde"],
            "qual": ["qual"]
        }
    
    def QuestionType(self, question):
        tipoPergunta = []
        question_lower = question.lower()
        
        words = question_lower.split()
        
        if "por" in words and "que" in words:
                index_por = words.index("por")
                index_que = words.index("que")
                if index_que == index_por + 1:
                    words[index_por] = "porque"
                    words.pop(index_que)
                    
        if "por" in words and "que?" in words:
                index_por = words.index("por")
                index_que = words.index("que?")
                if index_que == index_por + 1:
                    words[index_por] = "porque"
                    words.pop(index_que)
        
        
        for word in words:
            if word[-1] == "!" or word[-1] == "." or word[-1] == "?":
                word = word[:-1]
            for question_type, keywords_list in self.keywords.items():
                if word in keywords_list:
                    tipoPergunta.append(question_type)
                    break
        
        if tipoPergunta:
            tipo = ("Tipo de pergunta: " + " e ".join(tipoPergunta) + ".")
            return tipo
        else:
            return "Tipo de pergunta desconhecido ou não é uma pergunta."