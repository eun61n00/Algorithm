# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# programmers 숨어있는 숫자의 덧셈

def solution(my_string):
    answer = 0

    tmp = ""
    for str in my_string:
        if str.isalpha() and tmp != "":
            answer += int(tmp)
            tmp = ""
        elif str.isalpha() == False:
            tmp += str

    return answer