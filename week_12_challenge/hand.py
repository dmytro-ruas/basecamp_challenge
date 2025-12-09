from card import Card
import random
class Hand:
    def __init__(self) -> None:
        self.cards_list: list[Card] = [Card("Defuse","✂️","You don't explode, you can put the bomb back in the deck.")]
        pass

    def show_hand(self):
        final_card_number = ""
        final_top = ""
        final_bottom = ""
        final_side1 = ""
        final_side2 = ""
        final_suit_line = ""
        final_rank_line_right = ""
        final_rank_line_left = ""
        index = 0
        for card in self.cards_list:
            index += 1
            icon_str = card.icon
            value = card.value
            top = "┌─────────┐"
            bottom = "└─────────┘"
            side = "│         │"
            card_number = f"[{str(index)}]".center(11)
            icon_right = icon_str
            icon_left = icon_str
            value = value.center(9)
            value_line = f"│{value}│"
            rank_line_left =  f"│{icon_left}        │"
            rank_line_right = f"│       {icon_right}│"
            final_top += top
            final_rank_line_left += rank_line_left
            final_side1 += side
            final_suit_line += value_line
            final_side2 += side
            final_rank_line_right += rank_line_right
            final_bottom += bottom
            final_card_number += card_number
        print(final_top)
        print(final_rank_line_left)
        print(final_side1)
        print(final_suit_line)
        print(final_side2)
        print(final_rank_line_right)
        print(final_bottom)
        print(final_card_number)

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



    
