
import random

def ai_move(board):
    table = []
    iterator = -1
    for element in board:
        iterator += 1
        if element == " ":
            table.append(iterator)
    select_icon = random.choice(table)
    board[select_icon] = "X"
    return





def get_user_move(board):
    table = []
    iterator = -1
    for element in board:
        iterator += 1
        if element == " ":
            table.append(iterator)
    while True:
        wybor = input("Podaj numer gdzie chcesz wpisac: ")
        try:
            liczba = int(wybor)

            if liczba in table:
                board[liczba] = "O"
                return
            else:
                print("Zjebales")

        except ValueError:
            print("Zjebales")


def is_player_starting():
    while True:
        imie = input("Czy chcesz zaczynac, wpisz 1 jeśli tak, 2 jeśli nie, 3 jeśli chcesz wylosować: ")
        try:
            liczba = int(imie)
            if liczba == 1:
                return True
            elif liczba == 2:
                return False
            elif liczba ==3:
              rand =  random.randint(0, 1)
              if rand == 0:
                  return True
              else:
                  return False
            else:
                print("Zjebales")
        except ValueError:
            print("Zjebales")







