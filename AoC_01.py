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
print(max(list))
maximum1 = 67658
index = list.index(int(67658))
print(index)
list.pop(215)
print(max(list))
maximum2 =67344
index2 = list.index(int(67344))
print(index2)
list.pop(162)
print(max(list))
maximum3 = 65156
top3 = maximum1+maximum2+maximum3
print(top3)
