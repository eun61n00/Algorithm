# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1149 RGB

import sys

input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

table = [[0] * 3 for _ in range(n)]
table[0] = costs[0]

for i in range(1, n):
    prev_red = table[i - 1][0]
    prev_green = table[i - 1][1]
    prev_blue = table[i - 1][2]
    red, green, blue = costs[i][0], costs[i][1], costs[i][2]
    table[i][0] = min(prev_green + red, prev_blue + red)
    table[i][1] = min(prev_red + green, prev_blue + green)
    table[i][2] = min(prev_red + blue, prev_green + blue)

print(min(table[n - 1]))
