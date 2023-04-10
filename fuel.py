while True:
    try:
        x, y = input("Fraction: ").split("/")
        x, y = int(x), int(y)
        fuel = 0
        if (x>y):
            continue
        else:
            fuel = round(x/y*100)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
if fuel<=1:
    print("E")
elif fuel>=99:
    print("F")
else:
    print(f'{fuel}%')
