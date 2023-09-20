def trad(text):
        from googletrans import Translator
        translator = Translator()
        translated_text = translator.translate(text, src='auto', dest='en').text
        return translated_text