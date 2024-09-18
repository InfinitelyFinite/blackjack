from result import win_loss

def test_win_loss_player_win():
    user_hand = (20, ['10♠', 'Q♦'])
    dealer_hand = (18, ['9♠', '9♦'])
    result = win_loss(user_hand, dealer_hand, test=True)
    assert "Player wins" in result, "Player win not detected"

def test_win_loss_dealer_win():
    user_hand = (18, ['9♠', '9♦'])
    dealer_hand = (20, ['J♠', '10♦'])
    result = win_loss(user_hand, dealer_hand, test=True)
    assert "Dealer wins" in result, "Dealer win not detected"

def test_win_loss_push():
    user_hand = (20, ['10♠', 'Q♦'])
    dealer_hand = (20, ['10♠', 'Q♦'])
    result = win_loss(user_hand, dealer_hand, test=True)
    assert "Push" in result, "Tie not detected"

def test_win_loss_player_bust():
    user_hand = (22, ['10♠', 'J♦', '2♥'])
    dealer_hand = (18, ['9♠', '9♦'])
    result = win_loss(user_hand, dealer_hand, test=True)
    assert "Player busts" in result, "Player bust not detected"

def test_win_loss_dealer_bust():
    user_hand = (18, ['9♠', '9♦'])
    dealer_hand = (22, ['10♠', 'J♦', '2♥'])
    result = win_loss(user_hand, dealer_hand, test=True)
    assert "Dealer busts" in result, "Dealer bust not detected"
