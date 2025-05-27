from poziom1 import Poziom1
from poziom2 import Poziom2
from poziom3 import Poziom3

class Rozdzial1:
    def __init__(self, gracz, mode):
        self.gracz = gracz
        self.mode = mode
        self.poziom1 = Poziom1(gracz, mode)
        self.poziom2 = Poziom2(gracz, mode)
        self.poziom3 = Poziom3(gracz, mode)

    def uruchom_rozdzial(self):
        print('--'*60)
        print("ROZDZIAL PIERWSZY: WPROWADZENIE...")
        print('--'*60)

        poziom1_wynik = self.poziom1.uruchom()

        if poziom1_wynik == "rozdzial2":
            return "rozdzial2"
        elif poziom1_wynik == "poziom2":
            if self.poziom2.uruchom():
                wynik = self.poziom3.uruchom()
                if wynik == "rozdzial2":
                    return "rozdzial2"
                elif wynik is True:
                    return True
                else:
                    return False
            else:
                return False
        elif poziom1_wynik == "poziom3":
            wynik = self.poziom3.uruchom()
            if wynik == "rozdzial2":
                return "rozdzial2"
            elif wynik is True:
                return True
            else:
                return False
        elif poziom1_wynik is True:
            print('!!' * 60)
            print("Ukończono poziom 1")
            print('!!' * 60)
            if self.poziom2.uruchom():
                print('!!' * 60)
                print("Ukończono poziom 2")
                print('!!' * 60)
                wynik = self.poziom3.uruchom()
                if wynik == "rozdzial2":
                    return "rozdzial2"
                elif wynik is True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False