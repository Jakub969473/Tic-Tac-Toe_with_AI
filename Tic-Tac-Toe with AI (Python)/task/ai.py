import random


class Move:
    def __init__(self):
        self.score = int(0)
        self.index = []

    def get_score(self):
        return self.score

    def __str__(self):
        return f'{self.score} {self.index}'


def ai_easy(symbol, matrix):
    global x, y, x_turn

    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)

        if matrix[x][y] == " ":
            break

    return (x, y)


def ai_medium(symbol, matrix):
    global x, y, x_turn

    cords = two_in_row(symbol, matrix)

    if cords is None:
        if symbol == 'X':
            cords = two_in_row('O', matrix)
        else:
            cords = two_in_row('X', matrix)

    if cords is not None:

        if matrix[cords[0][0]][cords[0][1]] == matrix[cords[1][0]][cords[1][1]]:

            return cords[2]

        elif matrix[cords[0][0]][cords[0][1]] == matrix[cords[2][0]][cords[2][1]]:

            return cords[1]

        elif matrix[cords[1][0]][cords[1][1]] == matrix[cords[2][0]][cords[2][1]]:

            return cords[0]
    else:
        return ai_easy(symbol, matrix)


def two_in_row(symbol, matrix):
    cords = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
    )

    for i in cords:
        if [matrix[i[0][0]][i[0][1]], matrix[i[1][0]][i[1][1]], matrix[i[2][0]][i[2][1]]].count(symbol) == 2:
            if [matrix[i[0][0]][i[0][1]], matrix[i[1][0]][i[1][1]], matrix[i[2][0]][i[2][1]]].count(' ') > 0:
                return i
        elif [matrix[i[0][1]][i[0][0]], matrix[i[1][1]][i[1][0]], matrix[i[2][1]][i[2][0]]].count(symbol) == 2:
            if [matrix[i[0][1]][i[0][0]], matrix[i[1][1]][i[1][0]], matrix[i[2][1]][i[2][0]]].count(' ') > 0:
                return ((i[0][1], i[0][0]), (i[1][1], i[1][0]), (i[2][1], i[2][0]))

    if [matrix[0][0], matrix[1][1], matrix[2][2]].count(symbol) == 2:
        if [matrix[0][0], matrix[1][1], matrix[2][2]].count(' ') > 0:
            return ((0, 0), (1, 1), (2, 2))
    elif [matrix[0][2], matrix[1][1], matrix[2][0]].count(symbol) == 2:
        if [matrix[0][2], matrix[1][1], matrix[2][0]].count(' ') > 0:
            return ((0, 2), (1, 1), (2, 0))


def ai_hard(symbol, matrix):
    if symbol == 'O':
        move = minimax(matrix, symbol, 'X', 'O')
    else:
        move = minimax(matrix, symbol, 'O', 'X')

    return [move.index[0], move.index[1]]


def winning(game, symbol):
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2] == symbol:
            return True
        elif game[0][i] == game[1][i] == game[2][i] == symbol:
            return True
    if game[0][0] == game[1][1] == game[2][2] == symbol:
        return True
    if game[0][2] == game[1][1] == game[2][0] == symbol:
        return True
    return False


def empty_indexies(matrix):
    empty = []
    for row in range(0, 3):
        for column in range(0, 3):
            if matrix[row][column] == " ":
                empty.append([row, column])
    return empty


def minimax(newBoard, symbol, p1, p2):
    avail_spots = empty_indexies(newBoard)

    if winning(newBoard, p2):
        return -10
    elif winning(newBoard, p1):
        return 10
    elif len(avail_spots) == 0:
        return 0

    moves = []

    for i in avail_spots:
        move = Move()
        move.index = i

        newBoard[i[0]][i[1]] = symbol

        if symbol == p1:
            result = minimax(newBoard, p2, p1, p2)
        else:
            result = minimax(newBoard, p1, p1, p2)

        if isinstance(result, int):
            move.score = result
        else:
            move.score = result.score

        newBoard[i[0]][i[1]] = ' '

        moves.append(move)

    best_move = 0
    if symbol == p1:
        best_score = -1000000
        for j in moves:
            test = int(str(j.get_score()))
            if test > best_score:
                best_score = test
                best_move = j
    else:
        best_score = 1000000
        for j in moves:
            test = j.score
            if test < best_score:
                best_score = test
                best_move = j

    return best_move

