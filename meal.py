def main():
    numbers = input("What time is it? ")
    t = convert(numbers)
    if 7.0<=t<=8.0:
        print("breakfast time")
    elif 12.0<=t<=13.0:
        print("lunch time")
    elif 18.0<=t<=19.0:
        print("dinner time")



def convert(time):
    x, y = time.split(":")
    x, y = float(x), float(y)
    return x+y/60




if __name__ == "__main__":
    main()
