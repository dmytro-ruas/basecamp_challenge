import random

def boardgame_printer(board_dictionary :dict):
    print(board_dictionary["A1"],'|',board_dictionary["A2"],"|",board_dictionary["A3"])
    print("---------")
    print(board_dictionary["B1"],'|',board_dictionary["B2"],"|",board_dictionary["B3"])
    print("---------")
    print(board_dictionary["C1"],'|',board_dictionary["C2"],"|",board_dictionary["C3"])


def game_input_checker(input_string :str, board_dictionary :dict):
    valid_list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
    if input_string in valid_list:
        if board_dictionary[input_string] == " ":
            return True
        else:
            return False
    else:
        return False


def winner_checker_tic_tac_toe(board_dictionary :dict):
    row1 = ["A1","A2","A3"]
    row2 = ["B1","B2","B3"]
    row3 = ["C1","C2","C3"]
    column1 = ["A1","B1","C1"]
    column2 = ["A2","B2","C2"]
    column3 = ["A3","B3","C3"]
    diagonal1 = ["A1","B2","C3"]
    diagonal2 = ["A3","B2","C1"]
    valid_list = [row1,row2,row3,column1,column2,column3,diagonal1,diagonal2]
    for list in valid_list:
        value1 = board_dictionary[list[0]]
        value2 = board_dictionary[list[1]]
        value3 = board_dictionary[list[2]]
        if value1 == value2 and value2 == value3:
            if value1 == "X":
                return "1"
            elif value2 == "O":
                return "0"
            else:
                continue
    return False            

 
 
def is_count_valid():
    input_valid = False
    while input_valid == False:
        player_count = input("Hoeveel spelers zijn er? ")
        if player_count == "1" or player_count == "2":
            input_valid = True
            return player_count
            break
        else:
            print("input error")
 

def is_extra_game():
    extra_game_input = input("One more game?")
    extra_game_input_lower = extra_game_input.lower()
    if extra_game_input_lower == "no":
        extra_game = False
        return False
    return True
    

def single_player_tic_tac_toe():
    print("WIP")


def leaderboard_tic_tac_toe(player_list :list[str], game_count :int, is_winner :bool, current_leaderboard :list[str]):
    if game_count == 1:
        start_leaderboard = current_leaderboard
    else:
        if is_winner == True:
            current_leaderboard.append





def two_player_tic_tac_toe(game_count : int, player_list : list[str],current_leaderboard : list[str]):
    board = {
    "A1":" ",
    "A2":" ",
    "A3":" ",
    "B1":" ",
    "B2":" ",
    "B3":" ",
    "C1":" ",
    "C2":" ",
    "C3":" ",}
    boardgame_printer(board)
    turn = 1
    game_is_over = False
    while not game_is_over:
        player_turn = turn % 2
        player_name = player_list[player_turn]
        input_player = input(f"{player_name} please input your move: ")
        while not game_input_checker(input_player, board):
            input_player = input(f"{player_name} please input a valid move: ")
        if player_turn == 1:
            board[input_player] = "X"
        else:
            board[input_player] = "O"
        turn += 1
        boardgame_printer(board)
        if turn > 5:
            game_is_over = winner_checker_tic_tac_toe(board)
        if turn == 10:
            break
    if game_is_over == "1":
        print(player_list[1], "has won!")
        is_winner = True
        winner = player_list [1]
        loser = player_list[0]
    elif game_is_over == "0":
        print(player_list[0], "has won!")
        is_winner = True
        winner = player_list [0]
        loser = player_list[1]
        player_list = [loser,winner]
    else: 
        is_winner = False
        print("The game is a tie!")
        randomnumber1 = random.randint(0,1)
        randomnumber2 = (randomnumber1 + 1) % 2
        player_1 = player_list[randomnumber1]
        player_2 = player_list[randomnumber2]
        player_list =  [player_2,player_1]

    return player_list


def is_name_valid(player):
    valid_characters = "qwertyuiopasdfghjklzxcvbnm,-/"
 
    # variables die de loops helpen
    invalid_name = True
    invalid_chr = False
    # validatie loop
    while invalid_name:
        # input en een lowercase versie dat we nodig hebben om voor invalid characters te checken
        name = input(f"Name {player}: ")
        name_lower = name.lower()
        # die if controleert de hoofdletter
        if name[0].isupper() == False:
            print("input error")
            continue
        # die hele loop controleert dat er geen nummers in staan
        # als er iets invalid instaan, dan gaat de programma dit if in - die zegt dat er iets invalid is
        for character in name_lower :
            if character not in valid_characters:
                print("input error")
                invalid_chr = True
        # daarna, als er iets invalid instaan, gaat de programma dit if in, en het resets de inputproces
        if invalid_chr:
            invalid_chr = False
            continue
        # als er niets invalid is, dan kunnen we de loop stoppen en de name terug sturen
        invalid_name = False
        return name
       
        
      
def main ():
    game_count = 1
    extra_game = True
    player_count = int(is_count_valid())
    while extra_game:
        if player_count == 1:
            print("Het spel zal beginnen met 1 Speler")
            single_player_tic_tac_toe()
        else:
            print("Het spel zal beginnen met 2 Spelers")
            if game_count == 1:
                name_p1 = is_name_valid("player 1")
                name_p2 = is_name_valid("player 2")            
                player_list = [name_p2,name_p1]
                randomnumber1 = random.randint(0,1)
                randomnumber2 = (randomnumber1 + 1) % 2
                player_1 = player_list[randomnumber1]
                player_2 = player_list[randomnumber2]
                player_order_list =  [player_2,player_1]
                leaderboard_list = ["TIC TAC TOE Leaderboard",name_p1,name_p2]
            player_order_list = two_player_tic_tac_toe(game_count,player_order_list,leaderboard_list)
        extra_game = is_extra_game()
        if extra_game:
            game_count += 1

if __name__ == "__main__":
    main()