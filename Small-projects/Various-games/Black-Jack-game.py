# Black Jack rules
# The deck is unlimited in size
# There are no jokers
# The Jack/Queen/King all count as 10
# The Ace can count as 11 or 1
# Use the following list as the deck of cards:
import random


# The cards in the list have the equal probability of being drawn
# Cards are not removed from deck as they are drawn

def deal_card(cards):
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))
    computer_cards.append(deal_card([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]))


def calculate_score(score_list):
    total = 0
    for item in score_list:
        total += item
    return total


print(user_cards)
print(computer_cards)

print(f"User score is {calculate_score(user_cards)}")
print(f"Computer score is {calculate_score(computer_cards)}")
if calculate_score(user_cards) > calculate_score(computer_cards):
    print("User wins")
else:
    print("Computer wins")
