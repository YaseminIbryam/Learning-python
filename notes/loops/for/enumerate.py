string = "wowdxq01"
for index, character in enumerate(string):
    print(f"{index} - {character}")
for i, c in enumerate(string):  #first variable is index
    print(i)
for i, c in enumerate(string):  #second variable is the character in the string
    print(c)
for i in enumerate(string):  #if there is only one variable when using enumerate it's both - index and character (index, 'character') 
    print(i)
