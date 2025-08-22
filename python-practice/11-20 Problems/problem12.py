# Q12. Create a number guessing game with tracking number of attempts
import random

random_number = random.randint(1, 101)
no_of_attempts = 0

while True:
    user_guess = int(input("Guess the number between 0 to 101: "))
    if 1 <= user_guess <= 100:
        if user_guess > random_number:
            print("Try lower number.\n")
            no_of_attempts += 1
        elif user_guess < random_number:
            print("Try higher number.\n")
            no_of_attempts += 1
        elif user_guess == random_number:
            print(f"Congrats 🥳! You guessed the correct number in {no_of_attempts} attempts.\n")
            no_of_attempts += 1
            break
    else:
        print("Please choose number between 0 to 101\n")

