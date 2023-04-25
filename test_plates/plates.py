def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2<= len(s) <= 6 and s.isupper() and s.isalpha():
        return True
    elif 2<= len(s) <= 6 and s.isalnum():
        return alpha_upper(s)
    else:
        return False

def alpha_upper(n):
    if n[0:2].isalpha() and n.isupper():
        return isdigit(n)
    else:
        return False

def isdigit(o):
    if o[2:].isdigit() or o[3:].isdigit() or o[4:].isdigit() and o[-1].isdigit():
        return zero(o)
    else:
        return False

def zero(l):
    new = ''
    for i in l:
        if i.isdigit():
            new+=i
    if new[0]!= '0':
        return True
    else:
        return False

if __name__ == "__main__":
    main()