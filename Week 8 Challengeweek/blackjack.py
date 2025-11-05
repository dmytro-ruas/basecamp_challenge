import random


def start_game() -> set:
    print("\n\n\nWelcome to this game of blackjack. Would you like to view a tutorial?")
    tutorial_view = input("Would you like to view a tutorial? Y/N: ")
    if tutorial_view.lower() == "yes" or tutorial_view.lower() == "y":
        tutorial_read()
    # here validation regarding player count could be added (atm programm crashes if u type in a non-number)
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
    return players_data_dict

 
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
                bets_made.append({"name": player, "bet": int(placed_bet)})
                invalid_bet = False
            else: 
                print("invalid bet!")
    return bets_made


def dealers_turn(players):
    #dia - diamonds, sp - spades, hr - hearts, cl - clubs
    card_deck = {
        "ace_dia": [1, 11],
        "king_dia": 10,
        "queen_dia": 10,
        "jack_dia": 10,
        "10_dia": 10,
        "9_dia": 9,
        "8_dia": 8,
        "7_dia": 7,
        "6_dia": 6,
        "5_dia": 5,
        "4_dia": 4,
        "3_dia": 3,
        "2_dia": 2,
        "ace_sp": [1, 11],
        "king_sp": 10,
        "queen_sp": 10,
        "jack_sp": 10,
        "10_sp": 10,
        "9_sp": 9,
        "8_sp": 8,
        "7_sp": 7,
        "6_sp": 6,
        "5_sp": 5,
        "4_sp": 4,
        "3_sp": 3,
        "2_sp": 2,
        "ace_hr": [1, 11],
        "king_hr": 10,
        "queen_hr": 10,
        "jack_hr": 10,
        "10_hr": 10,
        "9_hr": 9,
        "8_hr": 8,
        "7_hr": 7,
        "6_hr": 6,
        "5_hr": 5,
        "4_hr": 4,
        "3_hr": 3,
        "2_hr": 2,
        "ace_cl": [1, 11],
        "king_cl": 10,
        "queen_cl": 10,
        "jack_cl": 10,
        "10_cl": 10,
        "9_cl": 9,
        "8_cl": 8,
        "7_cl": 7,
        "6_cl": 6,
        "5_cl": 5,
        "4_cl": 4,
        "3_cl": 3,
        "2_cl": 2,
    }
    deck_list = list(card_deck.items())
    player_hands = []
    dealers_hand = []
    card1 = random.choice(deck_list)
    card2 = random.choice(deck_list)
    dealers_hand.append({"name": "Dealer", "cards": [card1, card2]})
    deck_list.remove(card1)
    deck_list.remove(card2)

    for player in players:
        card1 = random.choice(deck_list)
        deck_list.remove(card1)
        card2 = random.choice(deck_list)
        deck_list.remove(card2)

        player_hands.append({"name": player, "cards": [card1, card2]})

# tutorial, karten zichtbaar maken, is_spel_gedaan

def tutorial_read():
    pass


def main():
    players = start_game()
    players_balance = players_data(players)

    game_on = True
    #ik wil dat de conditie van deze loop kijkt naar het balance van spelers en gaat tot er geen players kunnen doorspelen of iedereen gestopt is
    # game on kan een list zijn met een boolean value for elke speler, of een int
    while game_on:
        bets = player_bets(players_balance)
        dealers_turn(players)


if __name__ == "__main__":
    main()

# test branch