dogNames = []

while True:
    name = input('Enter the name of the dog ' + str(len(dogNames)+1) +
    ' (Or enter nothing (enter) to stop.):')
    dogNames += [name]
    if name == '':
        break
    
print('The Dog names are: ')
for name in dogNames:
    print('     ' + name)
