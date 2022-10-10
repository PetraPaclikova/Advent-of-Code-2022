import math

def platne_cislo(cislo):
    if len(cislo) == 9 or len(cislo) == 13:
        return True
    else:
        return False

def platba_za_SMS(zprava):
        cena_zpravy = math.ceil(3*(len(zprava)/180))
        return cena_zpravy

cislo = input("Na jaké číslo chceš poslat zprávu")

print(platne_cislo(cislo))

if (platne_cislo(cislo)):
    zprava = input("Jakou zprávu chces poslat?")
    print(f"Cena za zpravu je {platba_za_SMS(zprava)} Kč")



    



        



        
