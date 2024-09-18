from dealer import dealer_turn
def test_dealer_turn_initial_card():
    value, cards = dealer_turn([], 0)
    assert len(cards) == 1, "Initial dealer card not drawn"

def test_dealer_turn_value_update():
    value, _ = dealer_turn()
    assert 2 <= value <= 11, "Invalid dealer hand value after first draw"

def test_dealer_turn_multiple_cards():
    value, cards = dealer_turn([], 0)
    value, cards = dealer_turn(cards, value)
    assert len(cards) == 2, "Dealer didn't draw second card"

def test_dealer_turn_stops_at_17():
    value, cards = dealer_turn([], 16)
    value, cards = dealer_turn(cards, value)
    assert value >= 17, "Dealer should stop drawing at 17 or higher"

def test_dealer_turn_high_value():
    dealer_value = 18
    dealer_cards = ['9♠', '9♣'] #example
    value, cards = dealer_turn(dealer_cards, dealer_value)
    assert value == 18, "Dealer should not draw if already above 17"
    assert len(cards) == 2, "Dealer should have only the initial two cards"

