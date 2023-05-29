import random


def ai_move(board):
    table = []
    iterator = -1
    for element in board:
        iterator += 1
        if element == ' ':
            table.append(iterator)
    select_icon = random.choice(table)
    board[select_icon] = 'X'
    return board


def get_user_move(board):
    table = []
    iterator = -1
    for element in board:
        iterator += 1
        if element == ' ':
            table.append(iterator)
    while True:
        choice = input("Podaj numer gdzie chcesz wpisac: ")
        try:
            number = int(choice)

            if number in table:
                board[number] = 'O'
                return board
            else:
                print("Zjebales")

        except ValueError:
            print("Zjebales")


def is_player_starting():
    while True:
        name = input("Czy chcesz zaczynac, wpisz 1 jeśli tak, 2 jeśli nie, 3 jeśli chcesz wylosować: ")
        try:
            number = int(name)
            if number == 1:
                return True
            elif number == 2:
                return False
            elif number == 3:
                rand = random.randint(0, 1)
                if rand == 0:
                    return True
                else:
                    return False
            else:
                print("Zjebales")
        except ValueError:
            print("Zjebales")
