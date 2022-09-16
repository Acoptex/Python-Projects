from random import randint
print('Welcome to the number guess game')
number_to_guess = randint(1,10)
number_of_tries = 1
guess = int(input('Please guess a number between 1 and 10: '))
while number_to_guess != guess:
    print('Sorry wrong number')
    if number_of_tries == 4:
        break
    elif guess < number_to_guess:
        print('Your guess was lower than the number')
    else:
        print('Your guess was higher than the number')
    guess = int(input('Please guess a number between 1 and 10: '))
    number_of_tries += 1
if number_to_guess == guess:
    print('You won!', 'You guessed', number_of_tries , 'times')
else:
    print("You loose.", 'The number was', number_to_guess)
