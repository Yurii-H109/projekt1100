from poziom_las import PoziomLas

class Rozdzial2:
    def __init__(self, gracz, mode):
        self.gracz = gracz
        self.mode = mode
        self.poziom_las = PoziomLas(gracz)

    def uruchom_rozdzial_2(self):
        print('--' * 60)
        print("ROZDZIAŁ DRUGI: TAJEMNICZA PRZYGODA W LESIE!")
        print(f"Witaj, graczu {self.gracz.imie}, w Rozdziale drugim. Wyruszasz na nową przygodę...")
        print('--' * 60)

        if self.poziom_las.uruchom():
            print('!!'*60)
            print("Ukończyłeś leśną przygodę!")
            print('!!'*60)
        else:
            print("Nie przetrwałeś starcia z potworami lasu...")