from random import randint
import logo

print("###############################################################")
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("###############################################################")


def difficulty_selection():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        game_attempts = 10
    elif difficulty == "hard":
        game_attempts = 5
    else:
        print("Can not recognise. Set difficulty to easy.")
        game_attempts = 10
    return game_attempts


def game_logic():
    try:
        user_input = int(input("Make a guess: "))
    except ValueError:
        print("Type the number!!!")
        user_input = int(input("Make a guess: "))
    return user_input


def game_process():
    number = randint(1, 100)
    game_attempts = difficulty_selection()
    print(f"You have {game_attempts} attempts remaining to guess the number")
    user_input = game_logic()

    while user_input != number:
        if user_input < number:
            print("Too low\nGuess again.")
            game_attempts -= 1
        elif user_input > number:
            print("Too high.\nGuess again.")
            game_attempts -= 1
        else:
            print("###############################################################")
            print(f"You got it! The answer was {number}.")
            print("###############################################################")
            break
        if game_attempts == 0:
            print("###############################################################")
            print(f"You have run out of guesses, you lose. The answer was {number}.")
            print("###############################################################")
            break
        print(f"You have {game_attempts} attempts remaining to guess the number")
        user_input = game_logic()


game_process()
