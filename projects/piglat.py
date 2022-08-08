VOWELS = ['a', 'e', 'i', 'o', 'u']

print("Enter the English message to translate into Pig LatinL:")
message = input()

pigLatin = [] # translated message as a list

for word in message.split():
    # separate the non-letters at the start of this word
    prefixNonLetters = ''
    # while len(word) > 0:
