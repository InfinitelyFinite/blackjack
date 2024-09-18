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

def dealer_turn(dealer_cards=[], dealer_value=0):
    if dealer_value > 17:
        return dealer_value, dealer_cards

    card_rank = randint(2, 11)
    card_suit = randint(1, 4)
    suit_map = {1: '♠', 2: '♣', 3: '♥', 4: '♦'}
    card_suit_symbol = suit_map[card_suit]

    dealer_cards.append(f"{card_rank}{card_suit_symbol}")
    dealer_value += card_rank

    return dealer_value, dealer_cards
