from dealer import draw_card
def test_draw_card_suit():
    card, _ = draw_card()
    assert card[-1] in ['♠', '♥', '♦', '♣'], "Invalid card suit"

def test_face_card_value():
    card, value = draw_card()
    if card[0] in 'JQK':
        assert value == 10, "Face card value should be 10"

def test_ace_value():
    card, value = draw_card()
    if card[0] == 'A':
        assert value == 11, "Ace should have value 11"

def test_numeric_card_value():
    card, value = draw_card()
    card_value_map = {'A': 11, 'J': 10, 'Q': 10, 'K': 10}
    if card[0] in card_value_map:
        assert value == card_value_map[card[0]], f"Card value mismatch for {card[0]}"
    else:
        assert value == int(card[0]), f"Numeric card value mismatch for {card}"

def test_card_ranks():
    for rank in range(1, 14):
        card, value = draw_card()
        assert 1 <= value <= 11, "Invalid card rank or value"
        
def test_card_name():
    card, _ = draw_card()
    valid_card_names = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    card_name = card[:-1]  # Extract card name without the suit
    assert card_name in valid_card_names, f"Invalid card name: {card}"
