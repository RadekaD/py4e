# Computing gross pay per week using users input

hours = input("How many hours per week do you work?")
rate = input("What is your rate per hour?")
pay = float(hours) * float(rate)

print("You earn " + str(pay) + " Serbian Dinars every week!")