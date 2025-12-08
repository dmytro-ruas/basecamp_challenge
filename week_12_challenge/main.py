from player import Player
from card import Card
from hand import Hand


def start_game():
    players_list: list[Player] = []
    # list of dictionary, we besslisen het straks

    print('Welcome to the game of Exploding kittens™')
    print('Would you like to view a Tutorial?')
    tutorial_choice = input("Yes/No: ")
    # input validatie gaat here

    if tutorial_choice.lower() == "yes" or tutorial_choice.lower() == "y":
        tutorial_view()
    print("How many players are playing? 2-5")
    # input validatie gaat here

    amount_player = input("Enter a number: ")
    for player in range(int(amount_player)):
        print(f"What is the name of player {player + 1}")
        player_name = input("Enter a name: ")
        # input validatie gaat here
        player_hand = Hand()
        player_class: Player = Player(player_name, player_hand)

    return players_list

def tutorial_view():
    pass


if __name__ == "__main__":
    start_game()
