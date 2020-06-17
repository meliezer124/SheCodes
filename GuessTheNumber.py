import random
def guess_the_number():
    comp_number = random.randint(0,100)
    print("The computer has selected a random number between 0 and 100. Now it's your turn.")

    user_guess= input("What will your guess be? ")
    correct = False

    while correct == False:
        if user_guess == comp_number:
            print("You've won! How did you know, you lucky bastard?")
            correct = True
        else:
            print("Wrong! Sucker! Try again!")
            user_guess= input("What will your guess be this time? ")


guess_the_number()
