# Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

def check_for_float(input1, exit = True):
    try:
        val = float(input1)
        return val
    except:
        print("Invalid input")
        if exit:    
            quit()
        return False

input1 = input("Enter a number: ")
if input1 == "done":
    quit()

num = check_for_float(input1)

smallest = num
largest = num
count = 0
total = 0

while True:
    input1 = input("Enter a number: ")
    if input1 == "done":
        break

    num = check_for_float(input1)

    count = count + 1
    total = total + num

    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print ("Count: ", count, "Total: ", total, "Largest number: ", largest, "Smallest number: ", smallest)