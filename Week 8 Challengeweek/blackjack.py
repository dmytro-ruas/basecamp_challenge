
def start_game():
    print("Welcome to this game of blackjack. Would you like to view a tutorial?")

    tutorial_view = input("Would you like to view a tutorial? Y/N ")
    if tutorial_view.lower() == "yes" or tutorial_view.lower() == "y":
        tutorial_read

    player_count = input("How many players would like to play? 1-4 ")
    player_names = set()

    while len(player_names) != int(player_count):
        player_name = is_name_valid(len(player_names) + 1)
        if player_name not in player_names:
            player_names.add(player_name)
        else:
            print("Identical names are not allowed!")
    print(player_names)
        
        
def is_name_valid(player_number):
    valid_characters = "qwertyuiopasdfghjklzxcvbnm,-/"
    invalid_name = True
    invalid_chr = False

    while invalid_name:
        name = input(f"What is the name of player {player_number} ")
        name_lower = name.lower()
        if name[0].isupper() == False:
            print("input error")
            continue
        for character in name_lower :
            if character not in valid_characters:
                print("input error")
                invalid_chr = True
        if invalid_chr:
            invalid_chr = False
            continue
        invalid_name = False
        return name

def tutorial_read():
    pass

def main():
    start_game()

if __name__ == "__main__":
    main()
