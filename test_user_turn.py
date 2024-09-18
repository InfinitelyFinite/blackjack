from user import user_turn
def test_user_turn_adds_card():
    value, cards = user_turn([], 0)
    assert len(cards) == 1, "Initial card not drawn"

def test_user_turn_value_updates():
    value, _ = user_turn()
    assert 2 <= value <= 11, "Invalid user hand value after first draw"

def test_user_turn_two_draws():
    value, cards = user_turn(player_cards=[], player_value=0)
    value, cards = user_turn(cards, value)
    assert len(cards) == 2, "Second card not drawn correctly"


def test_user_turn_multiple_draws():
    value, cards = user_turn(player_cards=[], player_value=0)
    for _ in range(3):
        value, cards = user_turn(cards, value)
    assert len(cards) == 4, "Cards not correctly drawn after multiple turns"
    
def test_user_turn_high_value():
    value, cards = user_turn([], 20)
    assert value >= 20, "User hand value should be high after draw"
