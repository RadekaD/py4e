# Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.


import string


fname = input("Enter file name: ")
fhand = open(fname, encoding="utf-8")
letter_d = dict()

for line in fhand:
    line = line.translate(str.maketrans("", "", string.digits))
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            letter_d[letter] = letter_d.get(letter, 0) + 1
    
    
# print(letter_d)

tmp = list()
for key, value in letter_d.items():
    newt = (key, value)
    tmp.append(newt)


tmp = sorted(tmp)
for key, value in tmp:
    print(key, value)
