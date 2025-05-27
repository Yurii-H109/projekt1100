from random import randint
from postac import Postac

class Przeciwnik(Postac):
    def __init__(self, imie, life):
        base_life = life
        etap = 1
        exp = 0
        super().__init__(imie, life, base_life, etap, exp)

    def zadaj_obrazenia(self):
        return randint(3, 10)