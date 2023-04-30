import sys
import csv
from tabulate import tabulate

if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                general = []
                reader = csv.reader(file)
                for row in reader:
                    general.append(row)
                headers = general[0]
                table = general[1:]
                print(tabulate(table, headers, tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
