from random import choice, randint
from tajemniczy_sklepik import Tajemniczy_sklepik
from tajemnicza_skrzynia import TajemniczaSkrzynia
from przeciwnik_z_lasu import PrzeciwnikZLasu
from wielki_smok import WielkiSmok

class PoziomLas:
    def __init__(self, gracz):
        self.gracz = gracz
        self.etap = 1
        self.max_etapy = 10

    def walcz_z_smokiem(self):
        smok = WielkiSmok()
        print('--' * 60)
        print("UWAGA! Pojawił się WIELKI SMOK!!")
        print('--' * 60)

        while smok.czy_zyje() and self.gracz.zyje():
            smok.zaatakuj(self.gracz)
            print(f"!!! Masz {max(0, self.gracz.life)} HP, {min(100, self.gracz.exp)} EXP !!!")

            print("Wybierz atak:")
            print("a --- Normalny atak")
            print("b --- Super uderzenie")
            print("c --- MEGA moc")
            print("d --- Power Ball")
            print("e --- Sprawdź ekwipunek")
            print("f --- Użyj przedmiotu")
            print("s --- Otwórz Tajemniczy sklepik")

            wybor = input("Wybór: ")

            if wybor == "a":
                atak = self.gracz.basic_atak()
            elif wybor == "b":
                atak = self.gracz.super_uderzenie()
            elif wybor == "c":
                atak = self.gracz.mega_moc()
            elif wybor == "d":
                atak = self.gracz.power_ball()
            elif wybor == "e":
                self.gracz.pokaz_ekwipunek()
                continue
            elif wybor == "f":
                self.gracz.uzyj_przedmiotu()
                continue
            elif wybor == "s":
                self.otworz_sklepik()
                continue
            elif wybor == "mode":
                decyzja = self.gracz.mode.aktywuj()
                if decyzja == "rozdzial2":
                    print("Skok do Rozdziału 2!")
                    return
                elif decyzja == "poziom2":
                    print("Skok do poziomu 2!")
                    continue
                elif decyzja == "poziom3":
                    print("Skok do Final Bossa!")
                    continue
                else:
                    continue
            else:
                print("Nieprawidłowy wybór!")
                continue

            smok.hp -= atak
            print(f"Zadajesz {atak} obrażeń! Wielki Smok ma teraz {max(0, smok.hp)} HP.")

        if not self.gracz.zyje():
            print("Zginąłeś w walce z Wielkim Smokiem...")
        else:
            print("GRATULACJE! Pokonałeś Wielkiego Smoka i wygrałeś grę!")

    def uruchom(self):
        print("--" * 60)
        print("TRAFIASZ DO CIEMNEGO I TAJEMNICZEGO LASU. MUSISZ PRZETRWAĆ POKONUJĄC POTWORY LEŚNE!")
        print("--" * 60)

        przeciwnicy_lasu = ["Goblin", "Wiedźmin", "Mały elf", "Nimfa wodna", "Leśny Troll"]


        while self.etap <= self.max_etapy and self.gracz.zyje():
            imie_przeciwnika = choice(przeciwnicy_lasu)
            przeciwnik = PrzeciwnikZLasu(imie_przeciwnika, base_life=30, etap=self.etap)

            print('--'*60)
            print(f"Etap {self.etap}: Napotykasz przeciwnika {przeciwnik.imie}, ma {przeciwnik.life} HP!")
            print('--'*60)

            while przeciwnik.life > 0 and self.gracz.zyje():
                obrazenia = przeciwnik.zadaj_obrazenia()

                if self.gracz.redukcja_obrazen:
                    obrazenia = int(obrazenia * 0.5)
                    self.gracz.redukcja_obrazen = False
                    print("Zbroja zredukowała obrażenia o 50%!")
                    
                self.gracz.life = max(0, self.gracz.life - obrazenia)
                print(f"{przeciwnik.imie} zadaje {obrazenia} obrażeń.")
                print(f"!!! Masz {max(0, self.gracz.life)} HP i {min(100, self.gracz.exp)} EXP !!!")
                if self.gracz.life < 0:
                    self.gracz.life = 0
                print("Wybierz atak:")
                print("a --- Normalny atak")
                print("b --- Super uderzenie")
                print("c --- MEGA moc")
                print("d --- Power Ball")
                print("e --- Sprawdź ekwipunek")
                print("f --- Użyj przedmiotu")
                print("s --- Otwórz Tajemniczy sklepik")

                wybor = input("Wybór: ")

                if wybor == "a":
                    atak = self.gracz.basic_atak()
                elif wybor == "b":
                    atak = self.gracz.super_uderzenie()
                elif wybor == "c":
                    atak = self.gracz.mega_moc()
                elif wybor == "d":
                    atak = self.gracz.power_ball()
                elif wybor == "e":
                    self.gracz.pokaz_ekwipunek()
                    continue
                elif wybor == "f":
                    self.gracz.uzyj_przedmiotu()
                    continue
                elif wybor == "s":
                    self.otworz_sklepik()
                    continue
                elif wybor == "mode":
                    decyzja = self.gracz.mode.aktywuj()
                    if decyzja == "rozdzial2":
                        print("Skok do Rozdziału 2!")
                        return "rozdzial2"
                    elif decyzja == "poziom2":
                        print("Pomijasz do poziomu 2.")
                        continue
                    elif decyzja == "poziom3":
                        print("Skok do Final Bossa!")
                        continue
                    else:
                        continue
                else:
                    print("Nie wybrano czynności")
                    continue
                przeciwnik.life -= atak
                print(f"Zadajesz {atak} obrażeń. {przeciwnik.imie} ma {max(0, przeciwnik.life)} HP.")

            if self.gracz.zyje():
                print(f"Pokonałeś przeciwnika {przeciwnik.imie} w etapie {self.etap}!")
                self.etap += 1
                self.gracz.exp += 10
                self.gracz.life = min(100, self.gracz.life)
                nagroda_monety = randint(50, 75 + self.etap * 10)
                self.gracz.monety += nagroda_monety
                print(f"Dostałeś 10 EXP i {nagroda_monety} monet!")
                print(f"Twoje monety: {self.gracz.monety}")
            else:
                print("Niestety, zostałeś pokonany!")
                return False
        print('--'*60)
        print("Przetrwałeś wszystkie 10 etapów!!! Czas na Bosa - Wielkiego Smoka!")
        self.walcz_z_smokiem()
        return True
    

    def otworz_sklepik(self):
        print("--- TAJEMNICZY SKLEPIK ---")
        print('--'*60)
        print(f"Twoje monety: {self.gracz.monety}")
        print('--'*60)
        for index, item in enumerate(Tajemniczy_sklepik, 1):
            print(f"{index}. {item['nazwa']} - Cena: {item['cena']} monet")
            print(f"   → Siła: {item['siła']}, Redukcja obrażeń: {item['redukcja_obrażeń']} - 50%, "
                  f"Wzrost HP: {item['wzrost_hp']}, Wzrost Siły: {item['wzrost_siły']}")
        print(f"{len(Tajemniczy_sklepik)+1}. Tajemnicza Skrzynia - Cena: 350 monet")
        print("Wpisz numer przedmiotu, który chcesz kupić lub wpisz 'exit' aby wyjść.")

        wybor = input("Twój wybór: ")
        if wybor == 'exit':
            return
        if not wybor.isdigit():
            print("Nieprawidłowy wybór. Wprowadż liczbę")
            return

        index = int(wybor) - 1
        if index == len(Tajemniczy_sklepik):
            skrzynia = TajemniczaSkrzynia()
            if self.gracz.monety >= skrzynia.cena:
                self.gracz.monety -= skrzynia.cena
                skrzynia.otworz(self.gracz)
            else:
                print("Nie masz wystarczająco monet na skrzynię!")
            return
        
        if 0 <= index < len(Tajemniczy_sklepik):
            item = Tajemniczy_sklepik[index]
            if self.gracz.monety >= item['cena']:
                self.gracz.monety -= item['cena']
                self.gracz.ekwipunek.append(item)
                print(f"Kupiłeś {item['nazwa']}! Dodano do ekwipunku.")
            else:
                print("Nie masz wystarczająco monet!")
        else:
            print("Nieprawidłowy numer.")
