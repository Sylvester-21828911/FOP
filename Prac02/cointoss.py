#
# cointoss.py - simulate tossing a coin multiple times
#
import random
coin = ['heads','tails']
heads = 0
tails = 0
trials = 0
print('\nCOIN TOSS\n')

while True:
    try:
        trials = int(input("Flip a coin! How many flips would you like? "))
    except (ValueError, TypeError):
        pass
    if trials > 0:
        break
    print("Please enter a positive number\n")
for index in range(trials):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')
