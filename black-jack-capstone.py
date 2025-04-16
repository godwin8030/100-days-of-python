
import random



def deal_card():
    #returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
pc_cards = []

for _ in range(2):
    new_card = deal_card()
    user_cards.append(new_card)
    pc_cards.append(new_card)

def cal_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
