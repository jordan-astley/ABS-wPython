#try, except example
def div42by(val):
    try:
        return 42 / val
    except ZeroDivisionError:
        print('Error you tried to divide by 0')

print(div42by(7))
