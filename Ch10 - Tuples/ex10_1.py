# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.

fname = input("Enter file name: ")
fhand = open(fname)
email_dict = dict()

for line in fhand:
    words = line.split()
    if line.startswith("From "):
            address = words[1]
            email_dict[address] = email_dict.get(address, 0) + 1
            


tmp = list()
for k,v in email_dict.items():
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

largest = tmp[0]
largest_name = largest[1]
largest_number = largest[0]
print(f"The person who made the most commits is {largest_name}, he made {largest_number} commits!")