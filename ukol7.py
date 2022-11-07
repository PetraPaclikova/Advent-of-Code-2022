from datetime import datetime
date = input("datum?")
pocet_osob = input("a pocet osob?")

datum =datetime.strptime(str(date), "%d.%m.%Y")

zacatek_sezony = datetime(2021, 7, 1)
druha_sezona = datetime(2021, 8, 11)
konec_sezony = datetime(2021, 9, 1)

if datum < zacatek_sezony or datum > konec_sezony:
    print("Kino je zavrene")
elif datum >= zacatek_sezony and datum < druha_sezona:
    cena_listku = (250 * int(pocet_osob))
    print(f"cena listku je {cena_listku} Kč")
elif datum >= druha_sezona and datum < konec_sezony:
    cena_listku = (250 * int(pocet_osob))
    print(f"cena listku je {cena_listku} Kč")


