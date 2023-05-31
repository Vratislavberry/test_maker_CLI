from karticka import Karticka

class Deck:
    def __init__(self, sjednocena_data):
        self.karticky = [Karticka(prvek) for prvek in sjednocena_data]
        self.pocet_v_zakladu = len(self.karticky)
        self.spravne_counter = 0
        self.spatne_counter = 0

    def pocet_karticek(self):
        return len(self.karticky)

    def vypis_kartu(self):
        if self.pocet_karticek() > 0:
            print(self.karticky[0].otazka+"\n")
            self.karticky[0].vypis_odpovedi()

    def spravne_odpovedi(self):
        return self.karticky[0].spravne_odpovedi

    def smaz_kartu(self): # Vyhodi kartu z balicku
        self.karticky.pop(0)

    def zmen_kartu(self): # Vlozi aktualni kartu na konec balicku
        temp_karta = self.karticky.pop(0)
        self.karticky.append(temp_karta)

    def vypis_vysvetleni(self):
        print(self.karticky[0].vysvetleni)

    def get_procenta_celkove(self): # Vrati, kolik procent z CELEHO testu jsem odpovedel spravne
        procenta = round((self.spravne_counter/self.pocet_v_zakladu)*100,2) # Spocitano pomoci trojclenky
        return procenta

    def get_procenta_relativne(self): # Vrati na kolik procent otazek, ktere jsem jiz videl, jsem odpovedel spravne
        pocet_odpovedi = self.spravne_counter + self.spatne_counter
        if pocet_odpovedi != 0: # Zabraneni deleni nulou
            procenta = round((self.spravne_counter/pocet_odpovedi)*100, 2)
        else:
            procenta = 0.00
        return procenta







