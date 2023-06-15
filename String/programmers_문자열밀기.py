# !/usr/bin/python3
# -*- coding: utf-8 -*-
# programmers 문자열 밀기

def solution(A, B):
    if A == B:
        return 0

    B = list(B)
    answer = 1

    for i in range(len(A)):
        B.append(B.pop(0))
        if "".join(B) == A:
            return answer
        else:
            answer += 1
    return -1