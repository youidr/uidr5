# coding: utf-8
import re
#返回words集合里面的元素在text中出现的次数
def count_words(text, words):
    c = 0
    for a in words:
        if re.search(a,text.lower()):
            c += 1
    return c
