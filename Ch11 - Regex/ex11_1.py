# Write a simple program to simulate the operation of the grep command on Unix. Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

import re



fname = input("Enter file name: ")
fhand = open(fname)
user_input = input("Input regex command: ")
reg_exp = str(user_input)
count = 0

for line in fhand:
    line = line.rstrip()

    if re.findall(reg_exp, line) != []:
        count = count + 1


print(f"{fname} had {str(count)} lines that matched {reg_exp}")