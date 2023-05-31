from bs4 import BeautifulSoup

class Karticka():
    def __init__(self, sjednocena_data):
        soup = BeautifulSoup(sjednocena_data, "html.parser")
        self.otazka = soup.find(name="strong").text
        self.odpovedi = soup.findAll(name="li")
        self.obrazek = soup.find(name="img").get("src") if soup.find(name="img") != None else None # pokud obrazek neexistuje, tak by spadlo pri zjisteni textu src
        self.typ_otazky = self.ziskej_typ_otazky()
        self.vysvetleni = self.ziskej_vysvetleni(soup)
        self.spravne_odpovedi = self.ziskej_spravne_odpoved()


    def ziskej_typ_otazky(self): # Vrati typ (format) otazky, 1 = klasicky format (otazky), 2 = jen obrazek, 3 = otazky a obrazek
        if self.odpovedi != None and self.obrazek == None:
            return 0
        elif self.odpovedi == None and self.obrazek != None:
            return 1
        elif self.odpovedi != None and self.obrazek != None:
            return 2

    def ziskej_spravne_odpoved(self): # Vrati seznam spravnych odpovedi (ne jejich indexu)
        seznam = []
        for odpoved in self.odpovedi:
            if odpoved.find(name="strong") != None:
                seznam.append(self.odpovedi.index(odpoved)+1)
        return seznam


    def ziskej_vysvetleni(self, soup): # Vrati vysvetleni, nebo omluvni text pokud neexistuje
        paragrafy = soup.findAll(name="p")
        if len(paragrafy) == 2:
            return paragrafy[1].text
        elif len(paragrafy) == 3:
            return paragrafy[2].text
        else:
            return "Explanation to this question is not available"

    def vypis_odpovedi(self): # Vypise odpovedi v hezkem formatu
        if self.typ_otazky == 0:
            for i, odpoved in enumerate(self.odpovedi):
                print(f"{i+1}. {odpoved.text}")
        elif self.typ_otazky == 1:
            print(f"Available image: {self.obrazek}")
        elif self.typ_otazky == 2:
            for i, odpoved in enumerate(self.odpovedi):
                print(f"{i+1}. {odpoved.text}")
            print(f"Available image: {self.obrazek}")
        print() # Extra odradkovani


    def vypis_spravne_odpovedi(self): # Vypise spravne odpovedi v hezkem formatu
        if len(self.spravne_odpovedi) > 0:
            print("Correct answers are: ", end="")
            for odpoved in self.spravne_odpovedi:
                print(str(odpoved), end="")
                if self.spravne_odpovedi.index(odpoved) != (len(self.spravne_odpovedi)-1):
                    print(", ", end="")
            print()
        else:
            print("Correct answers are not available.")
