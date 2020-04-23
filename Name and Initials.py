from datetime import datetime

def user_info():
    now = datetime.now()
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    birth_year = input("What year  were you born?")

    initials = first_name[0] + last_name[0]
    age = now.year - int(birth_year)

    print("Your initials are {init} and you are {yrsold} years old.".format(init = initials, yrsold = str(age))) 

user_info()
