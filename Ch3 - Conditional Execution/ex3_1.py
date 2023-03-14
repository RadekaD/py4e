#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours_user_input = input("How many hours do you work per week?")
hours = float(hours_user_input)
rate_user_input = input("What is your hourly rate?")
rate = float(rate_user_input)
pay = hours * rate


if hours > 40:
    overtime_hours = hours - 40
    overtime_rate = rate * 1.5
    overtime_pay = 40.0 * rate + overtime_hours * overtime_rate
    print(overtime_pay)
else:
    print(pay)
 
