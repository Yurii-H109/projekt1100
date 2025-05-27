from random import choice, randint
from przeciwnik import Przeciwnik

class Poziom1:
    def __init__(self, gracz, mode):
        self.gracz = gracz
        self.mode = mode
        self.sigma = Przeciwnik("SIGMA", life=50)
        self.liczba_wygranych = 0

    def uruchom(self):
        print(f"Zapraszam gracza {self.gracz.imie} do Rozdziału pierwszego!")
        print("POZIOM 1. Pokonaj przeciwnika 'SIGMA'")
        print('--'*60)

        while self.gracz.zyje() and self.liczba_wygranych < 5:
            obrazenia = self.sigma.zadaj_obrazenia()

            if self.gracz.redukcja_obrazen:
                obrazenia = int(obrazenia * 0.5)
                self.gracz.redukcja_obrazen = False
                print("Zbroja zredukowała obrażenia o 50%!")

            self.gracz.life = max(0, self.gracz.life - obrazenia)
            self.gracz.exp = max(0, self.gracz.exp - randint(2, 5))

            print(f"{self.sigma.imie} zadaje Ci {obrazenia} obrażeń.")
            print(f"!!! Masz {round(self.gracz.life)} HP i {round(self.gracz.exp)} EXP !!!")

            atak = self.gracz.wybierz_atak()
            
            if atak == "poziom2":
                print("Pomijasz poziom 1, przechodzisz do poziomu 2!")
                return "poziom2"
            elif atak == "poziom3":
                print("Przeskok do Final Bossa!")
                return "poziom3"
            elif atak == "rozdzial2":
                print("Przeskok do Rozdziału 2!")
                return "rozdzial2"
            elif atak == "kontynuuj":
                continue
            else:
                self.sigma.life -= atak
                self.sigma.life = max(0, self.sigma.life)
                print(f"Zadałeś {atak} obrażeń SIGMIE.")
                print(f"SIGMA ma teraz {self.sigma.life} HP.")

            if self.sigma.life <= 0:
                self.liczba_wygranych += 1
                self.sigma.life = 50
                print(f"Pokonałeś SIGMĘ! Zwycięstw: {self.liczba_wygranych}/5.")

                nagrody = [
    {
        'nazwa': 'Miecz SIGMY',
        'bonus do ataku': 10
    },
    {
        'nazwa': 'Eliksir Życia',
        'wzrost_hp': 20
    },
    {
        'nazwa': 'Zbroja z Metalu',
        'redukcja_obrażeń': 0.5,
        'wzrost_exp': 10
    }
]

                przedmiot = choice(nagrody)
                self.gracz.dodaj_przedmiot(przedmiot)

        if not self.gracz.zyje():
            print("Zostałeś pokonany!")
            return False
        return True