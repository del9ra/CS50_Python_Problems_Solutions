text = input("Enter greeting: ").lower().strip()

if text.startswith("hello"):
    print("$0")
elif text.startswith("h"):
    print("$20")
else:
    print("$100")
