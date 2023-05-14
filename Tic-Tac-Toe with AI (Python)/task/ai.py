import random


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
