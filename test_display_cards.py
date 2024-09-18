from result import display_cards

def test_display_cards_hidden():
    player_cards = ['10♠', 'J♦']
    dealer_cards = ['9♠', 'Q♦']
    output = display_cards(player_cards, dealer_cards, dealer_hidden=True, test= True)
    assert "**" in output, "Dealer's card should be hidden"

def test_display_cards_revealed():
    player_cards = ['10♠', 'J♦']
    dealer_cards = ['9♠', 'Q♦']
    output = display_cards(player_cards, dealer_cards, dealer_hidden=False, test= True)
    assert "Q♦" in output, "Dealer's card should be revealed"
    
def test_display_player_hand():
    player_cards = ['10♠', 'J♦']
    dealer_cards = ['9♠', 'Q♦']
    output = display_cards(player_cards, dealer_cards, dealer_hidden=True, test= True)
    assert "10♠" in output, "Player's hand not displayed correctly"
