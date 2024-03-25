###
# PracTest1.py: Read name & age and print an ASCII birthday cake
#
# Student name: Sylvester Adhitama
# Student ID: 21828911
##

myname = "Sylvester"
myyear = 1996
maxyear = 2020

print("Hello, my name is ", myname)
uname = input("What is your name?")
while True:
    try:
        uyear = int(input("What year were you born?"))
        if 1930 > uyear or uyear > maxyear: #check if year is valid
            print("You can't be that old! Try again")
        else:
            break
    except ValueError:      #if user input nothing
        print("You haven't told me anything!")

age = maxyear - uyear       
print("Birthday greetings,", uname,"the aged!")
if uyear > myyear :         #check if younger or older than me
    print('Seems like you\'re younger than me!')
else:
    print('Seems like you\'re older than me!')
print("Here's a cake with", age, "candles!")

print(end=" ")
for i in range(age//2):     #print first line of candles
    print("*", end=" ")
print("")
for i in range(age//2):     #print second line of candles
    print("*",end="|")
print("")
for i in range(age//2):     #second line of candle sticks
    print(end="| ")
print("")

if age % 2 == 1:
    age = age -1

for g in range(5):          #cake base
    if g % 2 != 0:
        for i in range(age):
            print(end="#")
    else:
        for i in range(age):
            print(end='=')
    print()
print()
