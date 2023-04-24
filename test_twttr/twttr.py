def main():
    with_vowel = input("Enter: ")
    s = shorten(with_vowel)
    print(s)

def shorten(word):
    love = ""
    for i in word:
        match i.lower():
            case 'a' | 'e' | 'i' | 'o' | 'u':
                continue
            case _:
                 love+=i
    return love

if __name__ == "__main__":
    main()