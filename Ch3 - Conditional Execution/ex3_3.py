# Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

user_input = input("How many points did you score on the test?")

try:
    score = float(user_input)
except:
    score = -1



if score < 0.0 or score > 1.0:
    print("Whoops! Please write a value between 0 and 1")
elif score >= 0.9:
    print("You got an A!")
elif score >= 0.8:
    print("You got a B!")
elif score >= 0.7:
    print("You got a C!")
elif score >= 0.6:
    print("You got a D!")
elif score < 0.6:
    print("You got an F!")