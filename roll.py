import random

def dice_roll(how_many):

    first = random.randint(1,6)
    second = random.randint(1,6)
    third = random.randint(1,6)

    if how_many == 1:
        print("You rolled a", first)
    elif how_many == 2:
        print("First roll:", first, "Second roll:", second)
    elif how_many == 3:
        print("First roll:", first, "Second roll:", second, "Third roll:", third)


initial_roll = random.randint(1,6)

print("The first roll was a", initial_roll)

roll_again = input("Would you like to roll again? y/n")

while roll_again == "y":
    number = input("How many dice would you like to roll?")
    dice_roll(int(number))
    roll_again = input("Would you like to roll again? y/n")




