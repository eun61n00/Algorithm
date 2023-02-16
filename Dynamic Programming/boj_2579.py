# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2579 계단 오르기

n = int(input())

stairs = []
for i in range(n):
    stairs.append(int(input()))

dp_one_step, dp_two_step = [0 for _ in range(n)], [0 for _ in range(n)]

dp_one_step[0] = stairs[0]
dp_two_step[0] = 0

dp_one_step[1] = stairs[0] + stairs[1]
dp_two_step[1] = stairs[1]

for i in range(2, n):
    dp_one_step[i] = dp_two_step[i - 1] + stairs[i]
    dp_two_step[i] = dp_one_step[i - 2] + stairs[i]

print(max(dp_one_step[i], dp_two_step[i]))