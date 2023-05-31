import requests
from bs4 import BeautifulSoup
from deck import Deck
import os



def ziskej_int(): # Tato funkce bude od uzivatele chtit vstup tak dlouho, dokud nedostane int
    je_int = False
    while je_int == False:
        try:
            vstup = int(input("Answer: "))
            je_int = True
        except:
            pass
    return vstup




# Ziskani dat
os.system("cls")
STRANKA = input("Enter a webpage with questions from itexamanswers: ")
response = requests.get(STRANKA)

soup = BeautifulSoup(response.text, "html.parser")
data = soup.find(class_="thecontent clearfix")

# Sjednoceni tagu
data = str(data)
data = data.replace("<b>", "<strong>")
data = data.replace("</b>", "</strong>")

seznam_dat = data.split("<p><strong>")
for i in range(len(seznam_dat)):
    seznam_dat[i] = "<p><strong>" + seznam_dat[i] + "</div>"

# Vytvoreni sjednocenych dat
sjednocena_data = []
for prvek in seznam_dat:
    if prvek[11:23] == "Explanation:": # od indexu 11 zacina text v <p><strong>, pokud je ten text vysvetleni otazky, tak se prideli k dane otazce
        sjednocena_data[-1] += prvek
    elif prvek[11].isdigit():
        sjednocena_data.append(prvek)



# Kviz
deck = Deck(sjednocena_data) # Vytvoreni decku s kartickama
while deck.pocet_karticek() != 0:
    os.system("cls")
    print(f"Remaining questions: {deck.pocet_karticek()}/{deck.pocet_v_zakladu}"
          f"\nRelative success rate: {deck.get_procenta_celkove()}% "
          f"\nAbsolute success rate: {deck.get_procenta_relativne()}% "
          f"\n{'-'*50}\n")
    deck.vypis_kartu()

    jiz_recene_odpovedi = [] # odpoved uzivatele a jeji zpracovani
    for _ in range(len(deck.spravne_odpovedi())):
        user_odpoved = ziskej_int()
        if user_odpoved in deck.spravne_odpovedi() and user_odpoved not in jiz_recene_odpovedi:
            print("Correct")
            jiz_recene_odpovedi.append(user_odpoved)
        else:
            print("Incorrect")
    print()
    deck.vypis_vysvetleni()
    if len(jiz_recene_odpovedi) == len(deck.spravne_odpovedi()):
        print("Answer is completely correct")
        deck.spravne_counter += 1
        deck.smaz_kartu()
    else:
        print("Answer is not completely correct")
        deck.zmen_kartu()
        deck.spatne_counter += 1
    input("\nDo you want to continue? (ctrl+c to quit)")























