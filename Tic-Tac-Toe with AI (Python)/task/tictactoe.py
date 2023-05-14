import random
import ai


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


def menu(gm):
    if len(gm) != 3 or gm[0] not in possible_commands or gm[1] not in possible_commands or gm[
        2] not in possible_commands:
        return False

    global p1, p2

    p1 = gm[1]
    p2 = gm[2]
    print(p1, " ", p2)

    return True


def ai_move(symbol, level):
    if level == 'easy':
        print('Making move level "easy"')

        temp = ai.ai_easy(symbol, matrix)

    elif level == 'medium':
        print('Making move level "medium"')

        temp = ai.ai_medium(symbol, matrix)

    elif level == 'hard':
        print('Making move level "hard"')

        temp = ai.ai_hard(symbol, matrix)

    matrix[temp[0]][temp[1]] = symbol


def player_move(symbol1):
    global x, y, x_turn

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

                matrix[x - 1][y - 1] = symbol1
                break


if __name__ == '__main__':

    input_ = '               '
    matrix = [[input_[0], input_[1], input_[2]], [input_[3], input_[4], input_[5]],
              [input_[6], input_[7], input_[8]]]

    p1 = 'user'
    p2 = 'user'
    x_turn = 1
    continue_ = True
    possible_commands = ('start', 'end', 'easy', 'medium', 'hard', 'user')

    while continue_:
        while True:
            game_mode = input('Input command:').split()
            if game_mode[0] == 'exit':
                continue_ = False
                break

            if menu(game_mode):
                break
            else:
                print('Bad parameters!')

        if not continue_:
            break

        wyswietl(matrix)

        while True:

            if x_turn:
                if p1 == 'user':
                    player_move("X")
                else:
                    ai_move("X", p1)

            else:
                if p2 == 'user':
                    player_move("O")
                else:
                    ai_move("O", p2)


            wyswietl(matrix)

            x_turn = not x_turn

            if o_win(matrix):
                print("O wins")
                break
            elif x_won(matrix):
                print("X wins")
                break
            elif not is_finished(matrix):
                print("Draw")
                break

        x_turn = True
        matrix = [[input_[0], input_[1], input_[2]], [input_[3], input_[4], input_[5]],
                  [input_[6], input_[7], input_[8]]]
