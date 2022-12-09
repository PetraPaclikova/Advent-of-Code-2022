import string
with open("AC3.txt", encoding = "utf-8") as list:
    list = list.readlines()
print(list)
# Fisrt_part
pismeno = []
soucet= 0
for x in list:
    x = x.strip()
    pulka = len(x)//2
    string1 = slice(0,pulka)
    string2 = slice(pulka, len(x))
    for y in x[string1]:
        if y in x[string2]:
            pismeno.append(y)
            break
print(len(pismeno))

for z in pismeno:
    if  z.isupper():
        soucet += ord(z)-38
    else:
        soucet += ord(z)-96
    print(z,soucet)
# Second_part
trojce = []
soucet_trojce = 0
for i in (range(0, len(list)-1, 3)):
    
    first = list[int(i)].strip()
    second= list[int(i+1)].strip()
    third= list[int(i+2)].strip()
    prunik =str(set(first)& set(second)& set(third)).replace("{'", "").replace("'}","")
    trojce.append(prunik)

print(trojce)
soucet_trojce=0
for x in trojce:
    if  x.isupper():
        soucet_trojce += ord(x)-38
    else:
        soucet_trojce += ord(x)-96
    print(x,soucet_trojce)


        