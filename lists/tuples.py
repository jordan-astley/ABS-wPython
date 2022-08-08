### Tuple data type ###

# near identical to lists

groceries = ('eggs', 'milk', 'flower', 42, 70, 23) # tuple

print(groceries[0])
print(len(groceries))

# tuples cannot have values modified, they are immutable

# groceries[1] = 'test' # error

example_string = ('hello')
print(type(example_string))

trailing_comma_tuple = ('hello',) # the comma makes this a tuple
print(type(trailing_comma_tuple))

## tuples convey that sequence of values will not change
# because of this they are faster to use

# converting types

shopping_list = list(groceries)
print(type(shopping_list))
# handy to get a mutable version of a tuple value

# integers are immutable

spam = 42
cheese = spam
print(spam)
spam = 100
print('spam = ' + str(spam))
print('cheese = ' + str(cheese)) 
# variables reference memory location of data, e.g. initally spam 
# references 42 but is changed to 100, a different value in memory
# cheese is a copied address of the reference to 42 in the memory
# but it is unchanged when spam is overwritten

# lists don't work in this way

some_numbers = [0,1,2,3,4,5,6,7,8,9]
some_integers = some_numbers
some_numbers[1] = 'not a number'
print(some_numbers)
print(some_integers)

# modifying lists objects -- modifying in-place, doesn't create a new
# value it alters the existing one

# the append, reverse etc methods modify lists in place

