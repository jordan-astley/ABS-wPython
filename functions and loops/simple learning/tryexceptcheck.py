#how many pets do you have

def howmanypets():

    numPets = input('How many pets do you have:  ')    
    
    try: # input validation
        if int(numPets) >= 4:
            print('That is a lot of pets!')
        elif int(numPets) < 0: # checks for negative values
            print('Enter a POSITIVE integer')
        else:
            print('That is not a lot of pets!')

    except ValueError:  # deals with users not entering type int
        print('You did not enter an integer!')

while True:
    howmanypets()
