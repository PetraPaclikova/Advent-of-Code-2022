class Recept:

    def __init__(self, nazev, narocnost, url_adresa):
        self.nazev = nazev
        self.narocnost = narocnost
        self.url_adresa = url_adresa
        self.vyzkouseno = False
    
    def __str__(self):
        if int(self.narocnost) > 5:
            level = "pro zkusene kuchare"
        else:
            level = "pro zacatecniky"
        
        return f"Tento recept na {self.nazev}, ktery najdete na {self.url_adresa} je {level}" 

    def zmenit_narocnost(self, zmena_narocnosti):
        self.narocnost = zmena_narocnosti
        
    
    def uvareno(self):
        self.vyzkouseno = True

class Kucharka:
    def __init__(self, nazev, autor):
        self.nazev = nazev
        self.autor = autor
        self.recepty = []
        
    def __str__(self):
        return f"Kucharka {self.nazev} od autoru {self.autor} je plna skvelych receptu"

    def pocet_receptu(self):
        pocet_receptu = len(self.recepty)
        return pocet_receptu
        
    def pridej_recept(self,novy_recept):
        self.recepty.append(novy_recept)

    def vyzkouseny_recept(self):
        vyzkouseny_recept = []
        for x in self.recepty:
            if x.vyzkouseno:
                vyzkouseny_recept.append(x)
        return (vyzkouseny_recept)
                
    
                
                


gulas = Recept("gulas","2", "url adresa")
print(gulas)
kucharka1 = Kucharka("XY kucharka", "XY autor")
kucharka1.pridej_recept(gulas)
print(kucharka1.vyzkouseny_recept())
gulas.uvareno()
print(kucharka1.vyzkouseny_recept())












