from random import randint
from zgadnij_liczbe import sprawdz_liczbe, sprawdz_liczbe_2

class Poziom3:
    def __init__(self, gracz, mode):
        self.gracz = gracz
        self.mode = mode

    def uruchom(self):
        print("POZIOM 3: Zgadnij pierwszą liczbę BOSSa Rozdziału 1!")
        liczba_bossa = randint(1, 100)
        liczba_prob = 0

        while liczba_prob < 7:
            liczba = input("Zgadnij liczbę (1-100): ")
            if liczba == "mode":
                decyzja = self.mode.aktywuj(bez_full=True)
                if decyzja == "rozdzial2":
                    print("Przechodzisz do Rozdziału 2.")
                    return "rozdzial2"
                elif decyzja == "poziom2":
                    print("Pomijasz poziom 1.")
                    return True
                elif decyzja == "poziom3":
                    print("Skok do Final Bossa!")
                    return True
                else:
                    continue

            if not liczba.isdigit():
                print("Wprowadź poprawną liczbę!")
                continue

            liczba = int(liczba)
            if liczba == liczba_bossa:
                print("Zgadłeś pierwszą liczbę BOSSa!")
                break

            print(sprawdz_liczbe(liczba, liczba_bossa))
            liczba_prob += 1
            print(f"Liczba prób: {liczba_prob}/7")

        if liczba_prob == 7:
            print("Nie udało się odgadnąć wszystkich liczb Bossa. Koniec gry.")
            return False

        print("FINAL BOSS Rozdziału 1! Liczba od 1 do 1000!")
        liczba_bossa_2 = randint(1, 1000)
        liczba_prob_2 = 0

        while liczba_prob_2 < 12:
            liczba = input("Zgadnij liczbę (1-1000): ")
            if liczba == "mode":
                decyzja = self.mode.aktywuj(bez_full=True)
                if decyzja == "rozdzial2":
                    print("Przechodzisz do Rozdziału 2.")
                    return "rozdzial2"
                elif decyzja == "poziom2":
                    print("Skok do poziomu 2.")
                    return True
                elif decyzja == "poziom3":
                    print("Skok do Bossa rozdziału 1!")
                    return True
                else:
                    continue

            if not liczba.isdigit():
                print("Wprowadź poprawną liczbę!")
                continue

            liczba = int(liczba)
            if liczba == liczba_bossa_2:
                print("Zgadłeś drugą liczbę BOSSa!")
                break

            print(sprawdz_liczbe_2(liczba, liczba_bossa_2))
            liczba_prob_2 += 1
            print(f"Liczba prób: {liczba_prob_2}/12")

        if liczba_prob_2 == 12:
            print("Nie udało się odgadnąć wszystkich liczb Bossa. Koniec gry.")
            return False

        print("Gratulacje! Pokonałeś Final Bossa.")
        return True