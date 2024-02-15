# GAI
<h1>PT BR</h1>
A idéia do projeto é inovar em tudo o que possa imaginar
The idea of the project is innovate in all of things that U can think about

<h1>Prováveis próximas implementações no sistema:</h1>
<p>Compreender a maneira que o usuário "fala"/escreve e utilizar a mesma maneira para se comunicar com ele, fazendo ele sentir que está conversando com alguém que o entende</p>
<p>Procurar coisas que ele não sabe no google</p>
<p>Reconhecer perguntas indiretas</p>
<p>Código ser capaz de reparar a si mesmo (ignore a loucura desta idéia)</p>

<h1>Em implementação:</h1>

Algoritmo para gerar a certeza da resposta e as palavras usadas, ai as palavras que não foram usadas podem ter interligação com as erradas.
<h2>Exemplo:</h2>
<p>estava andando na praia e vi a estátua de salomão quem foi ele? me lembro de ver tbm a estátua de davi e joão, quem foram eles ah eu vi tbm outra estátua do joão q n sei qm é, quem foi, vi tbm os seus pais, quem foram eles</p>
<h2>Esta frase pode ser separada em:</h2>
<p>["Estava andando na praia e vi a estátua de salomão quem foi ele", "me lembro de ver tbm a estátua de davi e joão,", quem foram eles", "ah eu vi tbm outra estátua do joão q n sei qm é,", "quem foi,", "vi tbm os seus pais," "quem foram eles"]</p>
<h3>Tratando as frases separadas:</h3>
<p>Após separar, cada frase terá sua análise resultando em uma lista de respostas como por exemplo ["biografia de salomão", "informação", "palavra-chave", "biografia de joão", "palavra-chave", "informação", "palavra-chave"</p>
<h4>Dicionário dos significados:</h4>
<p>Bom, as respostas padrões são as biografias e tal, porém existirão termos que representarão palavras chaves em um nível mais baixo, por exemplo, ao invés de retornar ["resposta", "biografia de salomão"] poderá ser retornado ["informação", "me lembro de ver tbm a estátua de davi e joão"], claramente toda resposta terá uma série de informações importantes retiradas de si, que serão atreladas à ela como objeto, logo, vamos analisar a frase com o olhar do GAI...</p>
<h1>O olhar do GAI sobre a frase</h1>
<p>Primeiramente, a palavra estava refere-se ao verbo estar, que está na primeira pessoa, logo "eu estou" porém também está no passado, logo "eu estava" até aqui, apenas informações inúteis foram informadas, sabemos apenas que o usuário esteve no passado em algum local, logo esta informação será salva e consideraremos que retiramos 100% da informação destas palavras, em seguida será lido "na praia" (de duas em duas palavras, mas este número pode mudar), logo o usuário informou uma complementação, então a baixíssimo nível, sabemos mais informações sobre as duas informações anteriores que estão salvas) logo iremos atrelar esta informação, sabendo que o usuário, no passado, esteve andando(andar) na praia(local) afinal todo verbo precisa de uma pessoa que excecutou o verbo, e os verbos tem tipagem, andar pode (ou não) precisar de um local, pois eu posso andar na praia mas também posso andar meio triste.</p>
<p>Seguindo com a frase, sabemos que O usuário andou na praia, porém isto ainda não é uma pergunta, mas pode ser uma informação para solucionar a pergunta, então ainda manteremos a informação, com a observação que não sabemos em qual praia ele estava, afinal local tbm tem níveis de precisão. então será lido "e vi" o que indica, obviamente que o usuário viu algo, logo em seguida será lido "a estátua" indicando que o objeto visto foi uma estátua, ainda sem indentificação, também não é possível "rastrear" a esetátua pois não sabemos em qual praia ela foi vista, então seguimos analisando.</p>
<p>"de salomão" logo vemos q esta frase está, muito provavelmente completa, o usuário andou no passado em um local semi conhecido e encontrou um objeto mapeado e o datou como de salomão, logo seguimos em busca da pergunta para verificar a importancia desta informação na formação da resposta e do contexto da pergunta.</p>
<p>"quem foi ele?" mesmo se não houvesse ponto de interrogação, encontramos uma das 5 palavras que indicam uma dúvida, logo agora, temos a informação completa que o usuário andou no passado em uma praia desconhecida, encontrou um objeto (estatua) que está atrelado ao salomão porém a pergunta é relacionada ao salomão e não ao objeto (lembrando que absolutamente tudo q foi dito (e mais um pouco) terão níveis de certeza variáveis q mudarão dependendo da pergunta), logo sabemos q a resposta é "biografia de salomão", então quase todas as informações compreendidas serão apagadas e manteremos a informação q o usuário esteve na praia desconhecida, no passado (informações que ainda não tiveram atrelação)</p>
<p>"me lembro" apenas informa que o usuário se recorda, porém algo vago "de ver", indicando que algo foi visto junto ou próximo da estátua de salomão, criando uma atrelação entre as ifnormações, "também a", também fortifica a teoria da atrelamento entre as informações de salomão e das próximas palavras "estátua de" que são substantivos completados com "davi e" que precisão do complemento "joão" encerrando na "," logo davi e joão tem forte influencia na frase, então segue a leitura "quem foram", analisamos as próximas duas palavras pois não é "quem foi" mas sim "quem foram" e encontramos "eles ah", ignoramos o ah e reconhecemos a resposta "biografia de davi e joão", seguindo a leitura</p>
<p>"ah eu" buscamos algum verbo para o eu "vi" buscamos a informação do vi "tbm outra" o tbm fortifica que haverá informação, junto do outra que indica que algo que já foi visto foi revisto, indicando q provavelmente foi outra estátua (item mais visto). "estátua do" indicando que a idéia está correta e falta informação, "joão q" buscamos a continuação "n sei" indica que o usuário obviamente não sabe, logo a pergunta deve estar logo em seguida "qm é" indicando que a pergunta é sobre a biografia de joão, porém como é outra do joão, pode ser o mesmo joão, como isto fica incongruente, se não for encontrado mais informações sobre, junto da resposta perguntaremos se o usuário viu dois joão diferentes ou iguais, "quem foi" buscamos a continuação "vi tbm" mais informações "os seus" mais informações "pais," a virgula gera uma quebra, e concluimos que seus pais seriam os pais de joão ou de um dos joão, indicando q perguntar deve ser interessante para garantir, porfim vemos "quem foram eles" logo, fica incongruente se há uma ou duas estátuas de joão, se foi visto seus pais como pessoas ou estátuas que representam eles e, como a frase terminou, o quem foi sobrando após o "n sei qm é" fica atrelado a esta pergunta, dando foco ao joão, logo a resposta deve dar um valor mínimo da biografia de salomão, davi e joão mas focar no fato das dúvidas que sobraram, além de buscar pelos pais de um ou do joão mencionado.</p>
<h1>Em resumo</h1>
<p>Existem alguns estados em que o sistema pode se encontrar</p>
<h2>Estados do GAI</h2>
<p>Lendo: Quando ele está lendo uma palavra, frase ou trecho da pergunta</p>
<p>Analisando: Quando ele separou uma quantidade de informação da frase como "estava andando" e está analisando qual decisão/ação deve ser tomada</p>
<h3>Ações/Decisões</h3>
<p>Buscar por mais informações: volta o sistema ao estado de leitura, mantendo a informação da frase que foi lida por último (mais informações podem ser atreladas se necessário) e lendo as próximas sentenças considerando a frase anterior lida (e, se tiver suas informações e métricas)</p>
<p>Buscando verbo: Esta ação é chamada caso uma pessoa seja encontrada sem um verbo próximo, como por exemplo na sentença "ah eu" onde "eu" não contém um verbo, obviamente as frases anteriores podem ser consideradas antes de chamar esta ação</p>
<p>Gerando resposta/contexto solto: Esta ação gera uma resposta/contexto referente à tudo que já foi lido, e mantém as informações que ainda não houveram atrelação com mais "força" do que as informações que já contém atrelação</p>
<p>Gerar respsota e contexto final: Ultima ação tomada, leva em consideração toda a frase, sentenças, métricsa, respostas e contextos vistos, gera um contexto final como por exemplo "local: praia, tempo: passado" ... e uma "resposta" como "biografia de x, y e z"</p>
<h2>Quebras de leitura</h2>
<p>Existem caracteres, palavras chaves e coisas que forçam a parada da leitura para análise e tomada de decisão, segue lista:</p>
<ol>
  <li>Caracteres especiais</li>
  <li>Palavras que indicam pergunta ("Quem", "como", "onde", "por que", "quando")</li>
</ol>
<h2>Palavras que podem indicar informações em seguida ou anteriores à ela</h2>
<ol>
  <li>Perguntas de confirmação "Sério", "certeza"</li>
</ol>
<h1>Observação</h1>
<p>Mais informações serão adicionadas conforme suas implementações, tenha calma, sou um desenvolvedor solo...</p>

<h1>EN</h1>
The idea of the project is innovate in all of things that U can think about

<h1>Probably the next implementations in the system:</h1>
<p>Have the bot learn the way the user speaks, and use the same way to speak to the user, making them feel like they are talking to someone who understands them</p>
<p>Procurar coisas que ele não sabe no google</p>
<p>Reconhecer perguntas indiretas</p>
<p>Código ser capaz de reparar a si mesmo (ignore a loucura desta idéia)</p>
<p>Search things that he doesn't know on Google.</p>

<h1>Implementing:</h1>

Algorithm to generate the certainty of the answer and the words used, and the words that were not used may be linked to the wrong ones.
<h2>Exemple:</h2>
<p>I was walking on the beach and I saw the statue of Solomon who was he? I also remember seeing the statue of David and John, who were they oh I also saw another statue of John who I don't know who it is, who it was, I also saw his parents, who were they</p>
<h2>This sentence can be separated into:</h2>
<p>["I was walking on the beach and I saw the statue of Solomon, who was he", "I remember also seeing the statue of David and John", "who were they", "ah I also saw another statue of John who I don't know who he is ,", "who was it," "I also saw your parents," "who were they"]</p>
<h3>Treating the sentences separately:</h3>
<p>After separating, each sentence will have its analysis resulting in a list of answers such as ["solomão's biography", "information", "keyword", "john's biography", "keyword", "information", "keyword"</p>
<h4>Dictionary of meanings:</h4>
<p>Well, the standard answers are biographies and such, but there will be terms that represent key words at a lower level, for example, instead of returning ["answer", "biography of solomon"] it could be returned ["information", "I also remember seeing the statue of David and John"], clearly every answer will have a series of important information taken from it, which will be linked to it as an object, so let's analyze the sentence with GAI's perspective...</p>
<h1>GAI's vision about the phrase</h1>
<p>Firstly, the word was refers to the verb to be, which is in the first person, so "I am" but it is also in the past, so "I was" so far, only useless information has been provided, we only know that the user was in the passed somewhere, then this information will be saved and we will consider that we have removed 100% of the information from these words, then it will be read "on the beach" (every two words, but this number may change), then the user has entered a complement, so at a very low level, we know more information about the two previous pieces of information that are saved) we will then link this information, knowing that the user, in the past, was walking(walking) on ​​the beach(place) after all every verb needs a person who executed the verb, and verbs have typing, walking may (or may not) need a location, because I can walk on the beach but I can also walk a little sad.</p>
<p>Continuing with the sentence, we know that the user walked on the beach, but this is not yet a question, but it could be information to solve the question, so we will still keep the information, with the observation that we do not know which beach he was on, after all local also has levels of precision. then it will be read "and I saw" which obviously indicates that the user saw something, then it will be read "the statue" indicating that the object seen was a statue, still without identification, it is also not possible to "track" the statue because We don't know which beach she was seen on, so we continue analyzing.</p>
<p>"de solomão" we soon see that this sentence is, most likely complete, the user walked in the past in a semi-known location and found a mapped object and dated it as solomão, then we continue searching for the question to verify the importance of this information in formation of the answer and context of the question.</p>
<p>"Who was him?" even if there was no question mark, we found one of the 5 words that indicate a doubt, so now, we have complete information that the user walked in the past on an unknown beach, found an object (statue) that is linked to Solomon but the question is related to Solomon and not to the object (remembering that absolutely everything said (and a little more) will have variable levels of certainty that will change depending on the question), so we know that the answer is "Solomon's biography", so almost all the information understood will be deleted and we will keep the information that the user was on the unknown beach in the past (information that has not yet been linked)</p>
<p>"I remember" only informs that the user remembers, but something vague "to see", indicating that something was seen next to or close to the statue of Solomon, creating a link between the ifnormations, "also to", also strengthens the theory of linking the information about solomão and the next words "statue of" which are nouns completed with "davi and" the precision of the complement "joão" ending in "," therefore davi and joão have a strong influence on the sentence, so continue reading " who were", we analyze the next two words because it is not "who was" but "who were" and we find "they ah", we ignore the ah and recognize the answer "biography of davi and joão", following the reading</p>
<p>"ah eu" we look for some verb for the I "saw" we look for the information about the vi "also another" the also fortifies that there will be information, along with the other that indicates that something that has already been seen has been revised, indicating that it was probably another statue ( most viewed item). "statue of" indicating that the idea is correct and lacks information, "joão q" we look for the continuation "I don't know" indicates that the user obviously doesn't know, so the question must be right after "qm é" indicating that the question is about joão's biography, but as it is another joão, it could be the same joão, as this is incongruous, if no more information is found about it, next to the answer we will ask if the user has seen two different or the same joão, "who was it" we look for the continuation "I saw too" more information "yours" more information "parents," the comma creates a break, and we conclude that your parents would be the parents of João or one of João, indicating that asking must be interesting to ensure, finally we see "who they were" then, it becomes incongruous whether there are one or two statues of John, whether his parents were seen as people or statues that represent them and, as the sentence ended, who was left after the "I don't know who they are" " is linked to this question, focusing on John, so the answer must give a minimum value of the biography of Solomon, David and John but focus on the fact of the remaining doubts, in addition to searching for the parents of one or the mentioned John.</p>
<h1>Em resumo</h1>
<p>There are some states in which the system can find itself</p>
<h2>GAI states</h2>
<p>Reading: When he is reading a word, phrase or part of the question</p>
<p>Analyzing: When he has separated a quantity of information from the sentence such as "I was walking" and is analyzing what decision/action should be taken</p>
<h3>Actions/Decisions</h3>
<p>Search for more information: returns the system to the reading state, keeping the information of the sentence that was read last (more information can be added if necessary) and reading the next sentences considering the previous sentence read (and, if it has its information and metrics)</p>
<p>Seeking verb: This action is called if a person is found without a nearby verb, as for example in the sentence "ah eu" where "eu" does not contain a verb, obviously the previous sentences can be considered before calling this action</p>
<p>Generating a response/loose context: This action generates a response/context referring to everything that has already been read, and keeps the information that has not yet been linked with more "strength" than the information that already contains a link</p>
<p>Generate response and final context: Last action taken, takes into account the entire phrase, sentences, metrics, responses and contexts seen, generates a final context such as "location: beach, time: past" ... and a "response" as "biography of x, y and z"</p>
<h2>Readings breaks:</h2>
<p>There are characters, key words and things that force you to stop reading for analysis and decision making, below is the list:</p>
<ol>
  <li>Special characters</li>
  <li>Words that indicate question ("Who", "how", "where", "why", "when")</li>
</ol>
<h2>Words that can indicate information following or preceding it</h2>
<ol>
  <li>Confirmation questions "Really", "sure"</li>
</ol>
<h1>Comments:</h1>
<p>More information will be added as its implementations, don't worry, I'm a solo developer...</p>
