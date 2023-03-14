# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

hours_user_input = input("How many hours do you work per week?")

try:
    hours = float(hours_user_input)
except:
    print("Whoops! Please enter a numeric value!")
    quit()

rate_user_input = input("What is your hourly rate?")

try:
    rate = float(rate_user_input)
except:
    print("Whoops! Please enter a numeric value!")
    quit()


 
if hours > 40:
    overtime_hours = hours - 40
    overtime_rate = rate * 1.5
    overtime_pay = 40.0 * rate + overtime_hours * overtime_rate
    print(overtime_pay)
else:
    pay = hours * rate
    print(pay)
 