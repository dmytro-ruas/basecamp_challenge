import random
import sys
import time
 

def start_game() -> set:
    print("\n\n\nWelcome to this game of blackjack. Would you like to view a tutorial?")
    tutorial_view = input("Would you like to view a tutorial? Y/N: ")
    if tutorial_view.lower() == "yes" or tutorial_view.lower() == "y":
        tutorial_read()
    # here validation regarding player count could be added (atm programm crashes if u type in a non-number)
    player_count = input("\nHow many players would like to play? 1-4: ")
    while not player_count.isdecimal() or int(player_count) >4:
        player_count = input("\nHow many players would like to play? 1-4: ")
    player_names = set()
    while len(player_names) != int(player_count):
        player_name = is_name_valid(len(player_names) + 1)
        if player_name not in player_names:
            player_names.add(player_name)
        else:
            print("Identical names are not allowed!")
    return player_names
 
   
def players_data(players: set) -> dict:
    players_data_dict = {}
    for player_name in players:
        players_data_dict[player_name] = 300
    return players_data_dict #returns in format (Str:int)
 
 
def is_name_valid(player_number: int) -> str:
    valid_characters = "qwertyuiopasdfghjklzxcvbnm,-/"
    invalid_name = True
    invalid_chr = False
    
    while invalid_name:
        name = input(f"\nWhat is the name of player {player_number}: ")
        name_lower = name.lower()
        if name[0].isupper() == False:
            print("input error")
            continue
        for character in name_lower :
            if character not in valid_characters:
                print("input error")
                invalid_chr = True
        if invalid_chr:
            invalid_chr = False
            continue
        invalid_name = False
        return name
 
 
def player_bets(player_balances: dict) -> list:
    bets_made = []
    valid_numbers = set("1234567890")
    for player in player_balances:
        invalid_bet = True
        while invalid_bet:
        # look how much money a player has, tell him to input a bet in a range of his balance. place the bet and put it into a dictionary
            placed_bet = input(f"\n{player}, place a bet between 1 and {player_balances[player]}: ")
            # hier moet een volledige validatie van de bet staan. Geldige letters en geldig aantal geld.
 
            if player_balances[player] - int(placed_bet) >= 0:
                #bets_made[player] = int(placed_bet)
                bets_made.append({"name": player, "bet": int(placed_bet)})
                invalid_bet = False
            else:
                print("invalid bet!")
    return bets_made
 
 
def display_dealer_first_hand(card :tuple):
    print("Dealer First Card:")
    value_card,suit,rank_str = card
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"
    if rank_str == "10":  # Ten is the only rank with two digits
        rank_right = rank_str
        rank_left = rank_str
    else:
        rank_right = rank_str + " "
        rank_left = " " + rank_str
    suit_line = f"│    {suit}    │"
    rank_line_left = f"│{rank_left}       │"
    rank_line_right = f"│       {rank_right}│"
    print(top)
    print(rank_line_left)
    print(side)
    print(suit_line)
    print(side)
    print(rank_line_right)
    print(bottom)
 
def display_hand_player(player_name: str, hand: list[tuple[int,str,str]]):
    if player_name == "Dealer:":
        print("This was the dealer's hand: ")
    else:
        print(f"{player_name} this is your hand: ")
    final_top = ""
    final_bottom = ""
    final_side1 = ""
    final_side2 = ""
    final_suit_line = ""
    final_rank_line_right = ""
    final_rank_line_left = ""
    tot_value = 0
    for card in hand:
        value_card,suit,rank_str = card
        tot_value += value_card
        if tot_value > 21 and rank_str == "A":
            tot_value -= 10
        top = "┌─────────┐"
        bottom = "└─────────┘"
        side = "│         │"
        if rank_str == "10":  # Ten is the only rank with two digits
            rank_right = rank_str
            rank_left = rank_str
        else:
            rank_right = rank_str + " "
            rank_left = " " + rank_str
        suit_line = f"│    {suit}    │"
        rank_line_left = f"│{rank_left}       │"
        rank_line_right = f"│       {rank_right}│"
        final_top += top
        final_rank_line_left += rank_line_left
        final_side1 += side
        final_suit_line += suit_line
        final_side2 += side
        final_rank_line_right += rank_line_right
        final_bottom += bottom
    print(final_top)
    print(final_rank_line_left)
    print(final_side1)
    print(final_suit_line)
    print(final_side2)
    print(final_rank_line_right)
    print(final_bottom)
    
    
