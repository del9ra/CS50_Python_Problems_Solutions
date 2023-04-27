def main():
    s = input("Fraction: ")
    print(gauge(convert(s)))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError("Error 1")
        if x>y:
            raise ValueError("Error 2")
    except ValueError:
        raise ValueError("Error 2")
    fuel = int((x/y)*100)
    return fuel

def gauge(percentage):
    if percentage<=1:
        empty = "E"
        return empty
    elif percentage>=99:
        full = "F"
        return full
    else:
        Z = f'{percentage}%'
        return Z

if __name__ == "__main__":
    main()