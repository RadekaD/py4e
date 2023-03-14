# Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

num_list = list()

while True:
    user_input = input("Please enter a number: ")

    if user_input == "done": break

    try:
        num = float(user_input)
        num_list.append(num)
    except:
        print("Invalid input. Please enter a number")
    
    

print("The largest number is:", max(num_list))
print("The smallest number is:", min(num_list))
print("All the numbers in this list are:", num_list)