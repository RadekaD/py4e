# Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

fname = input("Enter file name: ")
fhand = open(fname)
email_list = dict()
biggest_sender = ""
message_count = 0

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        email_list[email] = email_list.get(email, 0) + 1

        
for address in email_list:
    if email_list[email] > message_count:
        message_count = email_list[email]
        biggest_sender = address



print(f"The person who sent the most emails is {biggest_sender} - he sent {message_count} emails!")

