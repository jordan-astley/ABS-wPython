# coin flip streaks
# how often does a streak_length of six heads or six tails come up
# in a randomly generated list of heads and tails.

# first part generates a list of randomly selected heads or tails

# second part checks if there is a streak_length of six in a row in it

# this code is to loop 10,000 times to run the experiment

import random

coin_toss_vals = [] # stores outcomes of coin flips in a list

def coin_toss(flips): # flips usually 100
    for _ in range(flips):
        coin_toss_vals.append(random.choice(['H','T']))
        # populate the list with Heads or Tails

def check6streak():
    global coin_toss_vals
    pre_coin_face = None # previous coin face
    streak_length = 0
    number_of_streaks = 0

    for curr_coin_face in coin_toss_vals:
        
        if curr_coin_face == pre_coin_face:
            streak_length += 1 # inc streak count
        else:
            pre_coin_face = curr_coin_face
            streak_length = 1 # reset streak count, include current

        if streak_length == 6:
            streak_length = 0
            number_of_streaks += 1

    print(number_of_streaks)

    return number_of_streaks

def coin_toss_experiment(RUNS):
    global coin_toss_vals
    successes = 0 # stores total amount of coin flip streaks

    for _ in range(RUNS): # e.g. run 10000 times
        coin_toss_vals = [] # reset the 100 coin flip outcomes for each RUN
        coin_toss(100) # flip a coin 100 times, store in the list
        successes += check6streak()
    print('number of streaks: %d found in %d attempts' % (successes,RUNS))
    print(f'Chance of 6 streak per 100 flips: {(successes/RUNS)*100:.2f}%')

coin_toss_experiment(10000)







# RUNS = 1000

# for _ in range(RUNS): # _ satisfy synatically
#     generate_vals()
#     check6streak()
# print('Chance of a Streak: %.4f %%' % ((number_of_streaks / RUNS)*100)) 
# %.4f gives four digitals afte the decimal point always
# %% is to give one % since its used for format specifier as well
# only /100  --- (1/10000)*100 = 1/100)
