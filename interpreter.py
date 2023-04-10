x, y, z = input("Enter: ").split(" ")
x, z = float(x), float(z)
match y:
    case "+":
        print(x+z)
    case "-":
        print(x-z)
    case "/":
        print(x/z)
    case "*":
        print(x*z)
