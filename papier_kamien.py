def papier(wybor_przeciwnika):
    if wybor_przeciwnika == "nozyce":
        return "Przegrales!", "SKIBIDI"
    elif wybor_przeciwnika == "kamien":
        return "wygrales!", "gracz"
    else:
        return "remis!", None
    

def kamien(wybor_przeciwnika):
    if wybor_przeciwnika == "papier":
        return "Przegrales!", "SKIBIDI"
    elif wybor_przeciwnika == "nozyce":
        return "wygrales!", "gracz"
    else:
        return "remis!", None


def nozyce(wybor_przeciwnika):
    if wybor_przeciwnika == "kamien":
        return "Przegrales!", "SKIBIDI"
    elif wybor_przeciwnika == "papier":
        return "wygrales!", "gracz"
    else:
        return "remis!", None
    
    