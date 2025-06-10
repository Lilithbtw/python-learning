import random

def read_dice():
    dice1 = None
    while True:

        accept_dice = input("Roll the dice? (y/n): ")

        if accept_dice == "y" or accept_dice == "Y":
            num_dice =int(input("How many rolls: "))
            times = int(input("How many times: "))
            dice_sides= int(input("How many sides: "))

            for i in range(times):
                for j in range(num_dice):
                    roll = random.randint(1, dice_sides)
                    print(f"Roll {j+1}: ({roll})")

        elif accept_dice == "n" or accept_dice == "N":
            if roll is not None:
                print("Thanks for playing!")
                exit(0)
            exit(0)

        else:
            print("Invalid choice!")

read_dice()