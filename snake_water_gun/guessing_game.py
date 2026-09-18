import random

easy_word = ["apple","train","tiger","money","india"]
medium_word = ["python","bottle","monkey","planet","laptop"]
hard_word = ["elephant","diamond","umbrella","computer","mountain"]

print("Welcome to the Password Guessing Game!")
print("Choose a difficulty level: easy, medium or hard")

level = input("Enter a difficulty level: ").lower()
if level == 'easy':
    secret = random.choice(easy_word)
elif level == 'medium':
    secret = random.choice(medium_word)
elif level == 'hard':
    secret = random.choice(hard_word)
else:
    print("Invalid choice.Defaulting to easy level.")
    secret = random.choice(easy_word)

attempts = 0
print("\nGuess the secret password")

while True:
    guess =input("Enter your gusee: ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! You guessed it in {attempts} attempts.')
        break
    
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
        
    print("Hint: ",hint)
print("Game Over!!")

