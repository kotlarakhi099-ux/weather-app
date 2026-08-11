import random
secret=random.randint(1,10)
guess=int(input("enter a number between 1-10:"))
if guess==secret:
    print("you guessed correctly")
else:
    print("try again")