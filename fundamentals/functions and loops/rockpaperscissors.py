import random, sys

print('ROCK...PAPER...SCISSORS')

# win and loss variables

win = 0
loss = 0
tie = 0

while True: # main loop for the game
    print('%s Wins, %s Losses, %s Ties' % (win,loss,tie))

    while True: # player input loop
        print('Enter your move: (r)ock  (p)aper  (s)cissors or (q)uit')
        playermove = input()

        if playermove == 'q':
            sys.exit() # end the program
        elif playermove == 'r' or 'p' or 's':
            break # leave the player input loop
        print('Type either: r, p or s') # instructs player to input correct character

    # display player move
    if playermove == 'r':
        print('ROCK versus...', end='')
    elif playermove == 'p':
        print('PAPER versus...', end='')
    else:
        print('SCISSORS versus...', end='')

    # display computers choice
    randomNum = random.randint(1,3)

    if randomNum == 1:
        computerMove = 'r'
        print('ROCK')

    elif randomNum == 2:
        computerMove = 'p'
        print('PAPER')
    else:
        computerMove = 's'
        print('SCISSORS')

    # decide winner and record the w/l/t ties ratio

    if playermove == computerMove:
        print('Its a tie!')
        tie = tie + 1
    elif playermove == 'r' and computerMove == 'p':
        print('Computer wins.')
        loss = loss + 1
    elif playermove == 'r' and computerMove == 's':
        print('Player wins.')
        win = win + 1
    
    elif playermove == 'p' and computerMove == 's' :
        print('Computer wins.')
        loss = loss + 1
    elif playermove == 'p' and computerMove == 'r' :
        print('Player wins.')
        win = win + 1
    
    elif playermove == 's' and computerMove == 'r':
        print('Computer wins.')
        loss = loss + 1
    elif playermove == 's' and computerMove == 'p' :
        print('Player wins.')
        win = win + 1
    
    # computer will then re-run loop and print the wins and losses.