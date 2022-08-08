# coin flip streaks
# how often does a streak of six heads or six tails come up
# in a randomly generated list of heads and tails.

# first part generates a list of randomly selected heads or tails

# second part checks if there is a streak of six in a row in it

# this code is to loop 10,000 times to run the experiment

import random

values = []

def generate_vals():
    global values
    flips = 100
    for i in range(flips):
        values.append(random.randint(0,1))

number_of_streaks = 0

def check6streak():
    streak = 0
    global number_of_streaks

    for i in range(len(values)):
        if values[i] == values[i-1]:
            streak += 1
            if streak == 5:
                number_of_streaks += 1
                streak = 0 # reset the counter
        else:
            streak = 0

RUNS = 1000

for _ in range(RUNS): # _ satisfy synatically
    generate_vals()
    check6streak()
print(number_of_streaks)
print('Chance of a Streak: %.4f %%' % ((number_of_streaks / RUNS)*100))
    
# %.4f gives four digitals afte the decimal point always
# %% is to give one % since its used for format specifier as well
# only /100  --- (1/10000)*100 = 1/100)
# generate_vals()
# check6streak()

