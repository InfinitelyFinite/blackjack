def display_cards(player_cards, dealer_cards, dealer_hidden=True):
    max_rounds = max(len(player_cards), len(dealer_cards))
    print("\nPlayer  Dealer")
    
    for i in range(max_rounds):
        player_card = player_cards[i] if i < len(player_cards) else "   "
        if i == 0 and dealer_hidden:
            dealer_card = "**"
        else:
            dealer_card = dealer_cards[i] if i < len(dealer_cards) else "   "
        
        print(f"| {player_card:<3} | {dealer_card:<3} |")
    print()

def win_loss(user_hand, dealer_hand):
    user_value, user_cards = user_hand
    dealer_value, dealer_cards = dealer_hand
    
    display_cards(user_cards, dealer_cards, dealer_hidden=False)

    print("-----------\nGAME RESULT\n-----------")
    print("Player total: {}\nDealer total: {}\n".format(user_value, dealer_value))
    if user_value > 21:
        print("Player busts, dealer wins")
    elif dealer_value > 21:
        print("Dealer busts, player wins")
    elif user_value > dealer_value:
        print("Player wins with {}!".format(user_value))
    elif dealer_value > user_value:
        print("Dealer wins with {}!".format(dealer_value))
    else:
        print("Push ({}).".format(user_value))
