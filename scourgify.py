import sys
import csv
if len(sys.argv) < 3:
   sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
   try:
      love={}
      with open(sys.argv[1], "r") as file:
         reader = csv.DictReader(file)
         with open(sys.argv[2], "w") as new_file:
            writer = csv.DictWriter(new_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
               x, y = row["name"].split(", ")
               love = {"last":x, "first":y, "house":row["house"]}
               writer.writerow(love)
   except FileNotFoundError:
      sys.exit(f"Could not read {sys.argv[1]}")
else:
   sys.exit("Too many command-line arguments")
