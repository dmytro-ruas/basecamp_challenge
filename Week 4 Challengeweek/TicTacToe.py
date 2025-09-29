
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
                return "Player 1 wins!"
            elif value2 == "O":
                return "Player 2 wins!"
            else:
                continue
    return "No winner yet!"            

        
      
def main ():
    board = {
    "A1":"X",
    "A2":"O",
    "A3":"X",
    "B1":" ",
    "B2":"X",
    "B3":" ",
    "C1":"X",
    "C2":"O",
    "C3":" ",}
    print(winner_checker_tic_tac_toe(board))
if __name__ == "__main__":
    main()    