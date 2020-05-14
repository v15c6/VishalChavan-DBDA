input_Str = "PyNaTive"
low = []
up = []
for char in input_Str:
    if char.islower():
        low.append(char)
    else:
        up.append(char)
sortedString = ''.join(low + up)
print(" arranging characters giving precedence to lowercase letters:")
print(sortedString)
