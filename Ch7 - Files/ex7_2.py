#  Write a program to prompt for a file name, and then read through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475

# When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.

# Test your file on the mbox.txt and mbox-short.txt files.

fhand = open("mbox-short.txt", encoding="utf-8")
count = 0
total = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence: "):
       count = count + 1
       colpos = line.find(":")
       number = line[colpos + 1:].strip()
       SPAM_C = float(number)
       total = total + SPAM_C

average = total / count
print("The average SPAM confidence is ", SPAM_C)





    

