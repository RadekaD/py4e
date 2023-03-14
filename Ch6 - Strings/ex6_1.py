# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

name = "Danilo Radeka"
index = 0
while index < len(name):
    letter = name[-index - 1]
    print(letter)
    index = index + 1
