# Write a program to read through a file and print the contents of the file (line by line) all in upper case.

fhand = open("Esej_Nativizam.txt", encoding="utf-8")
for line in fhand:
    line = line.rstrip()
    print(line.upper())