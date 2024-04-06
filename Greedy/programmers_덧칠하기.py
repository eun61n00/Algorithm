# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 덧칠하기

def solution(n, m, section):
    answer = 0
    complete = [False] * 200000

    for s in section:
        if complete[s] == False:
            answer += 1
            for i in range(m):
                complete[i + s] = True

    return answer
