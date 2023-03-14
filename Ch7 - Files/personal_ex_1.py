# Write a program that prints out all the lines that start with nativism, from your college essay.

fhand = open("Esej_Nativizam.txt", encoding="utf-8")

for line in fhand:
    line = line.rstrip()
    if line.startswith("Nativi"):
        print(line)