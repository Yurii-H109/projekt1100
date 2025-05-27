from random import randint
from postac import Postac

class PrzeciwnikZLasu(Postac):
    def __init__(self, imie, base_life, etap):
        obecne_life = base_life + etap * 10
        super().__init__(imie, obecne_life, base_life, etap, exp=0)

    def zadaj_obrazenia(self):
        return randint(5, 15)