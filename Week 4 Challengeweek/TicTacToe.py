import sys,time,random


def slow_type(output_string):
    # Ik heb deze functie online gevonden om mijn tutorial langzaam te printen. 
    typing_speed = 90 #wpm
    for letter in output_string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print (" ")

def bot_player_logic(): 
    valid_list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"] 
    board = {
    "A1":" ",
    "B1":" ",
    "C1":" ",
    "A2":" ",
    "B2":" ",
    "C2":" ",
    "A3":" ",
    "B3":" ",
    "C3":" ",}
    move_valid = False 
    while move_valid is not True: 
        bot_move = random.choice(valid_list) 
        if game_input_checker(bot_move, board): 
            move_valid = True 
            valid_list.remove(bot_move) 
        return bot_move
    
# Deze functie print het spelbord
def boardgame_printer(board_dictionary : dict):
    # Met behulp van de dictionary die word meegegeven met de functie print ik het spelbord.
    print(board_dictionary["A1"],'|',board_dictionary["A2"],"|",board_dictionary["A3"])
    print("---------")
    print(board_dictionary["B1"],'|',board_dictionary["B2"],"|",board_dictionary["B3"])
    print("---------")
    print(board_dictionary["C1"],'|',board_dictionary["C2"],"|",board_dictionary["C3"])

