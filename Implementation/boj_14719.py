# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14719 빗물

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
blocks = list(map(int, input().split()))
map = [[0 for _ in range(c)] for __ in range(r)]

j = 0
for block in blocks:
    i = r - 1
    for _ in range(block):
        map[i][j] = 1
        i -= 1
    j += 1

walls = []
result = 0

for row in map:
    wall = []
    start = 0
    end = c - 1
    if row.count(1) < 2:
        continue
    walls.append([i for i in range(len(row)) if row[i] == 1])

for wall in walls:
    for i in range(len(wall) - 1):
        result += wall[i + 1] - wall[i] - 1

print(result)
