with_vowel = input("Enter: ")

for i in with_vowel:
    match i:
        case 'a' | 'e' | 'i' | 'o' | 'u' | 'A' | 'E' | 'I' | 'O' | 'U':
            continue
        case _:
            print(i, end="") 
