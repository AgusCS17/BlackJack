import random
import art
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def calculate_score(cards):
    if sum(cards)==21 and len(cards) ==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)     

def play_game():
    user_cards = []
    computer_cards = []
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer first card: {computer_cards[0]}")
       
        if computer_score == 0 or user_score == 0 or user_score > 21:
            game_over = True
        else: 
            decision = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
            if decision == "y":
                user_cards.append(deal_card())
            else:
                game_over = True
        

    while computer_score != 0 and computer_score< 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Draw"
        elif computer_score == 0:
            return "Lose, opponet has blackjack"
        elif user_score == 0:
            return "You Win with Blackjack"
        elif user_score > 21:
            return "You went over, You Lose"
        elif computer_score > 21:
            return "Opponent went over, You Win"
        elif user_score> computer_score:
            return "You Win"
        else:
            return "You Lose"
    

    print(f"    Your Final cards: {user_cards}, final score: {user_score}")
    print(f"    Computer Final cards: {computer_cards}, Final score: {computer_score}")

    print(compare(user_score, computer_score))

print(art.logo)
while input("Want to play? 'y' or 'n': ").lower() == "y":
    os.system('cls')
    print(art.logo)
    play_game()
    