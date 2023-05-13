import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([1-9]|[1-1][0-2]):?([0-5]\d)? (AM|PM) to ([1-9]|[1-1][0-2]):?([0-5]\d)? (AM|PM)$",
                            s):
        a = int(matches.group(1))
        b = matches.group(2)
        c = matches.group(3)
        d = int(matches.group(4))
        e = matches.group(5)
        f = matches.group(6)
        if b is None:
            b = 0
            e = 0
            # тип None-type is None 2- None 3 - AM, а если нет - is not None
        if c == "AM":
            if a == 12:
                a = 0
        elif c == "PM":
            if a == 12:
                a = 0
            a = a + 12
        if f == "AM":
            if d == 12:
                d = 0
        elif f == "PM":
            if d == 12:
                d = 0
            d = d + 12
        return f"{a:02}:{int(b):02} to {d:02}:{int(e):02}"

    else:
        raise ValueError("ValueError")


if __name__ == "__main__":
    main()