#
# strings1.py: Read in a string and print it in reverse
#              using a loop and a method call

instring = input('Enter a string... ')

# *** add (2) upper and (3) duplicating code here
# print uppercase
print('Uppercase string is : ', instring.upper())

# print duplicate string
print ('Duplicate string is: ', instring, instring)

# print forward with a while loop
print('Forward string is : ', end='')
index = 0
while index < len(instring):
    print(instring[index], end='')
    index = index + 1
print()

# print forward with a for-range loop
print('Forward string is : ', end='')
for index in range(0 , len(instring), +1):
    print(instring[index], end='')
print()

# print forward with slicing
print('Forward string is :', instring[::1])

# print every second letter
print('\nNow printing every second letter only')

# print forward with a while loop
print('Forward string is : ', end='')
index = 0
while index < len(instring):
    print(instring[index], end='')
    index = index + 2
print()

# print forward with a for-range loop
print('Forward string is : ', end='')
for index in range(0 , len(instring), +2):
    print(instring[index], end='')
print()

# print forward with slicing
print('Forward string is :', instring[::2])

# print every second letter, excluding the first and the last
print('\nNow printing every second letter, excluding the first and the last')

# print forward with a while loop
print('Forward string is : ', end='')
index = 1
while index < len(instring)-2:
    print(instring[index], end='')
    index = index + 2
print()

# print forward with a for-range loop
print('Forward string is : ', end='')
for index in range(1 , len(instring)-2, +2):
    print(instring[index], end='')
print()

# print forward with slicing
print('Forward string is :', instring[1:len(instring)-2:2])
