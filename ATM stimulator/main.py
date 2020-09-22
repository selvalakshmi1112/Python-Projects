user = {1100: "USER-1", 2200: "USER-2", 3300: "USER-3"}
amount = {1100: 5000, 2200: 4000, 3300: 3000}


def display():
    print("WELCOME TO SBI ATM\n")
    print("1. BALANACE ENQUIRY\n")
    print("2. KEY UPDATE\n")
    print("3. WITHDRAWL\n")
    print("4. CASH DEPOSIT\n")


def balance():
    print("BALANCE-ENQUIRY\n")
    k = int(input("Enter the PIN\n"))
    print("Welcome\t")
    print(user[k])
    print("REMAINING-BALANCE\n")
    print(amount[k])
    print("Thanks for using SBI ATM")
    print("\n")
    display()
    choice()


def keyupdate():
    print("KEY-UPDATION\n")
    k = int(input("Enter the PIN\n"))
    print("Welcome\n")
    print(user[k])
    user.pop(k)
    print("Enter the New PIN\n")
    k1 = int(input())
    k2 = input("Enter the NEW Name\n")
    user[k1] = k2
    print(user)
    print("Your Key Is Updated\n")
    print("Thanks for Using SBI ATM\n")
    print("\n")
    display()
    choice()


def widthdrawl():
    print("WITHDRAWL\n")
    k = int(input("Enter the PIN\n"))
    print("Welcome\n")
    print(user[k])
    amt = int(input("Enter the Amount\n"))
    print("Remaining Balance\n")
    print(amount[k] - amt)
    print("Thanks for using SBI ATM\n")
    print("\n")
    display()
    choice()


def add_cash():
    print("Balance ADD\n")
    k = int(input("ENTER THE PIN\n"))
    print("Welcome\n")
    print(user[k])
    amt = int(input("Enter the Amount to Add\n"))
    print(amt, "This Amount is Added\n")
    print("New Balance\n")
    print(amount[k] + amt)
    print("Thanks for Using SBI ATM\n")
    display()
    choice()


def incorrect():
    print("Enter The Correct Choice\n")


def choice():
    j = int(input("PRESS THE KEY\n"))
    if (j == 1):
        balance()
    elif (j == 2):
        keyupdate()
    elif (j == 3):
        widthdrawl()
    elif (j == 4):
        add_cash()
    else:
        incorrect()
        choice()


print("\n")
display()
print("\n")
choice()