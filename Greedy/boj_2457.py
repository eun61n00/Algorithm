# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 2457 공주님의 정원

import sys

input = sys.stdin.readline

n = int(input())
flowers = []
for _ in range(n):
    m1, d1, m2, d2 = map(int, input().split())
    flowers.append((m2, d2, m1, d1))
flowers.sort()

answer = 0
m, d = 3, 1

while m < 11 or (m == 11 and d <= 30):
    selected = None
    for flower in flowers:
        if (flower[2] < m or (flower[2] == m and flower[3] <= d)) and (flower[0] > m or (flower[0] == m and flower[1] > d)):
            selected = flower
    if selected is not None:
        answer += 1
        m, d = selected[0], selected[1]
    if selected == None:
        break

if m > 11:
    print(answer)
else:
    print(0)
