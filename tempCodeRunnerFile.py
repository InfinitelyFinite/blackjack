from user import user_turn
from dealer import dealer_turn
from result import win_loss, display_cards

def game(test=False):
    game_output = ''
    print("-----------\nBEGIN\n-----------\n")
    user_value, user_cards = user_turn()
    user_value, user_cards = user_turn(user_cards, user_value)
    dealer_value, dealer_cards = dealer_turn()
    dealer_value, dealer_cards = dealer_turn(dealer_cards, dealer_value)

    game_output += display_cards(user_cards, dealer_cards, dealer_hidden=True, test=test)
    
    game_active = True
    game_result = ''  # Store game result at the end
    
    if user_value == 21:
        game_result = f"BLACKJACK! You have {user_value}.\n"
        game_active = False
    elif user_value > 21:
        print("-----------\nGAME RESULT\n-----------\n")
        game_result = f"Player busts with {user_value}.\nPlayer busts, dealer wins\n"
        game_active = False

    while game_active:
        action = 's' if test else input(f"You have {user_value}. Hit, stand or withdraw? [h/s/w] ").lower()
        
        if action == 'h':
            user_value, user_cards = user_turn(user_cards, user_value)
            game_output += display_cards(user_cards, dealer_cards, dealer_hidden=True, test=test)
            
            if user_value >= 21:
                if user_value == 21:
                    game_result = f"BLACKJACK! You have {user_value}.\n"
                else:
                    print("-----------\nGAME RESULT\n-----------\n")
                    game_result = f"Player busts with {user_value}.\nPlayer busts, dealer wins\n"
                break
        elif action == 's':
            break
        elif action == 'w':
            game_result = f"Player withdraws with {user_value}.\n"
            return game_output + game_result if test else ''
        else:
            game_output += "Invalid input, please choose [h]it, [s]tand or [w]ithdraw.\n"

    if user_value <= 21:
        game_output += display_cards(user_cards, dealer_cards, dealer_hidden=False, test=test)

        while dealer_value < 17:
            dealer_value, dealer_cards = dealer_turn(dealer_cards, dealer_value)
            game_output += display_cards(user_cards, dealer_cards, dealer_hidden=False, test=test)

        # Check if dealer busts or wins
        if dealer_value > 21:
            print("-----------\nGAME RESULT\n-----------\n")
            game_result = f"Dealer busts with {dealer_value}. Player wins!\n"
        else:
            print("-----------\nGAME RESULT\n-----------\n")
            game_result = win_loss((user_value, user_cards), (dealer_value, dealer_cards), test=test)

    if test:
        return game_output + game_result
    else:
        print(game_output + game_result)

if __name__ == '__main__':
    game()
