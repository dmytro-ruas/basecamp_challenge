
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
                print("Player 1 wins")
                return 1
            elif value2 == "O":
                print("Player 2 wins")
                return 2
            else:
                continue
    return False            

 
 
def is_count_valid():
    input_valid = False
    while input_valid == False:
        player_count = input("Hoeveel spelers zijn er?")
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


def two_player_tic_tac_toe(game_count :int, player_list :list[str]):
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
        game_is_over = winner_checker_tic_tac_toe(board)
    if game_is_over == 1:
        print(player_list[1], "has won!")
        winner = player_list [1]
        loser = player_list[0]
    else :
        print(player_list[0], "has won!")
        winner = player_list [0]
        loser = player_list[1]
        player_list = [loser,winner]
    return player_list




        
      
def main ():
    game_count = 1
    extra_game = True
    player_count = int(is_count_valid())
    player_list= ["Christopher","Dimitri"]
    while extra_game:
        if player_count == 1:
            print("Het spel zal beginnen met 1 Speler")
            single_player_tic_tac_toe()
        else:
            print("Het spel zal beginnen met 2 Spelers")
            player_list = two_player_tic_tac_toe(game_count,player_list)
    extra_game = is_extra_game()
    if extra_game:
        game_count += 1

if __name__ == "__main__":
    main()