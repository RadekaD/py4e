

time = "11:43 AM"
added_time = "11:18"
count = 0

split_time = time.split()
num_time = split_time[0]

# Splits the start time string into hours, minutes, and AM or PM

am_or_pm = split_time[1]
num_time = num_time.split(":")
hour = int(num_time[0])
minutes = int(num_time[1])

# Splits the duration time into hours and minutes

added_time = added_time.split(":")
added_hour = int(added_time[0])
added_minutes = int(added_time[1])

# If the sum of minutes is over 60, add 1 hour and the rest of the minutes to start time

hour_sum = (hour + added_hour) % 12
minute_sum = minutes + added_minutes

if minute_sum >= 60:
    minute_sum = minute_sum - 60
    hour_sum += 1
    if minute_sum < 10:
        # Add a 0 if the number is single digit
        minute_sum = "0" + str(minute_sum)



# Computes the differences between AM and PM


if (hour_sum % 24) <= 11:
    am_or_pm = "AM"
else:
    am_or_pm = "PM"

# if am_or_pm == "AM":

#     if hour_sum >= 12:
#         hour_sum = hour_sum % 12
#         am_or_pm = "PM"

#         if hour_sum == 0:
#             hour_sum = 12
    




# elif am_or_pm == "PM":
#     if hour_sum >= 12:
#         hour_sum = hour_sum % 12
#         am_or_pm = "AM"


print(f"{hour_sum}:{minute_sum} {am_or_pm}")

