import card
class Hand:
    def __init__(self) -> None:
        self.cards_list: list[card.Card] = []
        pass

    def show_hand(self):
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

    def add_card(self):
        return "card name"

    def play_card(self, card_name):
        pass

    def play_card(self,choice: int):
        played_card = self.cards_list[choice]
        played_card.play_card()
        self.remove_card(choice)

