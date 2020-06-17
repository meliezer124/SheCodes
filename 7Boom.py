def seven_boom():
    for i in range(1, 51):
        if i % 7 == 0:
            print("boom!")
        else:
            print(i)


def boom_check():
    for i in range(1, 21):
        response = input("Enter next one: ")
        boom = "boom"
        if i % 7 == 0 and response == boom:
            print("Okay!")
        elif i % 7 != 0 and int(response) == i:
            print("Okay!")
        else:
            print("Wrong! Game Over!")
            break


# boom_check()


def computer_boom():
    turn = False
    for i in range(1,51):
        #something that determines who's turn it is
        if turn == False:
            response = input("Enter next one: ")
            boom = "boom"
            if i % 7 == 0 and response == boom:
                print("Nice catch!")
            elif i % 7 != 0 and int(response) == i:
                print("Okay!")
            else:
                print("Wrong! Game Over!")
                break
            turn = True
        else:
            if i % 7 == 0:
                print("boom!")
            else:
                print(i)
            turn = False


computer_boom()