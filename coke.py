i = 50
full_sum = 0

while i > 0:
    print("Amount Due:", i)
    bucks = int(input("Insert Coin: "))
    if bucks == 25 or bucks == 10 or bucks ==  5:
        i -= bucks
        full_sum += bucks
print("Change Owed:", full_sum-50)
