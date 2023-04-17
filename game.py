import random
while True:
    try:
        n = int(input("Level: "))
        if n>0:
            r = random.randint(1, n)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess > 0:
                        if guess < r:
                            print("Too small!")
                        elif guess > r:
                            print("Too large!")
                        else:
                            print("Just right!")
                            break
                except ValueError:
                    pass
            break
    except ValueError:
        pass
