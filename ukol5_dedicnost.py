class Nemoc:
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, varianta = []):
        super().__init__(jmeno, inkubacni_doba = 7, pocet_obeti = 0, sireni = "vzducehm")
        self.varianta = varianta
        
    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)
        
    def __str__(self):

        return super().__str__() + f" varianta: {' ,'.join(self.varianty)}"






