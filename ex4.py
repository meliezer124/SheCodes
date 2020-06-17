#Loops ex4.1

def star_pyramid():
    height = 0
    while height < 1:
        height = int(input("Pick a height: "))
    for i in range(1, height + 1):
        print("*" * i)

def star_trapeze():
    height = 0
    base = "****"
    while height < 1:
        height = int(input("Pick a height: "))
    for i in range(1, height + 1):
        print(base + ("*" * i))

def bonus_star():
    height = 0
    while height < 1:
        height = int(input("Pick a height: "))
    for i in range(1, height + 1, 2):
        space = int((height - i)/2)
        print((" " * space) + ("*" * i))
    for i in range(height - 1, 0, -1):
        space = int((height - i) / 2)
        print((" " * space) + ("*" * i))

bonus_star()