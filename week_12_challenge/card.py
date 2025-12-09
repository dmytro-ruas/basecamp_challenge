import random
class Card:
    def __init__(self, value: str, icon: str, description: str) -> None:
        self.value = value
        self.icon = icon
        self.description = description

    def print_card(self):
        icon = self.icon
        value = self.value
        top = "┌─────────┐"
        bottom = "└─────────┘"
        side = "│         │"
        rank_right = icon
        rank_left = icon
        value = value.center(11)
        value_line = f"│{value}│"
        rank_line_left = f"│{rank_left}       │"
        rank_line_right = f"│       {rank_right}│"
        print(top)
        print(rank_line_left)
        print(side)
        print(value_line)
        print(side)
        print(rank_line_right)
        print(bottom)
    
    def play_card(self, deck: list, hand: list):
            match self.value:
                case "Skip":
                    self.skip()
                case "Attack":
                      self.attack()
                case "Defuse":
                      self.defuse(deck= deck, hand= hand)
                case "Predict_Future":
                      self.predict_future()
                case "Shuffle":
                      self.shuffle()
                case "Nope":
                      self.nope()
                case "Favor":
                      self.favor()
                case "Bomb":
                      self.bomb(hand= hand, deck= deck)
                

    def skip(self):
        print(self.description)

    
    def attack(self):
        print(self.description)
    
    def defuse(self, deck: list) -> list:
        upper_limit = len(deck)
        return_bomb_index = input(f"Where would you like to return the bomb? You can choose between 1 (on top) and {upper_limit} (last card)")
        try:
             deck.insert(int(return_bomb_index),Card("Bomb","💥","If you don't defuse this bomb you will explode and die."))
             return deck
        except:
             print("There seems to be an error")

    def predict_future(self):
        print(self.description)
    
    def shuffle(self):
       print(self.description)
    
    def nope(self):
        print(self.description)

    def favor(self):
        print(self.description)

    def bomb(self, hand: list, deck: list) -> bool:
        defused_bomb = False
        print(self.description)
        defuse_index = -1
        for card in hand:
            defuse_index += 1
            if card.value == "Defuse":
                choice = input("You have a Defuse card, would you like to use it? Y/N \n").upper()
                if choice == "Y" or choice == "YES":
                    hand.pop(defuse_index)
                    deck = self.defuse(deck= deck)
                    defused_bomb = True
        return defused_bomb,deck
                     


    