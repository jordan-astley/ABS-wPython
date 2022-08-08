'''
https://codereview.stackexchange.com/questions/247936/coin-flip-streaks-correct-streak-condition
'''
import random

def coin_toss():
    outcome = random.randint(0,1)
    return outcome

def check6streak(coin_tosses_data):
    previous_coin_face = None
    streak_length = 0
    number_of_streaks = 0 # streaks for 1 run

    for coin_face in coin_tosses_data:
        if coin_face == previous_coin_face:
            streak_length += 1
        else:
            previous_coin_face = coin_face
            streak_length = 1
        
        if streak_length == 6:
            number_of_streaks += 1

    return number_of_streaks
            

def coin_toss_experiment(RUNS):
    # RUNS = e.g. 10000 experiment runs
    FLIPS = 100 # coin flips
    total_streaks = 0 # total of streaks for no of runs

    for _ in range(RUNS):
        outcome_data = [] # list to hold H or T data
        
        for _ in range(FLIPS):
            outcome_data.append(coin_toss()) # populate outcome data
        print(check6streak(outcome_data))
        total_streaks += check6streak(outcome_data)

    print('number of streaks: %d found in %d attempts' % (total_streaks,RUNS))
    print('Chance of 6 streak per 100 flips: %d %%' % (100*(total_streaks/RUNS)))

coin_toss_experiment(100)



        
