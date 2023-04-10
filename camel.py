s = input("camelCase: ")
new_text = ''
for i in s:
    if i.islower():
        new_text += i
    else:
        new_text += '_' + i
print("snake_case:", new_text.lower())
