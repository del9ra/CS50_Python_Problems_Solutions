import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"<iframe (?:width=\"[0-9][0-9][0-9]\" height=\"[0-9][0-9][0-9]\" )?src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"", s, re.IGNORECASE):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
