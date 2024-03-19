#
# assorted.py - selecting random biscuits from a pack
#
import random
biscuits = []   #77665
biscuits.extend(['Monte Carlo']*1)
biscuits.extend(['Shortbread Cream']*1)
biscuits.extend(['Delta Cream']*1)
biscuits.extend(['Orange Slice']*1)
biscuits.extend(['Kingston']*1)
print('\nASSORTED CREAMS\n')
print('There are ', len(biscuits), ' biscuits in the pack.')
print('\n', biscuits, '\n')
more = input('\nWould you like a biscuit (Y/N)... ').upper()
while more != 'N' and biscuits:
    choice = random.randint(0,len(biscuits)-1)
    print('Your biscuit is : ', biscuits[choice])
    del biscuits[choice]
    more = input('\nWould you like a biscuit (Y/N)...')
print('\nThere are ', len(biscuits), ' biscuits left.')
print('\n', biscuits, '\n')
