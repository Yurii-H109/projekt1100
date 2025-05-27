class Mode:
    def __init__(self, gracz):
        self.gracz = gracz

    def aktywuj(self, bez_full=False):
        print("== WYBIERZ ==")
        print("12 -- Papier-kamień-nożyce")
        print("13 -- Przejdź do Final Bossa (Poziom 3)")
        print("2 -- Pomiń do Rozdziału 2 (Las)")
        print("exit -- Powrót do gry")
        if not bez_full:
            print("full -- Wypełnij EXP i HP")
    
        wybor = input("Wybór: ")
        
        if wybor == "2":
            return "rozdzial2"
        elif wybor == "12":
            self.gracz.exp += 100
            return "poziom2"
        elif wybor == "13":
            self.gracz.exp += 100
            return "poziom3"
        elif wybor == "full" and not bez_full:
            self.gracz.exp = 100
            self.gracz.life = 100
            print("Ustawiono pełne EXP i HP.")
            return "kontynuuj"
        else:
            print("Nie wybrano czynności.")
            return "kontynuuj"