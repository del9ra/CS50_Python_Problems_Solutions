import inflect
p = inflect.engine()
old_list = []
while True:
    try:
        s = input("Name: ")
        old_list.append(s)
        mylist = p.join((old_list))

    except EOFError:
        break
print(f"Adieu, adieu, to {mylist}")
