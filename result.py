def display_cards(player_cards, dealer_cards, dealer_hidden=True, test=False):
    max_rounds = max(len(player_cards), len(dealer_cards))
    display_output = "Player  Dealer\n"
    
    for i in range(max_rounds):
        player_card = player_cards[i] if i < len(player_cards) else "   "
        if i == 0 and dealer_hidden:
            dealer_card = "**"
        else:
            dealer_card = dealer_cards[i] if i < len(dealer_cards) else "   "
        
        display_output += f"| {player_card:<3} | {dealer_card:<3} |\n"

    if test:
        return display_output
    else:
        print(display_output)
        return ""

def win_loss(user_hand, dealer_hand, test=False):
    user_value, user_cards = user_hand
    dealer_value, dealer_cards = dealer_hand
    result_output = ''
    
    result_output += display_cards(user_cards, dealer_cards, dealer_hidden=False, test=True)
    result_output += f"Player total: {user_value}\nDealer total: {dealer_value}\n"
    
    if user_value > 21:
        result_output += "Player busts, dealer wins\n"
    elif dealer_value > 21:
        result_output += "Dealer busts, player wins\n"
    elif user_value > dealer_value:
        result_output += f"Player wins with {user_value}!\n"
    elif dealer_value > user_value:
        result_output += f"Dealer wins with {dealer_value}!\n"
    else:
        result_output += f"Push ({user_value}).\n"

    if not test:
        print(result_output)
    
    return result_output if test else ""
