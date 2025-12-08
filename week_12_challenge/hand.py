from card import Card
class Hand:
    def __init__(self) -> None:
        self.cards_list: list[Card] = [Card("Defuse","✂️","You don't explode, you can put the bomb back in the deck.")]
        pass

    def show_hand(self):
        card_number = "[]"
        final_top = ""
        final_bottom = ""
        final_side1 = ""
        final_side2 = ""
        final_suit_line = ""
        final_rank_line_right = ""
        final_rank_line_left = ""
        for card in self.cards_list:
            rank_str = card.icon
            suit = card.value
            top = "┌─────────┐"
            bottom = "└─────────┘"
            side = "│         │"
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

    def remove_card(self, choice: int):
        self.cards_list.pop(choice)

    def add_card(self, deck: list[Card])-> list[Card]:
        card_to_add = deck[0]
        card_to_add.print_card()
        if card_to_add.value == "Bomb":
            card_to_add.play_card(deck= deck, hand= self.cards_list)
            deck.pop(0)
        else:
            self.cards_list.append(card_to_add)
            deck.pop(0)
        return deck

    def play_card(self,choice: int,deck: list[Card]) -> list[Card]:
        if choice < len(self.cards_list)-1:
            played_card = self.cards_list[choice]
            played_card.play_card(deck= deck, hand= self.cards_list)
            self.remove_card(choice)
        else:
            print("Invalid Choice")

if __name__ == "__main__":

    deck = [Card("Bomb","💥","If you don't defuse this bomb you will explode and die."),Card("Attack","🗡️","End your turn without drawing. Force the next player to take 2 turns."),Card("Predict_Future","👁️","Peek at the top 3 cards from the Draw Pile. Put them back in the same order."),Card("Shuffle","🔀","Shuffle the Draw Pile thoroughly.")]
    Test_Hand = Hand()
    Test_Hand.show_hand()
    deck = Test_Hand.add_card(deck)
    Test_Hand.show_hand()

    
