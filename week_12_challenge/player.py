import hand

class Player:
    def __init__(self,name: str,hand : hand.Hand) -> None:
        self.name = name
        self.hand = hand
        self.status = "alive"
        self.turns = 1

    def player_turn(self, deck, next_player):
        while self.turns > 0:
            print(f"It's your turn {self.name}")
            print("These are your cards!")
            self.hand.show_hand()
            player_choice = input("Do you want to play a card?")
            if player_choice.lower() == "yes" or player_choice.lower() == "y":
                player_card_choice = input("Enter a card that you want to play: ")
                # validatie here
                print(f"You have chosen {player_card_choice}!")
                player_card_index = int(player_card_choice) - 1
                #self.hand.play_card(self.hand.cards[player_card_choice])
                played_card = self.hand.play_card(player_card_index, deck)
                if played_card == "Attack":
                    self.turns -=1
                if played_card == "Skip":
                    self.turns -= 1
                
                self.hand.remove_card(player_card_index)
            else:
                print(player_choice)
                print("You chose not to play a card!")
            if self.status == "alive" and self.turns > 0:
                print(f"Your new card is: \n")
                self.hand.add_card(deck)
                #+ indetent on turns
                self.turns -= 1

