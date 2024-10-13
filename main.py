'''A Tic Tac Toe game that allows user to play the game against an AI player.'''

import random
import time

list_index = [0, 1, 2]
position_index = [1, 5, 9]
winner_identified = False
game_on = True


def layout(list):
    for index, value in enumerate(list):
        if index == 10:
            print(value)
        else:
            print(value, end="")


def show_gameboard():
    layout(list_1)
    layout(list_2)
    layout(list_3)
    layout(list_4)
    layout(list_5)


def get_list():
    list_to_update = input("\nwhich line would you like to place 'x' at? (input 1, 2 or 3) ")
    if list_to_update == "1":
        return list_1
    elif list_to_update == "2":
        return list_3
    elif list_to_update == "3":
        return list_5
    else:
        print("this line does not exist, please input another line")
        return get_list()


def get_index():
    index = input("\nwhich position in this line would you like to place 'x' at? (input 1, 2 or 3) ")
    if index == "1":
        return 1
    elif index == "2":
        return 5
    elif index == "3":
        return 9
    else:
        print("this position does not exist, please input another position")
        return get_index()


def player_move():
    global list_1, list_2, list_3, list_4, list_5
    list_to_update = get_list()
    index_to_update = get_index()
    if list_to_update[index_to_update] == " ":
        list_to_update[index_to_update] = "x"
    else:
        print("this position has already been occupied, please pick another position")
        player_move()


def opponent_move():
    global list_1, list_2, list_3, list_4, list_5
    list_to_update = changeable_lists[random.choice(list_index)]
    index_to_update = random.choice(position_index)
    if list_to_update[index_to_update] == " ":
        list_to_update[index_to_update] = "o"
        print("\nyour opponent has made a move, now it is your turn")
    else:
        opponent_move()


def same_vertical_elements(n):
    if list_1[n] != " " and list_1[n] == list_3[n] == list_5[n]:
        return True
    else:
        return False


def same_cross_elements():
    if list_3[5] != " " and list_1[1] == list_3[5] == list_5[9]:
        return True
    elif list_3[5] != " " and list_1[9] == list_3[5] == list_5[1]:
        return True
    else:
        return False


def same_horizontal_elements(n):
    if changeable_lists[n][1] != " " and changeable_lists[n][1] == changeable_lists[n][5] == changeable_lists[n][9]:
        return True
    else:
        return False


def check_game_result(m, n):
    if changeable_lists[m][n] == "x":
        print("you win!")
    else:
        print("sorry, you lose:(")


def new_game():
    global game_on, winner_identified
    continue_game = input("\nwould you like to go again? input Y for 'yes' and N for 'no' ")
    print("\n")
    if continue_game == "N":
        game_on = False
        print("I am sorry to see you go, hope you had fun!")
    elif continue_game == "Y":
        pass
    else:
        print("sorry, but this is not an acceptable input, please try again")
        new_game()


def check_game_status():
    global game_on, winner_identified
    if same_vertical_elements(1) or same_vertical_elements(5) or same_vertical_elements(9):
        if same_vertical_elements(1):
            check_game_result(0, 1)
        elif same_vertical_elements(5):
            check_game_result(0, 5)
        else:
            check_game_result(0, 9)
        winner_identified = True
        new_game()

    elif same_horizontal_elements(0) or same_horizontal_elements(1) or same_horizontal_elements(2):
        if same_horizontal_elements(0):
            check_game_result(0, 1)
        elif same_horizontal_elements(1):
            check_game_result(1, 1)
        else:
            check_game_result(2, 1)
        winner_identified = True
        new_game()

    elif same_cross_elements():
        if list_3[5] == "x":
            print("you win!")
        else:
            print("sorry, you lose:(")
        winner_identified = True
        new_game()
    else:
        pass


while game_on:
    list_1 = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
    list_2 = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    list_3 = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
    list_4 = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    list_5 = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
    changeable_lists = [list_1, list_3, list_5]
    print("Welcome to Tic Tac Toe, be ready to wrestle your mind!")
    show_gameboard()
    winner_identified = False
    while not winner_identified:
        player_move()
        show_gameboard()
        check_game_status()
        if not winner_identified:
            time.sleep(2)
            opponent_move()
            show_gameboard()
            check_game_status()
