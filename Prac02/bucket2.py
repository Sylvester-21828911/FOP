#
# bucket2.py - bucket list builder
#
print('\nBUCKET LIST BUILDER\n')
bucket = []

def printItems():       # List bucket items
    if len(bucket) == 0:
        print('Bucket is empty!')
    index = 1
    for item in bucket:
        print(index,'. ', item)
        index += 1
        
while True:
    try:
        choice = input('Enter selection: e(X)it, (A)dd, (L)ist, or (D)elete: ').upper()

        if choice[0] == 'A':
            newitem = input('Enter list item... \n')
            bucket.append(newitem)

        elif choice[0] == 'L':
            printItems()

        elif choice[0] == 'D':
            printItems()
            if len(bucket) != 0:
                try:
                    num = int(input('Please enter the number of the entry you want to delete: '))
                    if len(bucket) >= num > 0:	# Check if input is valid entry
                        del bucket[num-1]
                        print ('Entry #', num, 'deleted.')
			# The line above is not a comment but I don't know how to escape the syntax highlighting
			# But it still work, so all is good?
                    else:
                        print('Invalid entry number')
                except ValueError:	# Empty input error
                    print('Please enter a number!')
                
        elif choice[0] == 'X':
            break

        else:
            print('Invalid selection.')

    except IndexError:      # Catch errors in case user did not put anything
        print('Please enter a selection.')

print('\nGOODBYE!\n')
