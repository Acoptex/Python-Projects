import random
run_game = True
while run_game:
    print("Let's roll the dices...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print('The values are ->', dice1, 'and', dice2)
    user_selection = input("Do you want to roll the dices again? Type 'yes' or 'no' : ").lower()
    if user_selection == 'no':
        run_game = False

    
