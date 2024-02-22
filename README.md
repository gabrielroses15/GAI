# GAI
The idea of the project is innovate in all of things that U can think about.

<h1>Probably the next implementations in the system:</h1>
<p>Have the bot learn the way the user speaks, and use the same way to speak to the user, making them feel like they are talking to someone who understands them.</p>
<p>Procurar coisas que ele não sabe no google.</p>
<p>Reconhecer perguntas indiretas.</p>
<p>Código ser capaz de reparar a si mesmo (ignore a loucura desta idéia)</p>
<p>Search things that he doesn't know on Google.</p>

<h1>Implementing:</h1>

Algorithm to generate the certainty of the answer and the words used, and the words that were not used may be linked to the wrong ones.
<h2>Exemple:</h2>
<p>I was walking on the beach and I saw the statue of Solomon who was he? I also remember seeing the statue of David and John, who were they oh I also saw another statue of John who I don't know who it is, who it was, I also saw his parents, who were they</p>
<h2>This sentence can be separated into:</h2>
<p>["I was walking on the beach and I saw the statue of Solomon, who was he", "I remember also seeing the statue of David and John", "who were they", "ah I also saw another statue of John who I don't know who he is ,", "who was it," "I also saw your parents," "who were they"]</p>
<h3>Treating the sentences separately:</h3>
<p>After separating, each sentence will have its analysis resulting in a list of answers such as ["solomão's biography", "information", "keyword", "john's biography", "keyword", "information", "keyword".</p>
<h4>Dictionary of meanings:</h4>
<p>Well, the standard answers are biographies and such, but there will be terms that represent key words at a lower level, for example, instead of returning ["answer", "biography of solomon"] it could be returned ["information", "I also remember seeing the statue of David and John"], clearly every answer will have a series of important information taken from it, which will be linked to it as an object, so let's analyze the sentence with GAI's perspective...</p>
<h1>GAI's vision about the phrase.</h1>
<p>Firstly, the word was refers to the verb to be, which is in the first person, so "I am" but it is also in the past, so "I was" so far, only useless information has been provided, we only know that the user was in the passed somewhere, then this information will be saved and we will consider that we have removed 100% of the information from these words, then it will be read "on the beach" (every two words, but this number may change), then the user has entered a complement, so at a very low level, we know more information about the two previous pieces of information that are saved) we will then link this information, knowing that the user, in the past, was walking(walking) on ​​the beach(place) after all every verb needs a person who executed the verb, and verbs have typing, walking may (or may not) need a location, because I can walk on the beach but I can also walk a little sad.</p>
<p>Continuing with the sentence, we know that the user walked on the beach, but this is not yet a question, but it could be information to solve the question, so we will still keep the information, with the observation that we do not know which beach he was on, after all local also has levels of precision. then it will be read "and I saw" which obviously indicates that the user saw something, then it will be read "the statue" indicating that the object seen was a statue, still without identification, it is also not possible to "track" the statue because We don't know which beach she was seen on, so we continue analyzing.</p>
<p>"de solomão" we soon see that this sentence is, most likely complete, the user walked in the past in a semi-known location and found a mapped object and dated it as solomão, then we continue searching for the question to verify the importance of this information in formation of the answer and context of the question.</p>
<p>"Who was him?" even if there was no question mark, we found one of the 5 words that indicate a doubt, so now, we have complete information that the user walked in the past on an unknown beach, found an object (statue) that is linked to Solomon but the question is related to Solomon and not to the object (remembering that absolutely everything said (and a little more) will have variable levels of certainty that will change depending on the question), so we know that the answer is "Solomon's biography", so almost all the information understood will be deleted and we will keep the information that the user was on the unknown beach in the past (information that has not yet been linked)</p>
<p>"I remember" only informs that the user remembers, but something vague "to see", indicating that something was seen next to or close to the statue of Solomon, creating a link between the ifnormations, "also to", also strengthens the theory of linking the information about solomão and the next words "statue of" which are nouns completed with "davi and" the precision of the complement "joão" ending in "," therefore davi and joão have a strong influence on the sentence, so continue reading " who were", we analyze the next two words because it is not "who was" but "who were" and we find "they ah", we ignore the ah and recognize the answer "biography of davi and joão", following the reading.</p>
<p>"ah eu" we look for some verb for the I "saw" we look for the information about the vi "also another" the also fortifies that there will be information, along with the other that indicates that something that has already been seen has been revised, indicating that it was probably another statue ( most viewed item). "statue of" indicating that the idea is correct and lacks information, "joão q" we look for the continuation "I don't know" indicates that the user obviously doesn't know, so the question must be right after "who is" indicating that the question is about joão's biography, but as it is another joão, it could be the same joão, as this is incongruous, if no more information is found about it, next to the answer we will ask if the user has seen two different or the same joão, "who was it" we look for the continuation "I saw too" more information "yours" more information "parents," the comma creates a break, and we conclude that your parents would be the parents of João or one of João, indicating that asking must be interesting to ensure, finally we see "who they were" then, it becomes incongruous whether there are one or two statues of John, whether his parents were seen as people or statues that represent them and, as the sentence ended, who was left after the "I don't know who they are" " is linked to this question, focusing on John, so the answer must give a minimum value of the biography of Solomon, David and John but focus on the fact of the remaining doubts, in addition to searching for the parents of one or the mentioned John.</p>
<h1>Em resumo.</h1>
<p>There are some states in which the system can find itself.</p>
<h2>GAI states:</h2>
<p>Reading: When he is reading a word, phrase or part of the question</p>
<p>Analyzing: When he has separated a quantity of information from the sentence such as "I was walking" and is analyzing what decision/action should be taken</p>
<h3>Actions/Decisions</h3>
<p>Search for more information: returns the system to the reading state, keeping the information of the sentence that was read last (more information can be added if necessary) and reading the next sentences considering the previous sentence read (and, if it has its information and metrics)</p>
<p>Seeking verb: This action is called if a person is found without a nearby verb, as for example in the sentence "ah eu" where "eu" does not contain a verb, obviously the previous sentences can be considered before calling this action.</p>
<p>Generating a response/loose context: This action generates a response/context referring to everything that has already been read, and keeps the information that has not yet been linked with more "strength" than the information that already contains a link</p>
<p>Generate response and final context: Last action taken, takes into account the entire phrase, sentences, metrics, responses and contexts seen, generates a final context such as "location: beach, time: past" ... and a "response" as "biography of x, y and z".</p>
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

<h1>Example of probably the analyses metrics:</h1>
<p>
  {
    "answerFounded": boolean,
    answer: string,
    "answersFounded": boolean,
    answers: string list,
    context: string,
    contexts: string list,
    words: string list,
    tokens: string list,
    importance: int list,
    themes: string list,
    multipleThemes: boolean
    mainTheme: string,
    mainThemes: string list,
    info: string list,
    names: string list,
    verbs: string list,
    verb-tenses: string list,
    locationOfAnswer: {
      precision: float,
      locate: string,
      references: string,
      context: string
      }
    objects: {
      found: boolean,
      number: int,
      objectsList: string,,
      importance: int list or int
    }
    noSenseSentences: string list
  }
</p>

<h1>
  My anottations (ignore-it)
</h1>

<p>Make a website</p>
<p>Update linkdlen</p>
<p>Update github</p>
<p>Update issues place</p>
<p>Update money helps</p>
<p>Update social media</p>
<p>use my business mail (found one free)</p>
<p>put the readme to change, if the user is from us or br</p>
