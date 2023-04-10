def convert(emoji):
    if ":)" in emoji:
        emoji = emoji.replace(":)", "🙂")
    if ":(" in emoji:
        emoji = emoji.replace(":(", "🙁")
    return emoji

def main():
    text=input("Enter text: ")
    h = convert(text)
    print(h)
main()
