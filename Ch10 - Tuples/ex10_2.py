# This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

fname = input("Enter a file name: ")
fhand = open(fname)

hour_d = dict()

for line in fhand:
    words = line.split()
    if line.startswith("From "):
        time = words[5]
        hour = time.split(":")
        hour = hour[0]
        hour_d[hour] = hour_d.get(hour, 0) + 1

# print(hour_d)

tmp = list()
for k,v in hour_d.items():
    newt = (k, v)
    tmp.append(newt)

tmp = sorted(tmp)

for k, v in tmp:
    print(k, v)