
import random
import os
from art import logo

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return (card)

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, oppenent haws Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return"You went over, you lose"
    elif computer_score > 21:
        return "Oppenent went over. You Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():

    print(logo)

    user_cards = []
    computer_cards = []

    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card()) 
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" computer First card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, Type 'n' to Pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"   Your Final hand: {user_cards}, Final score: {user_score}")
    print(f"   Computer Final hand: {computer_cards}, Final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': "):
    os.system("cls")
    play_game()
   




#sample is use to hoice multiple number from list and sum it

'''for user in card:
        user = random.sample((card),2)
        for computer in card:
        computer = random.sample((card),2)
    print(user)
    #print(computer)
    add_user = sum(sample(user, 2))
    add_computer = sum(sample(computer, 2))
    print(add_user)
    print(add_computer)'''

