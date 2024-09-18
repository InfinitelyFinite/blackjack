from random import randint, choice

def draw_card():
    suits = ['♠', '♥', '♦', '♣']
    card_rank = randint(1, 13)
    card_suit = choice(suits)
    
    if card_rank in [11, 12, 13]:
        card_value = 10
    elif card_rank == 1:
        card_value = 11
    else:
        card_value = card_rank
    
    card_names = {1: "A", 11: "J", 12: "Q", 13: "K"}
    card_name = card_names.get(card_rank, str(card_rank))
    
    full_card = f"{card_name}{card_suit}"
    
    return full_card, card_value

def user_turn(player_cards=[], player_value=0):
    card, value = draw_card()
    player_cards.append(card)
    player_value += value
    return player_value, player_cards
