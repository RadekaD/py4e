# Try to guess a computers secret number!

import random


def guess(x):

    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number: "))
        
        if guess < random_number:
            print("Sorry, wrong guess. Too low!")
        elif guess > random_number:
            print("Sorry, wrong guess. Too high!")
    
    print("Correct, the secret number was", guess)



guess(100)


# The computer tries to guess your secret number!

# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ""
#     guess_num = 0
    
#     while feedback != "c":
#         guess_num = guess_num + 1
#         guess = random.randint(low, high)
#         feedback = input(f"Is {guess} too high (H), too low (L), or Correct (C)?").lower()
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             low = guess + 1

#     print(f"Yay! The number {guess} is correct!")
#     print(f"You guessed correctly after {guess_num} tries!")

# computer_guess(5000)


