# coding: utf-8
import re
#返回words集合里面的元素在text中出现的次数
def count_words(text, words):
    c = 0
    for a in words:
        if re.search(a,text.lower()):
            c += 1
    return c

def checkio4(game_result):
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

def checkio1(text):
    #检查字符串中出现的字母的次数，列出出现次数最多的那个，如果有相同次数的，列出字母顺序表靠前的那个
    text1 = text.replace(' ','').replace('?','').replace('!','').lower()
    text1 = text1.replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','')
    text1 = text1.replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace(',', '').replace('.', '')
    x = {i:text1.count(i) for i in set(text1)}
    a = sorted(x.items(),key=lambda y: y[0],reverse=False)
    b = max(y for y in x.values())
    for c in a:
        if b in c:
            break
    return c[0]

def checkio2(data):
    #检查并删除列表中只出现一次的元素又不改变列表的排序
    data1=data.copy()
    for x in data1:
        if data.count(x) < 2:
            data.remove(x)



    #replace this for solution
    return data

import re
def checkio3(data):
    #检查字符串（密码）强度 同时包含 大小写字母和数字的为真
    w = re.search('[0-9]',data)
    l = re.search('[a-z]',data)
    u = re.search('[A-Z]',data)
    if len(data) > 9 and l and w and u:
        return True
    else:
        return False
