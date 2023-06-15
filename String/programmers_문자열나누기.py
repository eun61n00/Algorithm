# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# programmers 문자열 나누기

def solution(s):
    answer = 0
    s = list(s)

    while s:
        x = s[0]
        x_cnt = 1
        y_cnt = 0
        for y in s[1:]:
            if y != x:
                y_cnt += 1
            else:
                x_cnt += 1
            if x_cnt == y_cnt:
                break
        s = s[x_cnt + y_cnt:]
        answer += 1

    return answer