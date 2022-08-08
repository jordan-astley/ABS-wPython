# list = mutable data type, can have values edited.
# strings = immutable cannot be edited
# reassigning single character in string == typeError

statement = 'Rover. doggo.'
#statement[7] = 'the'

print(statement)

## proper way to mutate the string
# slicing the old string - creating a new string
new_statement = statement[:7] + 'The ' + statement[7:]
print(new_statement)
    # [0:6] referring to the characters we don't wish to replace
    # string not modified

print(statement[:6]) # prints the first 5 characters


