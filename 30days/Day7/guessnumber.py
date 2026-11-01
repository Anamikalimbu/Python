#Number guessing game (random number 1-100, hints "higher/lower", count attempts).


# number = random.randint(1, 100)
# attempts = 0

# while True:
#     guess = int(input("Guess the number (1-100): "))
#     attempts += 1

#     if guess < number:
#         print("Higher!")
#     elif guess > number:
#         print("Lower!")
#     else:
#         print(f"Congratulations! You guessed the number in {attempts} attempts.")
#         break


import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("🎮 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            attempts -= 1

        elif guess < secret_number:
            print("📈 Too low! Try a higher number.")

        elif guess > secret_number:
            print("📉 Too high! Try a lower number.")

        else:
            print("\n🎉 Congratulations! You guessed it!")
            print(f"The correct number was {secret_number}.")
            print(f"Total attempts: {attempts}")
            break

    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")
