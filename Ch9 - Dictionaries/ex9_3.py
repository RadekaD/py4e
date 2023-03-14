# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

fname = input("Enter file name: ")
fhand = open(fname)
email_list = dict()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        email_list[email] = email_list.get(email, 0) + 1


print(email_list)
