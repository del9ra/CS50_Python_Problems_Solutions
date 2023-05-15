import inflect
from datetime import date
import sys


def main():
    print(count(input("Date of Birth: ")))


def count(date_string ):
    p = inflect.engine()
    # date_format = "%Y-%m-%d"   # how to check if format is right
    # x = datetime.strptime(date_string, date_format) #checks the format according date_format
    try:
        t = date.fromisoformat(date_string)  # Returns a date object from the string representation of the date
        today = date.today()
        sub = today - t
        h = sub.days * 24 * 60
        words = p.number_to_words(h, andword="")
        return f"{words.capitalize()} minutes"
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()