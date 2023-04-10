food = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
sum = 0
while True:
    try:
        meal = input("Item: ").title()
        if meal in food:
            x = food.get(meal)
            sum += x
            print(f"Total: ${sum:.2f}")
    except (EOFError):
        print()
        break
