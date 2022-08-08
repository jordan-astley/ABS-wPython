# guess the number game

import random as ran

name = input('Hello what is your name?:  ')
x = int(1)
y = int(20)
secretNumber = ran.randint(x,y)

print('Well ' + name + 
' I am thinking of a number between ' + str(x) + ' and ' + str(y))

for guessesTaken in range(1,7): # you get 6 guesses
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Too low!')
    elif guess > secretNumber:
        print('Too high!')
    else:
        break
    # leave for loop, correct number found
    # or ran out of guesses

if guess == secretNumber:
    print('Congratulations ' + name + ' you guessed '+
    'the correct number in ' + str(guessesTaken) + ' guesses')
else:
    print('No wrong again...I was thinking of ' + secretNumber)



