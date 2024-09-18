from user import user_turn
from dealer import dealer_turn
from result import win_loss, display_cards

def game():
    print("-----------\nBEGIN\n-----------")

    user_value, user_cards = user_turn()
    user_value, user_cards = user_turn(user_cards, user_value)
    dealer_value, dealer_cards = dealer_turn()
    dealer_value, dealer_cards = dealer_turn(dealer_cards, dealer_value)

    display_cards(user_cards, dealer_cards, dealer_hidden=True)
    game_active = True
    
    if user_value == 21:
        print(f"BLACKJACK! You have {user_value}.")
        game_active = False
    elif user_value > 21:
        print(f"Player busts with {user_value}.")
        print("Player busts, dealer wins")
        game_active = False

    while game_active:
        action = input(f"You have {user_value}. Hit, stand or withdraw? [h/s/w] ").lower()
        if action == 'h':
            user_value, user_cards = user_turn(user_cards, user_value)
            display_cards(user_cards, dealer_cards, dealer_hidden=True)
            if user_value >= 21:
                if user_value == 21:
                    print(f"BLACKJACK! You have {user_value}.")
                else:
                    print(f"Player busts with {user_value}.")
                    print("Player busts, dealer wins")
                break
        elif action == 's':
            break
        elif action == 'w':
            print(f"Player withdraws with {user_value}.")
            return
        else:
            print("Invalid input, please choose [h]it, [s]tand or [w]ithdraw.")
    if user_value <= 21:
        print("\nRound 2 Dealer's turn")
        display_cards(user_cards, dealer_cards, dealer_hidden=False)

        while dealer_value < 17:
            dealer_value, dealer_cards = dealer_turn(dealer_cards, dealer_value)
            display_cards(user_cards, dealer_cards, dealer_hidden=False)
    
        # Check if dealer busts
        if dealer_value > 21:
            print(f"Dealer busts with {dealer_value}. Player wins!")
        else:
            win_loss((user_value, user_cards), (dealer_value, dealer_cards))

if __name__ == '__main__':
    game()
