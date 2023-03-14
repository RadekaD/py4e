
import re


fhand = open("regex_sum_1375553.txt", encoding="utf-8")
sum = 0

for line in fhand:
    line.rstrip()
    num_list = re.findall("[0-9]+", line)
    for num in num_list:
        if num_list != []:
            sum = sum + int(num)




print(sum)        
    
    