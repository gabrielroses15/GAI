# GAI
A idéia do projeto é inovar em tudo o que possa imaginar

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
