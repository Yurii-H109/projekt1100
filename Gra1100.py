from random import randint, choice
from postac import Postac
from gracz import Gracz
from przeciwnik import Przeciwnik
from rozdzial1 import Rozdzial1
from rozdzial2 import Rozdzial2
from mode import Mode

        
class Gra:
    def __init__(self):
        imie = input("Witaj w grze pełnej przygód i zachwycających wątków!!! Podaj swoje imie: ")
        self.gracz = Gracz(imie, life=100, exp=100)
        self.mode = Mode(self.gracz)
        self.gracz.mode = self.mode
        self.rozdzial1 = Rozdzial1(self.gracz, self.mode)
        
    def play(self):
        self.rozdzial2 = Rozdzial2(self.gracz, self.mode)
        wynik = self.rozdzial1.uruchom_rozdzial()

        if wynik in ("rozdzial2", "poziom2", "poziom3", True):
            self.rozdzial2 = Rozdzial2(self.gracz, self.mode)
            self.rozdzial2.uruchom_rozdzial_2()


gra = Gra()
gra.play()