months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    ask_date = input("Date: ")
    try:
        # To split and create a list
        if "/" in ask_date:
            numeric = ask_date.split("/")
            month = int(numeric[0])
            day = int(numeric[1])
            year = int(numeric[2])
            if 1<=month<=12 and 1<=day<=31:
                break

        # to create a function for zero-padding
        elif "," in ask_date:
            alphabetical = ask_date.split()
            year = int(alphabetical[2])
            day = int(alphabetical[1].replace(",", ""))
            month = int(months.index(alphabetical[0]) + 1)
            if 1<=month<=12 and 1<=day<=31:
                break

    except (ValueError):
        pass
    except (NameError):
        pass

print(f"{year}-{month:02}-{day:02}")
