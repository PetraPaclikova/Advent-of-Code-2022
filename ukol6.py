
with open("znamky.txt", encoding = "utf-8") as znamky:
    student_znamky = znamky.readlines()

nova_znamka_list = []
for znamka in student_znamky:
    nove_znamky = znamka.replace("1", "A").replace("2", "B").replace("3", "C").replace("4", "D").replace("5","E").replace("Test A", "Test 1").replace("Test B", "Test 2").replace("Test C", "Test 3").replace("Test D", "Test 4").replace("Test E", "Test 5")
    print(nove_znamky)
    nova_znamka_list.append(nove_znamky)

with open("nove_znamky.txt", mode = "w", encoding = "utf-8") as nove_znamky:
    nove_znamky.writelines(nova_znamka_list)



