# !/usr/bin/python3
# -*- coding: utf-8 -*-
# programmers 문자열 계산하기

def solution(my_string):
    str = my_string.split(" ")
    answer = int(str.pop(0))
    while str:
        tmp = str.pop(0)
        if tmp == "+":
            answer += int(str.pop(0))
        elif tmp == "-":
            answer -= int(str.pop(0))
    return answer