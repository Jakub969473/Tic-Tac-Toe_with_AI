import random


def x_won(game):
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2] == "X":
            return True
        elif game[0][i] == game[1][i] == game[2][i] == "X":
            return True
    if game[0][0] == game[1][1] == game[2][2] == "X":
        return True
    if game[0][2] == game[1][1] == game[2][0] == "X":
        return True
    return False


def o_win(game):
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2] == "O":
            return True
        elif game[0][i] == game[1][i] == game[2][i] == "O":
            return True
    if game[0][0] == game[1][1] == game[2][2] == "O":
        return True
    if game[0][2] == game[1][1] == game[2][0] == "O":
        return True
    return False


def is_finished(game):
    for i in game:
        for j in i:
            for z in j:
                if z == " ":
                    return True
    return False


def wyswietl(game):
    print("---------")

    for i in game:
        wiersz = "| "
        for j in i:
            if j != "_":
                wiersz += j + " "
            else:
                wiersz += "  "
        print(wiersz + "|")

    print("---------")


def does_x_start(game):
    x_amount = 0
    o_amount = 0
    for i in game:
        for j in i:
            if j == 'X':
                x_amount += 1
            elif j == 'O':
                o_amount += 1

    if x_amount == o_amount:
        return True
    else:
        return False


input_ = "          "
matrix = [[input_[0], input_[1], input_[2]], [input_[3], input_[4], input_[5]],
          [input_[6], input_[7], input_[8]]]

wyswietl(matrix)

ai_turn = False

while True:
    if ai_turn:
        print('Making move level "easy"')
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        matrix[x][y] = "O"
        ai_turn = False

    else:
        while True:
            cords = input("Enter the coordinates: ").split()
            try:
                x = int(cords[0])
                y = int(cords[1])
            except ValueError:
                print("You should enter numbers!")
            else:

                if x > 3 or x < 1 or y > 3 or y < 1:
                    print("Coordinates should be from 1 to 3!")
                elif matrix[x - 1][y - 1] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    matrix[x - 1][y - 1] = "X"
                    ai_turn = True
                    break

    wyswietl(matrix)

    if o_win(matrix):
        print("O wins")
        break
    elif x_won(matrix):
        print("X wins")
        break
    elif not is_finished(matrix):
        print("Draw")
        break
