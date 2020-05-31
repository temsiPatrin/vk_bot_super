from wiki import Wiki
class Commander:
    hello = ["hello","ghbdtn","привет","хай"]
    whatsup = ["че как","че как?", "как дела","как дела?"]
    wiki = ["wiki", "википедия","вики"]
    last_msg = ""
    def ans(self,text:str):
        text = text.lower()
        if self.last_msg == "вики":
            w = Wiki()
            self.last_msg = ""
            return w.get_wiki(text)

        for i in self.hello:
            if text == i:
                self.last_msg = ""
                return "Привет, я БОТ_ИМЯ!\nЯ умею присылать статью из Википедии(напиши: вики или wiki)"

        for i in self.whatsup:
            if text == i:
                self.last_msg = ""
                return "У меня всгда все круто, я же рообот\nА у тебя как дела?"

        for i in self.wiki:
            if text == i:
                self.last_msg = "вики"
                return "Что ты хочешь узнать?"

        return "Я тебя не понял"