# Deze functie checkt of de input geldig was 
def game_input_checker(input_string :str, board_dictionary : dict):
    valid_list = ["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
    # Hier word een input gecheckt met de lijst, als hij niet in de lijst is is het niet geldig.
    if input_string.upper() in valid_list:
        # Hier word er gecheckt of de positie in het bord wel degelijk leeg is. 
        # Dit doe ik door de value te halen van de dictionary m.b.v. de input als key
        if board_dictionary[input_string] == " ":
            return True
        else:
            return False
    else:
        return False

# Deze functie check of er iemand een potje heeft gewonnen. 
def winner_checker_tic_tac_toe(board_dictionary :dict):
    #Hier maak ik verschillende lijsten aan met de posities die gecheckt moeten worden.
    row1 = ["A1","A2","A3"]
    row2 = ["B1","B2","B3"]
    row3 = ["C1","C2","C3"]
    column1 = ["A1","B1","C1"]
    column2 = ["A2","B2","C2"]
    column3 = ["A3","B3","C3"]
    diagonal1 = ["A1","B2","C3"]
    diagonal2 = ["A3","B2","C1"]
    # Deze lijsten worden in 1 grote lijst gestoken zodat ik hier makkelijk door kan lopen en alles in 1 loop controleer
    valid_list = [row1,row2,row3,column1,column2,column3,diagonal1,diagonal2]
    for list in valid_list:
        # hier worden de values gehaald van dictionary met behulp van de values in de list als keys 
        value1 = board_dictionary[list[0]]
        value2 = board_dictionary[list[1]]
        value3 = board_dictionary[list[2]]
        # Als alle drie values gelijk zijn hebben we een winnaar!
        if value1 == value2 and value2 == value3:
            # Als de value X is heeft speler 1 gewonnen en word returned om te gebruiken in de logica van het spel
            if value1 == "X":
                return "1"
            # Als de value O is heeft speler 2 gewonnen
            elif value1 == "O":
                return "0"
            # Als we hier geraken betekend dat alle drie de values " " zijn. In dit geval herhalen we de loop.
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
 
    while True:
        extra_game_input = input("One more game? Yes/No ")
        extra_game_input_lower = extra_game_input.lower()
        if extra_game_input_lower == "yes" or extra_game_input_lower == "no":
            if extra_game_input_lower == "yes":
                break
            if extra_game_input_lower == "no":
                extra_game = False
                return False
        else:
            print("Didn't quite catch that, type Yes or No")
    return True
    

def single_player_tic_tac_toe(game_count : int, player_list : list[str],current_leaderboard : list[str]):
    board = {
    "A1":" ",
    "B1":" ",
    "C1":" ",
    "A2":" ",
    "B2":" ",
    "C2":" ",
    "A3":" ",
    "B3":" ",
    "C3":" ",}
    boardgame_printer(board)
    turn = 1
    game_is_over = False
    while not game_is_over:
        player_turn = turn % 2
        player_name = player_list[player_turn]
        if player_turn == 1:
            symbol_player = "X"
            input_player = input(f"{player_name} please input your move ({symbol_player}): ")
            input_player = input_player.upper()
            while not game_input_checker(input_player, board):
                input_player = input(f"{player_name} please input a valid move: ")
                input_player = input_player.upper()
            board[input_player] = "X"
        else:
            print("Mr. Robot is thinking")
            input_bot = str(bot_player_logic())
            while not game_input_checker(input_bot, board):
                input_bot = bot_player_logic()
            board[input_bot] = "O"
        turn += 1
        boardgame_printer(board)
        if turn > 5:
            game_is_over = winner_checker_tic_tac_toe(board)
        if turn == 10:
            break
    if game_is_over == "1":
        print(player_list[1], "heeft gewonnen!")
        is_winner = True
        winner = player_list [1]
        loser = player_list[0]
        player_list = [loser,winner]
    elif game_is_over == "0":
        print(player_list[0], "heeft gewonnen!")
        is_winner = True
        winner = player_list [0]
        loser = player_list[1]
        player_list = [loser,winner]
    else: 
        is_winner = False
        print("Het is gelijkspel!")
        randomnumber1 = random.randint(0,1)
        randomnumber2 = (randomnumber1 + 1) % 2
        player_1 = player_list[randomnumber1]
        player_2 = player_list[randomnumber2]
        player_list =  [player_2,player_1]
    current_leaderboard = leaderboard_tic_tac_toe(player_list,game_count,is_winner,current_leaderboard)    
    return_list = [player_list,current_leaderboard]
    return return_list


# Deze functie checkt wie er het het meest aan het winnen is.
def lead_counter(current_leaderboard : list[list[str]]):
    # Current_leaderboard is een list van lists, de eerste versie word gemaakt in de eerste loop van het spel Tic Tac Toe
    # leaderboard_lists = [["TIC TAC TOE Leaderboard"],["#",f"{name_p1}", "Gelijkspel", f"{name_p2}"]]
    #Hier maak ik dus name_list aan door die te halen ui de leaderboard_lists
    name_list = current_leaderboard[1]
    # ik haal de namen uit de lijst en strip de whitespaces 
    name_1 = name_list[1].strip()
    name_2 = name_list[3].strip()
    # hier worden de integers win_counter gemaakt buiten de loop.
    win_counter_player_1 = 0
    win_counter_player_2 = 0
    # We gaan den per "row" in list current_leaderboards, row is een lijst
    for row in current_leaderboard:
        # ik check hier als de lengte van list row gelijk is aan 4 om de eerste row over te slaan omdat deze een len heeft van 1.
        # zonder deze stap is er een out of range error
        if len(row) == 4:
            #ik haal de status van elke ronde.
            status_player_1 = row[1].strip()
            status_player_2 = row[3].strip()
            # hier check ik of hij won of niet, als hij wint word int win_counter_player met 1 groter.
            if status_player_1 == "W":
                win_counter_player_1 += 1
            if status_player_2 == "W" :
                win_counter_player_2 += 1
    if win_counter_player_1 > win_counter_player_2:
        print(f"{name_1} is in the lead with {win_counter_player_1} wins!")
        print(f"{name_2} is behind with {win_counter_player_2} wins!")
    elif win_counter_player_2 > win_counter_player_1:
        print(f"{name_2} is in the lead with {win_counter_player_2} wins!")
        print(f"{name_1} is behind with {win_counter_player_1} wins!")
    else:
        print(f"You are both tied with {win_counter_player_1}!")        

# Deze funcite maakt onze leaderboard. Dit is een list van lists
def leaderboard_tic_tac_toe(player_list : list[str], game_count : int, is_winner : bool, current_leaderboard : list[list[str]]):
    # Current_leaderboard is een list van lists, de eerste versie word gemaakt in de eerste loop van het spel Tic Tac Toe
    # leaderboard_lists = [["TIC TAC TOE Leaderboard"],["#",f"{name_p1}", "Gelijkspel", f"{name_p2}"]]
    # Hier maak ik dus name_list aan door die te halen ui de leaderboard_lists
    name_list = current_leaderboard[1]
    name_1 = name_list[1].strip()
    name_2 = name_list[3].strip()
    #Als er iemand de ronde heeft gewonnen
    if is_winner == True:
        # player_list heeft als opmaak [naam_loser,naam_winnaar]
        winner = player_list[1]
        gelijkspel_status_string =  " "*(len("Gelijkspel"))
        if winner == name_1:
            # Hier worden de status strings aangemaakt, met whitespaces er bij om het overzichtelijker te maken.
            name_1_status_string = " "*(len(name_1)//2)+"W"+" "*(len(name_1)//2)
            name_2_status_string = " "*(len(name_2)//2)+"L"+" "*(len(name_2)//2)
            
        else:
            name_1_status_string = " "*(len(name_1)//2)+"L"+" "*(len(name_1)//2) # ik maak gebruik van // omdat ik integer nodig heb. Floats geven een error. 
            name_2_status_string = " "*(len(name_2)//2)+"W"+" "*(len(name_2)//2)
        # Deze worden dan in een mooi listje gestoken om later aan de leaderboard_lists toe te voegen.
        append_list = [f"{game_count}",name_1_status_string,gelijkspel_status_string,name_2_status_string]
    # Indien gelijkspel:
    else:
        # Whitespace strings voor speler 1 en 2
        name_1_status_string = " "*(len(name_1))
        name_2_status_string = " "*len(name_2)

        gelijkspel_status_string = " "*(len("Gelijkspel")//2)+"X"+" "*(len("Gelijkspel")//2)
        append_list = [f"{game_count}",name_1_status_string,gelijkspel_status_string,name_2_status_string]
    current_leaderboard.append(append_list)
    # blank lines om verwarring te voorkomen
    print(" ")
    print(" ")
    # Loopen door de current_leaderboard om deze lijn per lijn te printen
    for row in current_leaderboard:
        output_string = ""
        for item in row:
            output_string += item + " "
        print(output_string)
    # Lead counter word gecalled om de laatste lijn te printen.
    lead_counter(current_leaderboard)
    return current_leaderboard

# Dit is de gamelogic voor het 2 speler versie van Tic Tac Toe
def two_player_tic_tac_toe(game_count : int, player_list : list[str],current_leaderboard : list[list[str]]):
# Dictionary gebruikt omdat ik de key en de value nodig heb voor mijn spel.
    board = {
    "A1":" ",
    "B1":" ",
    "C1":" ",
    "A2":" ",
    "B2":" ",
    "C2":" ",
    "A3":" ",
    "B3":" ",
    "C3":" ",}
    boardgame_printer(board)
    turn = 1
    game_is_over = False
    while not game_is_over:
        # Ik gebruik hier % om makkelijk te checken wie zijn beurt het is. 
        player_turn = turn % 2
        player_name = player_list[player_turn]
        if player_turn == 1:
            symbol_player = "X"
        else:
            symbol_player = "O"
        input_player = input(f"{player_name} please input your move ({symbol_player}): ")
        input_player = input_player.upper()
        while not game_input_checker(input_player, board):
            input_player = input(f"{player_name} please input a valid move: ")
            input_player = input_player.upper()
        if player_turn == 1:
            # hier word de value van positie aangepast in het bordpsel
            board[input_player] = "X"
        else:
            board[input_player] = "O"
        turn += 1
        boardgame_printer(board)
        # Je kan pas winnen na turn 5.
        if turn > 5:
            game_is_over = winner_checker_tic_tac_toe(board)
        # Als je aan 10 geraakt betekent het gelijkspel
        if turn == 10:
            break           
    if game_is_over == "1":
        print(player_list[1], "heeft gewonnen!")
        is_winner = True
        winner = player_list [1]
        loser = player_list[0]
        player_list = [loser,winner]
    elif game_is_over == "0":
        print(player_list[0], "heeft gewonnen!")
        is_winner = True
        winner = player_list [0]
        loser = player_list[1]
        player_list = [loser,winner]
    else: 
        is_winner = False
        print("Het is gelijkspel!")
        #hier maken we gebruik van de random library om randomly speler 1 toe te wijzen
        randomnumber1 = random.randint(0,1)
        randomnumber2 = (randomnumber1 + 1) % 2
        player_1 = player_list[randomnumber1]
        player_2 = player_list[randomnumber2]
        player_list =  [player_2,player_1]
    current_leaderboard = leaderboard_tic_tac_toe(player_list,game_count,is_winner,current_leaderboard)
    # return list aangemaakt om makkelijker mee te werken
    return_list = [player_list,current_leaderboard]
    return return_list


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
# Kort tutorial hoe het spel werkt     
def tutorial_tic_tac_toe():
    board = {
    "A1":"A1",
    "B1":"B1",
    "C1":"C1",
    "A2":"A2",
    "B2":"B2",
    "C2":"C2",
    "A3":"A3",
    "B3":"B3",
    "C3":"C3",}
    slow_type("Welkom tot de tutorial")
    slow_type("Om tic tac toe te spelen moet je een coordinaat geven als input")
    slow_type("Dit zijn de geldige posities in het spel met de corresponderende positie in het bord")
    boardgame_printer(board)
    board = {
    "A1":"X",
    "B1":" ",
    "C1":" ",
    "A2":" ",
    "B2":" ",
    "C2":" ",
    "A3":" ",
    "B3":" ",
    "C3":" ",}
    slow_type("Dus als je linksboven iets wilt plaatsen zoals hieronder")
    boardgame_printer(board) 
    slow_type("Moet je als input A1 geven")
    slow_type("Hopelijk is het duidelijker nu, veel succes met de game!")
# Start Tic Tac Toe spel   
def Tic_Tac_Toe_start():
    game_count = 1
    extra_game = True
    player_count = int(is_count_valid())
    while extra_game:
        if player_count == 1:
            print("Het spel zal beginnen met 1 Speler")
            if game_count == 1:
                name_p1 = is_name_valid("player 1")
                tutorial_tic_tac_toe()
                name_p2 = "Mr. Robot"
                player_order_list =  [name_p2,name_p1]
                leaderboard_lists = [["TIC TAC TOE Leaderboard"],["#",f"{name_p1}", "Gelijkspel", f"{name_p2}"]]
            return_list = single_player_tic_tac_toe(game_count,player_order_list, leaderboard_lists)
            leaderboard_lists = return_list[1]           
        else:
            print("Het spel zal beginnen met 2 Spelers")
            if game_count == 1:
                name_p1 = is_name_valid("player 1")
                name_p2 = is_name_valid("player 2")
                tutorial_tic_tac_toe()
                # In de eerste ronde is speler 1 random>           
                player_list = [name_p2,name_p1]
                randomnumber1 = random.randint(0,1)
                randomnumber2 = (randomnumber1 + 1) % 2
                player_1 = player_list[randomnumber1]
                player_2 = player_list[randomnumber2]
                player_order_list =  [player_2,player_1]
                leaderboard_lists = [["TIC TAC TOE Leaderboard"],["#",f"{name_p1}", "Gelijkspel", f"{name_p2}"]]
            return_list = two_player_tic_tac_toe(game_count,player_order_list,leaderboard_lists)
            player_order_list = return_list[0]
            leaderboard_lists = return_list[1]
        extra_game = is_extra_game()
        if extra_game:
            game_count += 1

if __name__ == "__main__":
    Tic_Tac_Toe_start()