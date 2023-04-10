def main():
    plate = input("Plate: ")
    if not is_number(plate) and is_valid(plate) and the_length(plate):
        print("Valid")
    elif is_number(plate) and is_valid(plate) and the_length(plate) and numbers(plate) and zero_begin(plate):
        print("Valid")
    else:
        print("Invalid")

def is_number(s):
    for i in s:
        if i.isdigit():
            return True

def is_valid(s):
    if s[0:2].isalpha() and s.isupper():
        return True

def the_length(s):
    if 2<= len(s) <= 6 and s.isalnum():
        return True

def numbers(s):
    if s[2:].isdigit() or s[3:].isdigit() or s[4:].isdigit() and s[-1].isdigit():
        return True
def zero_begin(s):
    new = ''
    for i in s:
        if i.isdigit():
            new+=i
    if new[0]!= '0':
        return True


main()
