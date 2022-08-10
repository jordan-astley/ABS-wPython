# The Collatz Sequence
import time

steps = 0

def collatz(input):
    if (input % 2) == 0: # check remainder when divided by 2
        input = input // 2 # remainder 0 then even
    else:
        input = (3*input) + 1

    return input

def step_count(start,increment):
    global steps
    if start == True:
        steps = 0
    elif increment == True:
        steps = steps + 1

def mainloop():
    step_count(True,False)
    try:          
        number = int(input('Please enter an integer number:'))
        # expect an integer input
        
        while number != 1:
            number = collatz(number)
            print(number)
            step_count(False,True)
            time.sleep(0.01)

        if number == 1:
            print('Done in...' + str(steps) + ' steps.')
            mainloop()

    except:
        print('That\'s not a valid number')
        mainloop()

mainloop()
