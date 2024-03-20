import os



BLACK = '\033[30m'  #colour vars
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
BOLD = '\033[1m'
RESET = '\033[0m'

treats = [['#','Name','Price','Count'],
        ['1','Choco Pie', '$1.00',5],
        ['2','Hello Panda','$0.50',10],
        ['3','Fortune Cookie','$0.30',10],
        ['4','Fig Roll','$0.30',10],
        ['5','Maliban Orange Cream','$0.30',10],
        ['6','Maliban Custard Cream','$0.30',10],
        ['7','Maliban Chocolate Cream','$0.30',10],
        ['8','Eccles Cake','$0.80',5],
        ['9','Wagon Wheel','$1.50',1]]

print(BOLD, "Welcome to the snack vending machine!", RESET,
        "\n\n\nThe slots are loaded with delicious treats!")
line = YELLOW+"+"+"-"*49+"+"+RESET

error = RED+"Please enter a valid selection."+RESET
while True:
    print(end=BOLD)
    choice = input("Would you like a treat? (Y/N)... ").upper()
    print(end=RESET)
    if choice == 'N':
        print(GREEN+"Glad to be of service!")
        break
    if choice == 'Y':
        print("Which treat would you like?\n"+ line)
        for i  in range(len(treats)):
            if i == 1:
                print(line)
            print(YELLOW+"|", str(treats[i][0]).rjust(2," "), "|", str(treats[i][1]).ljust(26," "), "|", treats[i][2], "|",
                    str(treats[i][3]).rjust(5," "), "|")
        print(line)
        try:
            selection = int(input("Enter your selection: "))
        except (IndexError, ValueError):
            print(error)
            continue
        if selection <= 0:
            print(error)
            continue
        print("That will be :", treats[selection][2])
        if treats[selection][3] == 0:
            print(RED, "Oh dear! We are all out of", treats[selection][1], RESET)
        else:
            stock = treats[selection][3] - 1
            treats[selection].pop(3)
            treats[selection].insert(3, stock)
            print(GREEN, "Enjoy your treat!",RESET)

