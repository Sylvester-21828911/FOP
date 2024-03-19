import os

print("Welcome to the snack vending machine!\n\n\nThe slots are loaded with delicious treats!")
num = ['#',1,2,3,4,5,6,7,8,9]
name = ['Name','Choco Pie','Hello Panda','Fortune Cookie','Fig Roll','Maliban Orange Cream',
        'Maliban Custard Cream','Maliban Chocolate Cream','Eccles Cake','Wagon Wheel']

price = ['Price','$1.00','$0.50','$0.30','$0.30','$0.30','$0.30','$0.30','$0.30','$0.80','$1.50']

count = ['Count',5,10,10,10,10,10,10,5,1]



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

line = "+"+"-"*49+"+"

error = "Please enter a valid selection."
while True:
    choice = input("Would you like a treat? (Y/N)... ").upper()
    if choice == 'N':
        print("Glad to be of service!")
        break
    if choice == 'Y':
        print("Which treat would you like?\n"+ line)
        for i  in range(len(name)):
            if i == 1:
                print(line)
            print("|", str(treats[i][0]).rjust(2," "), "|", str(treats[i][1]).ljust(26," "), "|", treats[i][2], "|",
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
            print("Oh dear! We are all out of", treats[selection][1])
        else:
            stock = treats[selection][3] - 1
            treats[selection].pop(3)
            treats[selection].insert(3, stock)
            print("Enjoy your treat!")

