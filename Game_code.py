import random
while True:
    attempts = 0
    limit=0
    print("Welcome to Number Guessing Game!")
    print("Enter the range of numbers you want to guess from.")
    Min = int(input("Enter the minimum number: "))
    Max = int(input("Enter the maximum number: "))
    A=input("Do you want to set a limit of guesses? (yes/no):").lower()
    if A == "yes":
        limit = int(input("Enter the limit of guesses: "))
    if Min >= Max:
        print("Invalid range. Minimum number must be less than maximum number.")
        continue
    Target = random.randint(Min, Max)
    print(f"Guess a number between {Min} and {Max}.")
    while True:
        if limit > 0 and attempts >= limit:
            print("You have reached the limit of guesses.")
            print(f"The correct number was {Target}.")
            break
        attempts += 1
        try:
            Guess = int(input("Enter your guess: "))
            if Guess < Min or Guess > Max:
                print(f"Please enter a number between {Min} and {Max}.")
                continue
            if Guess == Target:
                print("Congratulations! You guessed the correct number.")
                print(f"It took you {attempts} attempts.")
                break
            elif Guess < Target:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")