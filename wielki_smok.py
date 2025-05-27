from random import randint

class WielkiSmok:
    def __init__(self):
        self.nazwa = "Wielki Smok"
        self.hp = 500
        self.min_atak = 10
        self.max_atak = 25

    def czy_zyje(self):
        return self.hp > 0

    def zaatakuj(self, gracz):
        obrazenia = randint(self.min_atak, self.max_atak)
        if gracz.redukcja_obrazen:
            obrazenia = int(obrazenia * 0.5)
            gracz.redukcja_obrazen = False
            print("Zbroja zredukowała obrażenia o 50%!")
        gracz.life -= obrazenia
        print(f"{self.nazwa} atakuje i zadaje {obrazenia} obrażeń!")