def hit_or_stay(player:str ,hand: list[tuple[int,str,str]], deck: dict, deck_keys: list) -> list[tuple[int,str,str]]:
    value = 0
    for card in hand:
        value += card[0]
    while value < 21:
        player_choice = input(f"{player} would you like to Hit [H] or Stay [S]? If you want to see your hand again type HAND!\n").upper()
        valid_set = {'H','HIT','S','STAY',"HAND"}
        while player_choice not in valid_set:
            print("Please input a valid move")
            player_choice = input(f"{player} would you like to Hit [H] or Stay [S]? If you want to see your hand again type HAND!\n").upper()
        if player_choice == "H" or player_choice == 'HIT':
            new_card_key = random.choice(deck_keys)
            new_card = deck[new_card_key]
            deck_keys.remove(new_card_key)
            deck.pop(new_card_key)
            value += new_card[0]
            hand.append(new_card)
            if value > 21:
                for card in hand:
                    if card[2] == 'A':
                        value -= 10
            display_hand_player(player,hand)
        elif player_choice == "HAND" or player_choice == "HAND!":
            display_hand_player(player,hand)
        else:
            return hand
    return hand
            
            
 
def dealers_turn(bets: list, players_balance: dict):
    players = set(players_balance.keys())
    card_deck = {
        "A♦": (11,'♦','A'),
        "K♦": (10,'♦','K'),
        "Q♦": (10,'♦','Q'),
        "J♦": (10,'♦','J'),
        "10♦": (10,'♦','10'),
        "9♦": (9,'♦','9'),
        "8♦": (8,'♦','8'),
        "7♦": (7,'♦','7'),
        "6♦": (6,'♦','6'),
        "5♦": (5,'♦','5'),
        "4♦": (4,'♦','4'),
        "3♦": (3,'♦','3'),
        "2♦": (2,'♦','2'),
        "A♠": (11,'♠','A'),
        "K♠": (10,'♠','K'),
        "Q♠": (10,'♠','Q'),
        "J♠": (10,'♠','J'),
        "10♠": (10,'♠','10'),
        "9♠": (9,'♠','9'),
        "8♠": (8,'♠','8'),
        "7♠": (7,'♠','7'),
        "6♠": (6,'♠','6'),
        "5♠": (5,'♠','5'),
        "4♠": (4,'♠','4'),
        "3♠": (3,'♠','3'),
        "2♠": (2,'♠','2'),
        "A♥": (11,'♥','A'),
        "K♥": (10,'♥','K'),
        "Q♥": (10,'♥','Q'),
        "J♥": (10,'♥','J'),
        "10♥": (10,'♥','10'),
        "9♥": (9,'♥','9'),
        "8♥": (8,'♥','8'),
        "7♥": (7,'♥','7'),
        "6♥": (6,'♥','6'),
        "5♥": (5,'♥','5'),
        "4♥": (4,'♥','4'),
        "3♥": (3,'♥','3'),
        "2♥": (2,'♥','2'),
        "A♣": (11,'♣','A'),
        "K♣": (10,'♣','K'),
        "Q♣": (10,'♣','Q'),
        "J♣": (10,'♣','J'),
        "10♣": (10,'♣','10'),
        "9♣": (9,'♣','9'),
        "8♣": (8,'♣','8'),
        "7♣": (7,'♣','7'),
        "6♣": (6,'♣','7'),
        "5♣": (5,'♣','5'),
        "4♣": (4,'♣','4'),
        "3♣": (3,'♣','3'),
        "2♣": (2,'♣','2'),
    }
    deck_keys = list(card_deck.keys())
    player_hands = {}
    dealer_hand = {}
    card1_key = random.choice(deck_keys)
    card1 = card_deck[card1_key]
    card1 = card_deck[card1_key]
    deck_keys.remove(card1_key)
    card_deck.pop(card1_key)
    card2_key = random.choice(deck_keys)
    card2 = card_deck[card2_key]
    deck_keys.remove(card2_key)
    card_deck.pop(card2_key)
    display_dealer_first_hand(card1)
    dealer_hand["cards"] = [card1, card2]
    dealer_hand["value"] = card1[0] + card2[0]
    for player in players:
        card1_key = random.choice(deck_keys)
        card1 = card_deck[card1_key]
        card_deck.pop(card1_key)
        deck_keys.remove(card1_key)
        card2_key = random.choice(deck_keys)
        card2 = card_deck[card2_key]
        deck_keys.remove(card2_key)
        card_deck.pop(card2_key)
        value = card1[0]+card2[0]
        player_hands[player] = {"cards": [card1, card2], "value": value}
        current_player_hand = player_hands[player]["cards"]
        display_hand_player(player,current_player_hand)
    for player in players:
        current_player_hand = player_hands[player]["cards"]
        current_player_hand = hit_or_stay(player,current_player_hand,card_deck,deck_keys)
        value = 0
        for card in current_player_hand:
            value += card[0]
        if value > 21:
            for card in current_player_hand:
                if card[2] == "A":
                    value -= 10
        player_hands[player]["value"] = value
        if value >21:
            player_hands[player]["value"] = 0        
    dealer_value = dealer_hand['value']
    if dealer_value < 17:
        new_card_key = random.choice(deck_keys)
        new_card = card_deck[new_card_key]
        deck_keys.remove(new_card_key)
        card_deck.pop(new_card_key)
        dealer_hand['cards'].append(new_card)
    display_hand_player("Dealer",dealer_hand['cards'])
    if dealer_value > 21:
        for card in dealer_hand["cards"]:
            suit = card[2]
            if suit == "A":
                dealer_value -= 10
    if dealer_value > 21:
        dealer_value = 0
    winners = []
    losers = []
    tied = []
    if len(players) > 0:
        for player in players:
            if player_hands[player]["value"] == 0:
                print(f"{player} Busted")
                losers.append(player)
            elif dealer_value == 0:
                print(f"Dealer busted, remaining players win")
                winners.append(player)
            elif dealer_value > player_hands[player]["value"]:
                print(f"{player} lost their bet, dealer has better hand")
                losers.append(player)
            elif dealer_value == player_hands[player]["value"]:
                print(f"The game is a tie")
                tied.append(player)
            else:
                print(f"{player} win their bet, they have the better hand")
                winners.append(player)
            game_result = winners, losers, tied
        player_balance = balance_update(bets, game_result, players_balance)
        return player_balance
 
 
