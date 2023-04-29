import sys

if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)==1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 2:
    if sys.argv[1].endswith(".py"):
        try:
            with open (sys.argv[1], "r") as file:
                count = 0
                for line in file:
                    if line.isspace():
                        continue
                    elif line.lstrip().startswith("#"):
                        continue
                    else:
                        count+=1
                print(count)
        except FileNotFoundError:
            print("File does not exist")
    else:
        sys.exit("Not a Python file")
