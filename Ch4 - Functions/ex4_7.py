# Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.




def computegrade(score):
    try:
        score = float(score)
    except:
        score = -1
        quit()

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

computegrade(0.83)