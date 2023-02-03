# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2493 탑

import sys

input = sys.stdin.readline

n = int(input().strip())
towers = list(map(int, input().split()))
towers.insert(0, 0)
tower_stack = []
result = []

for i in range(1, n + 1):
    while len(tower_stack) > 0:
        if tower_stack[-1][1] > towers[i]:
            result.append(tower_stack[-1][0])
            break
        else:
            tower_stack.pop(-1)
    if len(tower_stack) == 0:
        result.append(0)
    tower_stack.append((i, towers[i]))

print(*result)


# !시간초과
# for i in range(n, 0, -1):
#     for j in range(i, -1, -1):
#         if j == 0:
#             result.append(j)
#             break
#         if towers[j] > towers[i]:
#             result.append(j)
#             break
# print(*result[::-1])

