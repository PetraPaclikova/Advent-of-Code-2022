import math

def platne_cislo(cislo):
    cislo = cislo.replace(" ","")
    return len(cislo) == 9 or (len(cislo) == 13 and (cislo[0:4]) == "+420" )
        
def platba_za_SMS(zprava):
        cena_zpravy = math.ceil((len(zprava)/180))*3
        return cena_zpravy

cislo = input("Na jaké číslo chceš poslat zprávu")

if (platne_cislo(cislo)) == False:
    print("Neplatné číslo")

if (platne_cislo(cislo)):
    zprava = input("Jakou zprávu chces poslat?")
    print(f"Cena za zpravu je {platba_za_SMS(zprava)} Kč")



    



        



        
