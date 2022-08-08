path = 'C:\\Users\\AST96885\\OneDrive - Mott MacDonald\\Documents\\programming\\holybible.txt'

with open(path, encoding='utf-8') as bible:
    contents = bible.read()
    
    count = {}
    for char in contents:
        count.setdefault(char, 0)
        count[char] = count[char] + 1
    
print(count)
print(contents)