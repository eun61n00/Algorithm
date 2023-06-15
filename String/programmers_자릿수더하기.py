# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# programmers 자릿수 더하기

def solution(n):
    answer = 0

    for i in list(str(n)):
        answer += int(i)

    return answer