import time, sys

def mainloop():

    indent = 0 #spaces to indent, creating the zigzag
    indent_increase = True #indentation increasing or not

    try: # allowing exit for the main program with keyboard interrupt
        # handles exit cleanly
        while True:
            print(' ' * indent, end='') # print amount of spaces according to indent
            # no newline, end=''
            print('********') # the zig / zag
            time.sleep(0.01)

            if indent_increase == True:
                indent = indent + 1
                if indent == 20:
                    indent_increase = False
                    # reverse direction after 20 lines
            else:
                indent = indent - 1
                if indent == 0:
                    indent_increase = True
                    # reverse direction again
    except KeyboardInterrupt:
        sys.exit()

mainloop()







