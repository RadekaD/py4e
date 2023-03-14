# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

# word = 'banana'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(str, letter):
    counter = 0
    for char in str:
        if char == letter:
            counter = counter + 1
    print(counter)



count("Heeeej, samo da mi je, hladne vode sa Romanije", "e")