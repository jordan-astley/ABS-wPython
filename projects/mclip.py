#! python3
# mclip.py - A multi-clipboard program

TEXT = {"agree": """Yes, I agree. Lets proceed.""",
        "busy":  """Sorry, I am currently quite busy. Can we speak later this week?""",
        "notsure": """Apologies, I am not sure what you mean. Can I call you later?"""
        }

# command line arguments are stored in the variable sys.argv

import sys, pyperclip
# pyperclip requires install

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1].lower() # second element in argv, 1st command line arg

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for '{keyphrase}' copied to clipboard")
else:
    print(f"There is no text for '{keyphrase}'")
