from card import Card
class Hand:
    def __init__(self) -> None:
        self.cards_list: list[Card] = [Card("Defuse","✂️")]
        pass

    def show_hand(self):
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
        pass

    def add_card(self, deck: list[Card])-> list[Card]:
        card_to_add = deck[0]
        deck.pop(0)
        self.cards_list.append(card_to_add)
        rank_str = card_to_add.icon
        suit = card_to_add.value
        top = "┌─────────┐"
        bottom = "└─────────┘"
        side = "│         │"
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
        return deck

    def play_card(self,choice: int):
        played_card = self.cards_list[choice]
        played_card.play_card()
        self.remove_card(choice)

if __name__ == "__main__":
    deck = [Card("Attack","🗡️"),Card("Predict_Future","👁️"),Card("Shuffle","🔀")]
    Test_Hand = Hand()
    deck = Test_Hand.add_card(deck)
