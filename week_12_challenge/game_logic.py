from player import Player
from card import Card
from hand import Hand
import random,sys,os,json


class Game_logic:
    def __init__(self) -> None:
        self.players: list[Player] = []

    def start_game(self):
        players_list: list[Player] = []
        # list of dictionary, we besslisen het straks

        print('Welcome to the game of Exploding kittens™')
        print('Would you like to view a Tutorial?')
        tutorial_choice = input("Yes/No: ")
        # input validatie gaat here

        if tutorial_choice.lower() == "yes" or tutorial_choice.lower() == "y":
            pass
        print("How many players are playing? 2-5")
        # input validatie gaat here

        amount_player = input("Enter a number: ")
        for player in range(int(amount_player)):
            print(f"What is the name of player {player + 1}")
            player_name = input("Enter a name: ")
            # input validatie gaat here
            player_hand = Hand()
            player_class: Player = Player(player_name, player_hand)
            players_list.append(player_class)

        self.players = players_list


    def json_loader(self) -> list[dict]:
        path = os.path.join(sys.path[0], "deck.json")
        try:
            with open(path,mode= "r",encoding= "utf-8") as fileobj:
                deck = json.load(fileobj)
                return deck
        except FileNotFoundError:
            print("File not found")
            deck = []
            return deck


    def create_deck(self, player_count : int) -> list[Card]:
        deck_from_json = self.json_loader()
        game_deck: list[Card] = []
        for card in deck_from_json:
            for value,info in card.items():
                if value == "Defuse":
                    info["count"] -= player_count
                if value == "Bomb":
                    info["count"] = player_count-1
                for x in range(0,info["count"]):
                    card_for_player_deck = Card(value= value,icon= info['icon'],description= info["description"])
                    game_deck.append(card_for_player_deck)
        random.shuffle(game_deck)
        return game_deck    
    
    def run_game(self):
        self.start_game()
        deck = self.create_deck(len(self.players))
        alive_players = self.players
  
        while len(alive_players) > 1:
            for player in self.players:

                if alive_players.index(player) + 1 == len(alive_players):
                    next_player = alive_players[0]
                else:
                    next_player = alive_players[alive_players.index(player) + 1]

                #next_player.turns += 1
                player.turns += 1
                player.player_turn(deck, next_player)

            

            
