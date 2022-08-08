spam = 'Hello world'
print(spam.upper())
print(spam) # spam will be the same, strings are immutable.

# to actually change spam
spam = spam.upper()
print(spam)

'hello'.isalpha() # true
'hello123'.isalpha() # false
'123'.isdecimal() # true
'hello123'.isdecimal() #false
'   '.isspace() # true

hello_world = 'hello world'
print(hello_world[5].isspace()) #true dat
titlecase = 'This Is Title Case'
print(titlecase.istitle()) # true
print(hello_world.startswith('hello'))

listofstrings = ['cats', 'rats', 'bats']
print(','.join(listofstrings))
print('   '.join(listofstrings))
print('\n\n'.join(listofstrings))

print(titlecase.split()) # splits on white space
print(titlecase.split('i')) # splits on 'i' lowercase only

## make strings longer
spam1= 'hello'
print(spam1.rjust(10,'*'))
print(spam1.ljust(10,'-'))
print(spam1.center(20,'-'))

spam1 = spam1.rjust(10,'&')
print(spam1)
print(spam1.strip('&')) # removes unwanted chars, if no args default to spaces
print(spam1.lstrip('&'))
print(spam1.rstrip('&')) #does nothing here
# none of these methods have altered spam

spam2 = 'hello there!'
print(spam2.replace('e', 'XYZ'))


