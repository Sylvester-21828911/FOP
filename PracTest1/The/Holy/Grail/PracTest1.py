###
# PracTest1.py: Read name & age and print an ASCII birthday cake
#
# Student name: Sylvester Adhitama
# Student ID: 21828911
##

from datetime import datetime

myname = "Sylvester"
myyear = 1996
currentyear = int(datetime.today().strftime('%Y'))

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
if age % 2 == 1:          #add space for odd years
    print(end=" ")
for i in range(age//2):     #print first line of candles
    print("*", end=" ")
print("")
if age % 2 != 0:            #add space in the end for odd years
    print(end=" ")
for i in range(age//2):     #print second line of candles
    print("*",end="|")
print("")
for i in range(age//2):     #second line of candle sticks
    print(end="| ")
print("")
for i in range(age):
    print(end="#")


print()
