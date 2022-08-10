greetings = ['hello', 'hi', 'howdy', 'hey', 'heyas']

print(greetings.index('howdy'))

greetings += 'hey'
print(greetings) # adds 'h', 'e', 'y'
# note cannot remove with -=

# multiple entries of same item in list, index returns 1st index of 1st
# time it finds that value

## append and insert
# can only be called on lists, not other types
# print(greetings.index('hey'))
# greetings.append('hey')
# print(greetings.index('hey'))

# print(greetings)
# greetings.append('hey') 
# print(greetings)

## greetings = greetings.append('hey')
## ^^this is wrong, append and insert return none value
greetings.insert(1, 'whatsup') # specifies where to add the item to list
print(greetings)

## remove
greetings.remove('hey') # first instance removed
print(greetings)

del greetings[-1] # removed final value
print(greetings)

numbers = [1, 5.5, 3.75, 4.14, 10.5, 2.6, 3.4, 1.7999]
numbers.sort()
print(numbers)
numbers.sort(reverse=True) # prints in reverse order
print(numbers)

# sorts the list in place
# new_var = numbers.sort(reverse=True) # this is wrong

# sort for for list of strings is in ASCIIbetical order, i.e. Z >> a
# avoid this with below for normal alphabetical order, treating all
# letters as lowercase

words = ['cat', 'bat', 'Dog', 'Bus', 'ciggy', 'water', 'Zigzag']
print(words)
words.reverse()
print(words)

words.sort()
print(words)

words.sort(key=str.lower)
print(words)

print('this is a very long string of text that can be ' + \
    'broken up on to mutliple lines using \ to make it more readable')
    
