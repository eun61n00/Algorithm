# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# programmers 인덱스 바꾸기

def solution(my_string, num1, num2):
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return "".join(my_string)