def balance_update(bets: list[dict], game_result: tuple[list], players_balance): # bets, player_balance,
    winners, losers, tied = game_result
    for player in bets:
        player_name = player["name"]
        if player_name in winners:
            current_balance = players_balance[player_name]
            player_bet = player["bet"]
            current_balance += player_bet
            players_balance[player_name] = current_balance
        if player_name in losers:
            current_balance = players_balance[player_name]
            player_bet = player["bet"]
            current_balance -= player_bet
            players_balance[player_name] = current_balance
    return players_balance
# tutorial, karten zichtbaar maken, is_spel_gedaan
 
def tutorial_read():
    slow_type("Welcome to the game of Blackjack!")
    slow_type("")
    slow_type("The goal is simple: get a hand value as close to 21 as possible, without going over.")
    slow_type("")
    slow_type("You're playing against the dealer. You want your hand to be higher than the dealer's hand.")
    slow_type("")
    slow_type("Let's play for points to keep score! You will start with 300 points.")
    slow_type("")
    slow_type("Before each round, you'll decide how many points (like 5 or 10) you want to play for.")
    slow_type("")
    slow_type("If you lose the round, you lose the points you played for.")
    slow_type("If you win the round, you get back double the points you played for (your original points, plus that same amount in winnings).")
    slow_type("")
    slow_type("Be careful, though! If your point score reaches zero, the game is over.")
    slow_type("")
    slow_type("Let's learn the card values:")
    slow_type("")
    slow_type("Cards 2 through 10 are worth their face value.")
    slow_type("(e.g., a 5 is worth 5 points)")
    slow_type("")
    slow_type("Jacks, Queens, and Kings are each worth 10 points.")
    slow_type("")
    slow_type("The Ace is special! It can be worth 1 point or 11 points, whichever helps your hand more.")
    slow_type("")
    slow_type("The game starts. You and the dealer both get two cards.")
    slow_type("")
    slow_type("You'll see both of your cards.")
    slow_type("")
    slow_type("You'll only see one of the dealer's cards. The other is face-down.")
    slow_type("")
    slow_type("Now, it's your turn. You have two main choices: \"Hit\" or \"Stand\".")
    slow_type("")
    slow_type("If you \"Hit\", you take another card.")
    slow_type("")
    slow_type("You can hit as many times as you want, as long as your total doesn't go over 21.")
    slow_type("")
    slow_type("If you \"Stand\", you keep the cards you have and end your turn.")
    slow_type("")
    slow_type("Be careful! If your hand's total goes over 21, that's a \"Bust\", and you automatically lose your points for the round.")
    slow_type("")
    slow_type("Once you stand (or bust), it's the dealer's turn.")
    slow_type("")
    slow_type("The dealer will reveal their hidden card.")
    slow_type("")
    slow_type("The dealer has rules they must follow.")
    slow_type("")
    slow_type("If the dealer's hand is 16 or less, they *must* hit.")
    slow_type("")
    slow_type("If the dealer's hand is 17 or more, they *must* stand.")
    slow_type("")
    slow_type("So, who wins?")
    slow_type("")
    slow_type("If your hand is closer to 21 than the dealer's (and you didn't bust), you win the round!")
    slow_type("")
    slow_type("If the dealer busts (goes over 21), you also win the round!")
    slow_type("")
    slow_type("If the dealer's hand is closer to 21 than yours, the dealer wins, and you lose your points for the round.")
    slow_type("")
    slow_type("What if you both have the same total? That's called a \"Push\", and it's a tie. You don't win or lose any points.")
    slow_type("")
    slow_type("One last thing: A \"Blackjack\" is when your first two cards are an Ace and a 10-point card (10, J, Q, or K).")
    slow_type("")
    slow_type("It's the best possible hand! It usually means you win 2 times your points for that round!")
    slow_type("")
    slow_type("That's the basic game! Ready to play? Try to see how high you can get your point score!")
    


def slow_type(output_string):
    # Ik heb deze functie online gevonden om mijn tutorial langzaam te printen. 
    typing_speed = 120 #wpm
    for letter in output_string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print (" ")
 
 
def main():
    players = start_game()
    player_balance = players_data(players)
 
    game_on = True
    while game_on:
        bets = player_bets(player_balance)
        player_balance = dict(dealers_turn(bets, player_balance))
        player_remove = []
        for player_name,balance in player_balance.items():
            if balance == 0:
                player_remove.append(player_name)
        for player in player_remove:
            print(f"{player} sucks at this game and has run out of money. They are out.")
            player_balance.pop(player)
        if len(player_balance) == 0:
            print("Everyone is out of money, the game will end now")
            game_on = False

 
if __name__ == "__main__":
    main()