
with open("znamky.txt", encoding = "utf-8") as znamky:
   student_znamky = znamky.readlines()

student_znamky_bez = [student_znamky.pop(0)]

nova_znamka_list = []
for znamka in student_znamky:
    nove_znamky = znamka.replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D").replace("5","E")
    nova_znamka_list.append(nove_znamky)

with open("nove_znamky.txt", mode = "w", encoding = "utf-8") as nove_znamky:
    nove_znamky.writelines(student_znamky_bez)
    nove_znamky.writelines(nova_znamka_list)



