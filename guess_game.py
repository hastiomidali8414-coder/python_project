secret_number = 7

print("Guess the number!")

guess = int(input("Enter your guess: "))

if guess == secret_number:
    print("Congratulations! You guessed the number!")

else:
    print("Wrong guess!")
