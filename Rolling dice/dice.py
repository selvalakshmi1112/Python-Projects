import random

roll = "1"

while (roll == "1" or roll == "yes"):
    print("Dices is Rolling..")
    print("The value is")
    print(random.randint(1, 6))
    roll = input("Do you want to Roll Again(yes/no)?")

print("Thank you!! Enjoy playing again")
