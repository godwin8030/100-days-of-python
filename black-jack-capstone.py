import random

art = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~
~$██████╗$██╗$$$$$$█████╗$$██████╗██╗$$██╗$$$$$██╗$█████╗$$██████╗██╗$$██╗$~
~$██╔══██╗██║$$$$$██╔══██╗██╔════╝██║$██╔╝$$$$$██║██╔══██╗██╔════╝██║$██╔╝$~
~$██████╔╝██║$$$$$███████║██║$$$$$█████╔╝$$$$$$██║███████║██║$$$$$█████╔╝$$~
~$██╔══██╗██║$$$$$██╔══██║██║$$$$$██╔═██╗$██$$$██║██╔══██║██║$$$$$██╔═██╗$$~
~$██████╔╝███████╗██║$$██║╚██████╗██║$$██╗╚█████╔╝██║$$██║╚██████╗██║$$██╗$~
~$╚═════╝$╚══════╝╚═╝$$╚═╝$╚═════╝╚═╝$$╚═╝$╚════╝$╚═╝$$╚═╝$╚═════╝╚═╝$$╚═╝$~
~$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


def deal_card():
    #returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cal_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(u_score, p_score):
    if u_score == p_score:
        return "Draw!!"
    elif p_score == 0:
        return "Loser, opponent has Blackjack"
    elif u_score == 0:
        return "Win with a Blackjack"
    elif u_score > 21:
        return "You went over buddy. You lose"
    elif p_score > 21:
        return "Opponent went over. You win!!"
    elif u_score > p_score:
        return "You Win !!"
    else:
        return "You lose !!"

def play_game():    
    print(art)
    user_cards = []
    pc_cards = []
    pc_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        new_card = deal_card()
        user_cards.append(new_card)
        pc_cards.append(new_card)

    while not is_game_over:
        user_score =  cal_score(user_cards)
        pc_score =  cal_score(pc_cards)
        print(f"Your Cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {pc_cards[0]}")


        if user_score == 0 or pc_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while pc_score != 0 and pc_score < 17:
        pc_cards.append(deal_card())
        pc_score = cal_score(pc_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")
    print(compare(user_score, pc_score))

start_again = input("Do you want to play Blackjack? Type 'y' or 'n': ")
if start_again == 'y':
    print("\n"*20)
    play_game()
