import wikipedia

class Wiki:
    wikipedia.set_lang("ru")
    def get_wiki(self,text):
        try:
            s1 = wikipedia.summary(text,3)
            s2 = wikipedia.page(text).url
            return s1 + "\n" +s2
        except Exception as e:
            print(e.__str__())
            return "Попробуй другой запрос"