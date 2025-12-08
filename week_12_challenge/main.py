from player import Player
from card import Card
from hand import Hand
import random,sys,os,json

def json_loader() -> list[dict]:
    path = os.path.join(sys.path[0], "deck.json")
    try:
        with open(path,mode= "r",encoding= "utf-8") as fileobj:
            deck = json.load(fileobj)
            return deck
    except FileNotFoundError:
        print("File not found")
        deck = []
        return deck

def create_deck(player_count : int):
    deck_from_json = json_loader()
    game_deck: list[Card] = []
    for card in deck_from_json:
        for name,info in card.items():
            if name == "Defuse":
                info["count"] -= player_count
            if name == "Bomb":
                info["count"] = player_count-1
            for x in range(0,info["count"]):
                card_for_player_deck = Card(name,info['icon'])
                game_deck.append(card_for_player_deck)
    random.shuffle(game_deck)
    for card in game_deck:
        print(card.icon)     


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
