import random

answer = random.randint(1,9)
guess = int(input("Please enter your guess"))
if guess==answer:
    print("Your guess was right! The number is indeed", answer)
elif guess>answer:
    print("Oops. Your guess was too high.")
elif guess<answer:
    print("Oops. Your guess was too low.")
else:
    print("Invalid Reply")
