from random import choice
from papier_kamien import papier, kamien, nozyce

class Poziom2:
    def __init__(self, gracz, mode):
        self.gracz = gracz
        self.mode = mode

    def uruchom(self):
        print("POZIOM 2: Gra w Papier-Kamień-Nożyce przeciwko SKIBIDI!")
        wygrane = 0
        przegrane = 0
        opcje = ["papier", "kamien", "nozyce"]

        while wygrane < 10 and przegrane < 10:
            print("Wybierz: p (papier), k (kamien), n (nożyce), stop")
            wybor = input()

            if wybor == "stop":
                return False
            elif wybor == "mode":
                decyzja = self.mode.aktywuj(bez_full=True)
                if decyzja == "poziom2":
                    print("Pomijasz poziom 1.")
                    continue
                elif decyzja == "rozdzial2":
                    print("Przechodzisz do Rozdziału 2.")
                    return "rozdzial2"
                elif decyzja == "poziom3":
                    print("Skok do Final Bossa!")
                    return "poziom3"
                else:
                    continue

            if wybor == "p":
                gracz_wybor = "papier"
            elif wybor == "k":
                gracz_wybor = "kamien"
            elif wybor == "n":
                gracz_wybor = "nozyce"
            else:
                print("Nieprawidłowa opcja!")
                continue

            skibidi_wybor = choice(opcje)
            print(f"Ty: {gracz_wybor}, SKIBIDI: {skibidi_wybor}")

            if gracz_wybor == "papier":
                wynik, zwyciezca = papier(skibidi_wybor)
            elif gracz_wybor == "kamien":
                wynik, zwyciezca = kamien(skibidi_wybor)
            else:
                wynik, zwyciezca = nozyce(skibidi_wybor)
            print(wynik)

            if zwyciezca == "gracz":
                wygrane += 1
            elif zwyciezca == "SKIBIDI":
                przegrane += 1
            print(f"Wygrane: {wygrane}/10, Przegrane: {przegrane}/10")

        if wygrane == 10:
            return True
        else:
            print("Niestety, nie udało się wygrać w grę papier-kamień-nożyce")
            return False