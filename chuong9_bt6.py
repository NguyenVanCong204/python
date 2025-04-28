class Vietnam:
    def capital(self):
        print("Thủ đô của Việt Nam là Hà Nội")
    
    def language(self):
        print("Ngôn ngữ của Việt Nam là Vietnamese.")

class Japan:
    def capital(self):
        print("Thủ đô của Nhật Bản là Tokyo.")
    
    def language(self):
        print("Ngôn ngữ của Nhật Bản là Japanese.")

def aboutCountry(country):
    country.capital()
    country.language()

vietnam = Vietnam()
japan = Japan()

aboutCountry(vietnam)
aboutCountry(japan)