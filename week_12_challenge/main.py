from player import Player
from card import Card
from hand import Hand
import random,sys,os,json
from game_logic import Game_logic
# def json_loader() -> list[dict]:
#     path = os.path.join(sys.path[0], "deck.json")
#     try:
#         with open(path,mode= "r",encoding= "utf-8") as fileobj:
#             deck = json.load(fileobj)
#             return deck
#     except FileNotFoundError:
#         print("File not found")
#         deck = []
#         return deck

# def create_deck(player_count : int) -> list[Card]:
#     deck_from_json = json_loader()
#     game_deck: list[Card] = []
#     for card in deck_from_json:
#         for value,info in card.items():
#             if value == "Defuse":
#                 info["count"] -= player_count
#             if value == "Bomb":
#                 info["count"] = player_count-1
#             for x in range(0,info["count"]):
#                 card_for_player_deck = Card(value= value,icon= info['icon'],description= info["description"])
#                 game_deck.append(card_for_player_deck)
#     random.shuffle(game_deck)
#     return game_deck    


# def tutorial_view():
#     pass

def test():
    deck = [Card("Bomb","💥",'Defuse'),Card("Bomb","💥",'Defuse')]
    Chris = Player("Chris",Hand())
    Chris.player_turn(deck)

    
if __name__ == "__main__":
    #game = Game_logic()
    #game.run_game()
    test()
