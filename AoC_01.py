with open("AC.txt", encoding = "utf-8") as AO:
   AO_list = AO.readlines()
list = []
soucet = 0
for x in AO_list:
    if x.strip().isdigit():
        soucet = soucet + int(x)
    else:
        list.append(soucet)
        soucet = 0
print(list)
max(list)