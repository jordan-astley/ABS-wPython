# references - how arguments get passed in functions

def eggs(someParameter):
    someParameter.append('eggs!')

spam = [1,2,3]
print(spam)
eggs(spam)

print(spam)

