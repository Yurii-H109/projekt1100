class Postac:
    def __init__(self, imie, life, base_life, etap, exp):
        self.imie = imie
        self.life = life
        self.base_life = base_life
        self.etap = etap
        self.exp = exp

    def zyje(self):
        return self.life > 0 and self.exp > 0