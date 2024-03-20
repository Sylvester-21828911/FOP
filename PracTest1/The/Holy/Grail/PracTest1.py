###
# PracTest1.py: Read name & age and print an ASCII birthday cake
#
# Student name: Sylvester Adhitama
# Student ID: 21828911
##

myname = "Sylvester"
myyear = 1996
currentyear = 2024

print("Hello, my name is ", myname)
uname = input("What is your name?")
while True:
    try:
        uyear = int(input("What year were you born?"))
        if 1950 > uyear or uyear > currentyear:
            print("You can't be that old! Try again")
        else:
            break
    except ValueError:
        print("You haven't told me anything!")
age = currentyear - uyear
print("Birthday greetings,", uname,"the aged!")
print("Here's a cake with", age, "candles!")

print(end=" ")
for i in range(age//2):  
    print("*", end=" ")
print("")
if age % 2 != 0:
    print(end=" ")
for i in range(age//2):
    print("*",end="|")
print()
