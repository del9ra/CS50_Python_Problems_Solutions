from validator_collection import validators, checkers, errors

s = input("What's your email address? ").strip()

try:
    email_address = validators.email(s, allow_empty = False)
    if email_address:
        print("Valid")
except errors.EmptyValueError:
    print("Invalid")
except errors.InvalidEmailError:
    print("Invalid")
