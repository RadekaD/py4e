# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).



    


def computepay(hours, rate):
    try:
        hours = float(hours)
    except:
        print("Please enter a numeric value")
        quit()
    
    try:
        rate = float(rate)
    except:
       print("Please enter a numeric value!")
       quit() 
    if hours > 40:
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        overtime_pay = 40.0 * rate + overtime_hours * overtime_rate
        print(overtime_pay)
    else:
        pay = hours * rate
        print(pay)


print(computepay(35, "gobledygook"))
print(computepay(48,10))
