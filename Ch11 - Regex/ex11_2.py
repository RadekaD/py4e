#  Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

import re

fname = input("Enter file name: ")
fhand = open(fname)
new_r_list = []

for line in fhand:
    line = line.rstrip()
    new_r = re.findall("^New Revision: ([0-9.]+)", line)
    if new_r != [] and not new_r:
        for val in new_r:
            val = float(val)
            new_r_list += [val]


# newr_sum = sum(new_r_list)
# count = float(len(new_r_list))
# newr_average = newr_sum / count

# print(newr_average)