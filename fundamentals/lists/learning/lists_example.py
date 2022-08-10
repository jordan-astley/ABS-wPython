spam = ['cat', 'bat', 'rat', 'elephant']

# slice, several values from a list

slice = spam[0:2]
print(slice)
print(spam[:])

nums = ['10', '20', '30']
nums[1] = 'test'
print(nums)

nums[0:3] = 'tests'
print(nums)


word = 'jordan'
listed_word = list(word)
print(listed_word)


print('jordan' in word)
print('j' in word)

print('jordan' in listed_word)
print('j' not in listed_word) # reverse if just: in operator
print('j' in listed_word) # evaluates to True

# demonstrating iterating over a list

office_supplies = ['pens', 'cordless drill', 'pencils', 'paper', 'flame-thrower', 'sharpener', 'ruler']
spam = ['spam','spam','spam','spam','spam','spam','spam','spam','spam']

for i in range(len(office_supplies)):
    print('Index ' + str(i) + ' in office supplies is: ' + office_supplies[i])

# for loops iterate over the values in a list
# range function returns a list like value, can be passed to list()
# which gives the actual list value

for s in range(len(spam)):
    print(spam[s] + ' ' + str(s))


# mutliple Assignment #

cat = ['fat', 'ginger', 'loud']

# # below variable assigment from list == convoluted
# size = cat[0]
# colour = cat[1]
# disposition = cat[2]

size, colour, disposition = cat # variables assigned to value of list entries
print(size,colour,disposition)

size, colour, disposition = 'skinny', 'black', 'quiet'
print(size,colour,disposition) # multiple variables and values,
# around assignment operator

a = 'AAA' # swap operation
b = 'BBB'
a, b = b, a #swap
print(a, b)

# augmented assigment operators
spammy  =  42
spammy += 1
print(spammy)

### enurmerate() function ###

# instead of range(len(somelist))
# on each iteration of loop, enumerate returns 2 values index and item

office_supplies = [
'pens', 'cordless drill',
'pencils', 'paper', 'flame-thrower',
 'sharpener', 'ruler'
    ]

### instead of this ###
# for i in range(len(office_sdddddddddddddupplies)):
#     print('Index ' + str(i) + ' in office supplies is: ' + office_supplies[i])

### use the enumerate function instead ###
for index, item in enumerate(office_supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

## random selection from lists ##

# You can consider random.choice(someList)
# to be a shorter form of someList[random.randint(0, len(someList) – 1].

import random

random.shuffle(office_supplies)
print(office_supplies)

ex1 = office_supplies[random.randint(0, len(office_supplies)-1)]
ex2 = random.choice(office_supplies)
print(ex1, ex2)


## augmented assignment ##

spam = 'spam, '
spam += 'spam'
print(spam)

meat = ['bacon']
meat *= 3
print(meat)

tree = ['oak']
tree = tree*3
print(tree)
