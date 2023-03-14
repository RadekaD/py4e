# Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


def check_for_float(input1, exit = True):
    try:
        val = float(input1)
        return val
    except:
        print("Invalid input")
        if exit:    
            quit()
        return False

count = 0
total = 0.0
average = 0.0

while True:
    input_number = input("Enter a number: ")
    if input_number == "done":
        break

    num = check_for_float(input_number, False)
    if not num:
        continue    

    count += 1
    total = total + num

if count:
    average = total / count

print(total, count, average)