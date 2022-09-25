kod_baliku = input ('Jaký máš kod balíku?')
baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
baliky[kod_baliku]
if baliky[kod_baliku]: 
    print ('Balik je u kuryra')
else:
    print ('Balik neni u kuryra')


