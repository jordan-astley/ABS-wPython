'''
passing round references is a handy way to deal with lists
and dictionaries, if the function modifies the list/ dictionary passed
you may not want these changes in the original object value
'''

## copy module ##

# create a duplicate of a mutable value like a list

import copy

spam = ['a', 'b', 'c', 'd']

print(id(spam))

cheese = copy.copy(spam)
print(cheese)
print(id(cheese))

print(id(cheese) == id(spam)) # evaluates to false

cheese[3] = 'cheese'
print(cheese, spam)

## lists containing lists

silly_list = [[1,2,3,4],['carrot','peas','potatoe','cabbage'],[5,6,7,8]]

another_silly_list = copy.deepcopy(silly_list)

print(silly_list, another_silly_list)

veg = another_silly_list[1]
print(veg)

orange_veg = another_silly_list[1][0] # access an item in a list of lists
print(orange_veg)

firstEntry = [entry[0] for entry in another_silly_list]
print(firstEntry)

