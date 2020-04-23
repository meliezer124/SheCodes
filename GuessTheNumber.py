import random
def guess_the_number():
    comp_number = random.randint(0,100)
    print("The computer has selected a random number between 0 and 100. Now it's your turn.")

    user_guess= input("What will your guess be? ")

    if user_guess == comp_number:
        print("You've won! How did you know, you lucky bastard?")
    else:
        print("Wrong! Sucker! The number was {correct}".format(correct = comp_number))


guess_the_number()
