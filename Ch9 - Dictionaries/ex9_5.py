# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

fname = input("Enter file name: ")
host_list = dict()

try:
    fhand = open(fname)
except:
    print("Error, file doesn't exist", fname)
    quit()

for line in fhand:
    if line.startswith("From "):
        words = line.split()
        at_split = words[1].split("@")
        host = at_split[1]
        host_list[host] = host_list.get(host, 0) + 1


print(host_list)