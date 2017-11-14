# coding: utf-8
import re
#返回words集合里面的元素在text中出现的次数
def count_words(text, words):
    c = 0
    for a in words:
        if re.search(a,text.lower()):
            c += 1
    return c

def checkio1(game_result):
    #三子棋比输赢
    if game_result[0][0] == "X" and game_result[0][1] == "X" and game_result[0][2] == "X" \
            or game_result[1][0] == "X" and game_result[1][1] == "X" and game_result[1][2] == "X" \
            or game_result[2][0] == "X" and game_result[2][1] == "X" and game_result[2][2] == "X" \
            or game_result[0][0] == "X" and game_result[1][0] == "X" and game_result[2][0] == "X" \
            or game_result[0][1] == "X" and game_result[1][1] == "X" and game_result[2][1] == "X" \
            or game_result[0][2] == "X" and game_result[1][2] == "X" and game_result[2][2] == "X" \
            or game_result[0][0] == "X" and game_result[1][1] == "X" and game_result[2][2] == "X" \
            or game_result[0][2] == "X" and game_result[1][1] == "X" and game_result[2][0] == "X":
        return 'X'
    elif game_result[0][0] == "O" and game_result[0][1] == "O" and game_result[0][2] == "O" \
            or game_result[1][0] == "O" and game_result[1][1] == "O" and game_result[1][2] == "O" \
            or game_result[2][0] == "O" and game_result[2][1] == "O" and game_result[2][2] == "O" \
            or game_result[0][0] == "O" and game_result[1][0] == "O" and game_result[2][0] == "O" \
            or game_result[0][1] == "O" and game_result[1][1] == "O" and game_result[2][1] == "O" \
            or game_result[0][2] == "O" and game_result[1][2] == "O" and game_result[2][2] == "O" \
            or game_result[0][0] == "O" and game_result[1][1] == "O" and game_result[2][2] == "O" \
            or game_result[0][2] == "O" and game_result[1][1] == "O" and game_result[2][0] == "O":
        return 'O'
    else:
        return "D"

