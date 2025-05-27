from random import choice, randint
from tajemniczy_sklepik import Tajemniczy_sklepik

class TajemniczaSkrzynia:
    def __init__(self):
        self.nazwa = "Tajemnicza Skrzynia"
        self.cena = 350

    def otworz(self, gracz):
        print("--" * 30)
        print("Otwierasz Tajemniczą Skrzynię!")
        print("--" * 30)

        dostepne = Tajemniczy_sklepik.copy()
        dropy = []
        for _ in range(3):
            if dostepne:
                item = choice(dostepne)
                dropy.append(item)
                dostepne.remove(item)

        for przedmiot in dropy:
            gracz.ekwipunek.append(przedmiot)
            print(f"Otrzymałeś: {przedmiot['nazwa']}")

        if randint(1, 3) == 1:
            dodatkowe_monety = randint(1, 500)
            gracz.monety += dodatkowe_monety
            print(f"Otrzymałeś dodatkowo {dodatkowe_monety} monet!")
        print("--" * 30)