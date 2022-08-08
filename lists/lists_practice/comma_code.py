# function that takes list as argument
# returns string with all items separate by comma and space
# 'AND' inserted before last item

spam = ['apples', 'bananas', 'tofu', 'cats']    
test = [1,2,3,4]

zero = []

def commacode(input):
    for i in range(len(input)):
        if i == (len(input) - 1):
            print('and ' + str(input[i]) + '.')
        else:
            print(str(input[i]) + ', ', end='')

commacode(spam)
commacode(test)

commacode(zero)
