def division(diviser):
    try:
        return 42/diviser
    except:
        print('Invalid input.')

import random

secretNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20')
i = 1

while i<7:
    num = int(input('Take a guess : '))
    if num < secretNum:
        print('Your guess is too low.')
    elif num > secretNum:
        print('Your guess is too high.')
    else:
        print('Good job! You guessed my number in ' + str(i) + ' attempts.')
        break
    i+=1
