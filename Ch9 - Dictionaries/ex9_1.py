# Write a program that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

fhand = open("words.txt", encoding="utf-8")
word_dictionary = dict()

for line in fhand:
    words = line.split()
    for word in words:
        word_dictionary[word] = word_dictionary.get(word, 0) + 1


if "everyone" in word_dictionary:
    print("True")
else:
    print("False")

print(word_dictionary)


