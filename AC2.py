with open("AC2.txt", encoding = "utf-8") as list:
    list = list.readlines()
    print(list)

score = 0
# first part
for x in list:
    if x.strip() == "A X":
        score += 4
    elif x.strip() == "A Y":
        score += 8
    elif x.strip() == "A Z":
        score += 3
    elif x.strip() == "B X":
        score += 1
    elif x.strip() == "B Y":
        score += 5
    elif x.strip() == "B Z":
        score += 9
    elif x.strip() == "C X":
        score += 7
    elif x.strip() == "C Y":
        score += 2
    elif x.strip() == "C Z":
        score += 6
print(score)


# second part
for x in list:
    if x.strip() == "A X":
        score += 3
    elif x.strip() == "A Y":
        score += 4
    elif x.strip() == "A Z":
        score += 8
    elif x.strip() == "B X":
        score += 1
    elif x.strip() == "B Y":
        score += 5
    elif x.strip() == "B Z":
        score += 9
    elif x.strip() == "C X":
        score += 2
    elif x.strip() == "C Y":
        score += 6
    elif x.strip() == "C Z":
        score += 7
print(score)

   


