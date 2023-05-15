import inflect
from datetime import date
import sys

class Season:
    def __init__(self, minutes):
        self.minutes = minutes

    def __sub__(self, other):
        return Season(self.minutes - other.minutes)

def main():
    print(count(input("Date of Birth: ")))


def count(date_string ):
    p = inflect.engine()
    # date_format = "%Y-%m-%d"   # how to check if format is right
    # x = datetime.strptime(date_string, date_format) #checks the format according date_format
    try:
        t = date.fromisoformat(date_string)
        a = Season(date.today())
        b = Season(t)
        c = a - b
        total = c.minutes.days * 24 * 60
        words = p.number_to_words(total, andword="")
        return f"{words.capitalize()} minutes"
    except ValueError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()