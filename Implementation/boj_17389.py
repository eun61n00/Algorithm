# /usr/bin/env python
# -*- coding: utf-8 -*-
# boj 17389 보너스 점수

N = int(input())
S = input()
bonus = 0
score = 0
for i, s in enumerate(S):
    if s == "O":
        score += i + 1 + bonus
        bonus += 1
    else:
        bonus = 0

print(score)