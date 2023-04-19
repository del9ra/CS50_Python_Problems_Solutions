import random

def main():
    i = 0
    k = 0
    z = get_level()
    counter = 0
    while i<10:
        i+=1
        x, y = generate_integer(z)
        sum = x+y
        print(f"{x} + {y} = ", end="")
        user = int(input(""))
        if user != sum:
            print("EEE")
            while counter<2:
                try:
                    print(f"{x} + {y} = ", end="")
                    user = int(input(""))
                    if user==sum:
                        break
                    elif user!=sum:
                        print("EEE")
                except ValueError:
                    print("EEE")
                counter+=1
            if user != sum:
                print(f"{x} + {y} = {sum}")
                counter = 0

        elif user==sum:
            k+=1
    print(f"Score: {k}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level==1 or level==2 or level==3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        x = random.randrange(10)
        y = random.randrange(10)
        return x, y

    elif level == 2:
        x = random.randrange(10,100)
        y = random.randrange(10,100)
        return x, y

    elif level == 3:
        x = random.randrange(100, 1000)
        y = random.randrange(100, 1000)
        return x, y

if __name__ == "__main__":
    main()
