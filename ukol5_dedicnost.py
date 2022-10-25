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
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni, varianty):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = [varianty]

        
    def pridej_variantu(self, varianta):
        self.varianta = varianta
        self.varianty.append(self.varianta)
        return (self.varianty)
    
    def __str__(self):

        return super().__str__() + f" varianta: {' ,'.join(self.varianty)}"






