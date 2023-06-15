# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# programmers OX퀴즈

def solution(quizes):
    answer = []

    for quiz in quizes:
        x, op, y, equals, z = quiz.split(" ")
        if op == "+":
            if int(x) + int(y) == int(z):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(x) - int(y) == int(z):
                answer.append("O")
            else:
                answer.append("X")
    return answer