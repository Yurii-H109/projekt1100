from random import randint
from postac import Postac

class Gracz(Postac):
    def __init__(self, imie, life, exp):
        base_life = life
        etap = 1
        super().__init__(imie, life, base_life, etap, exp)
        self.ekwipunek = []
        self.bonus_do_ataku = 0
        self.redukcja_obrazen = False
        self.mode = None
        self.monety = 0

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)
        print('--'*60)
        print(f"Dodano do ekwipunku: {przedmiot['nazwa']}, którero możesz użyć już teraz! kliknij 'f' by użyć.")
        print('--'*60)

    def pokaz_ekwipunek(self):
        if not self.ekwipunek:
            print("!!!Ekwipunek jest pusty!!!")
        else:
            print('--'*60)
            print("Ekwipunek:")
            for item in self.ekwipunek:
                print(f"- {item['nazwa']}")
                print('--'*60)

    def basic_atak(self):
        koszt = randint(1, 6)
        if self.exp < koszt:
            print("Nie masz wystarczającej ilości EXP!")
            return 0
        self.exp -= koszt
        obrazenia = randint(3, 20) + self.bonus_do_ataku
        self.bonus_do_ataku = 0
        return obrazenia

    def super_uderzenie(self):
        koszt = randint(2, 5)
        if self.exp < koszt:
            print("Nie masz wystarczającej ilości EXP!")
            return 0
        self.exp -= koszt
        obrazenia = randint(15, 25) + self.bonus_do_ataku
        self.bonus_do_ataku = 0
        return obrazenia

    def mega_moc(self):
        koszt = randint(3, 5)
        if self.exp < koszt:
            print("Nie masz wystarczającej ilości EXP!")
            return 0
        self.exp -= koszt
        obrazenia = randint(18, 28) + self.bonus_do_ataku
        self.bonus_do_ataku = 0
        return obrazenia

    def power_ball(self):
        koszt = randint(4, 6)
        if self.exp < koszt:
            print("Nie masz wystarczającej ilości EXP!")
            return 0
        self.exp -= koszt
        obrazenia = randint(15, 35) + self.bonus_do_ataku
        self.bonus_do_ataku = 0
        return obrazenia
    

    def uzyj_przedmiotu(self):
        if not self.ekwipunek:
            print("Nie masz żadnych przedmiotów!")
            return

        print("Wybierz przedmiot do użycia:")
        for index, item in enumerate(self.ekwipunek, 1):
            print(f"{index}. {item['nazwa']}")

        wybor_input = input("Numer przedmiotu: ")

        if not wybor_input.isdigit():
            print("Wprowadź liczbe.")
            return

        wybor_przedmiotu = int(wybor_input) - 1

        if 0 <= wybor_przedmiotu < len(self.ekwipunek):
            przedmiot = self.ekwipunek.pop(wybor_przedmiotu)
            print(f"Użyto przedmiotu: {przedmiot['nazwa']}")

            if przedmiot['nazwa'] == "Miecz SIGMY":
                self.bonus_do_ataku += 10
                print('--'*60)
                print("Twój następny atak zada +10 obrażeń!")
                print('--'*60)
            elif przedmiot['nazwa'] == "Eliksir Życia":
                self.life = min(100, self.life + 20)
                print('--'*60)
                print("Odzyskałeś 20 HP!")
                print('--'*60)
            elif przedmiot['nazwa'] == "Zbroja z Metalu":
                self.redukcja_obrazen = True
                self.exp += 10
                print('--'*60)
                print("Odzyskałeś 10 EXP!")
                print("Założyłeś Zbroję z Metalu! Następny atak SIGMY zada o 50% mniej obrażeń.")
                print('--'*60)
            elif przedmiot['nazwa'] == "Posąg Wiedźmina":
                self.redukcja_obrazen = True
                self.bonus_do_ataku += 10
                print('--'*60)
                print("Wykorzystałeś Posąg Wiedźmina! Następny atak przeciwnika zada o 50% mniej obrażeń.")
                print("Twój następny atak zada +10 obrażeń!")
                print('--'*60)
            elif przedmiot['nazwa'] == "Hełm Goblina":
                self.redukcja_obrazen = True
                self.life = min(100, self.life + 10)
                self.exp += 5
                print('--'*60)
                print("Wykorzystałeś Hełm Goblina! Następny atak przeciwnika zada o 50% mniej obrażeń.")
                print("Odzyskałeś 10 HP!")
                print("Odzyskałeś 5 EXP!")
                print('--'*60)
            elif przedmiot['nazwa'] == "Eliksir Mocy":
                self.bonus_do_ataku += 30
                print('--'*60)
                print("Wykorzystałeś Eliksir Mocy!")
                print("Twój następny atak zada +30 obrażeń!")
                print('--'*60)
            else:
                print("Przedmiot nie ma specjalnego efektu.")
        else:
            print("Nieprawidłowy wybór.")

    def wybierz_atak(self):
        print("Wybierz atak:")
        print('a --- Wykonaj Normalny Atak')
        print('b --- Super uderzenie!')
        print('c --- MEGA moc!!')
        print('d --- Power Ball!!')
        print('e --- Sprawdź ekwipunek')
        print('f --- Użyj przedmiotu')
        wybor = input()
    
        if wybor == 'a':
            return self.basic_atak()
        elif wybor == 'b':
            return self.super_uderzenie()
        elif wybor == 'c':
            return self.mega_moc()
        elif wybor == 'd':
            return self.power_ball()
        elif wybor == 'e':
            self.pokaz_ekwipunek()
            return 0
        elif wybor == 'f':
            self.uzyj_przedmiotu()
            return self.wybierz_atak()
        elif wybor == "mode":
            return self.mode.aktywuj()
        else:
            print("Nieprawidłowy wybór.")
            return 0