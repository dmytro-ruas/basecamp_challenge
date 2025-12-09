import hand

class Player:
    def __init__(self,name: str,hand : hand.Hand) -> None:
        self.name = name
        self.hand = hand
        self.status = "alive"
        self.turns = 1

    def player_turn(self, deck):
        while self.turns > 0:
            print(f"It's your turn {self.name}")
            print("These are your cards!")
            self.hand.show_hand()
            player_choice = input("Do you want to play a card?")
            if player_choice.lower == "yes" or player_choice.lower == "y":
                player_card_choice = input("Enter a card that you want to play: ")
                # validatie here
                print(f"You have chosen {player_card_choice}!")
                #self.hand.play_card(self.hand.cards[player_card_choice])
                self.hand.play_card(int(player_card_choice))

                self.hand.remove_card(int(player_choice))
            else:
                print("You chose not to play a card!")
            print(f"Your new card is: \n")
            self.hand.add_card(deck)
            self.turns -= 1

