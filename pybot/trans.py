from translate import Translator
def translate(text, to_lang="ru"):
    return Translator(to_lang=to_lang).translate(text)
