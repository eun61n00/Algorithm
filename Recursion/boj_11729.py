# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 11729 하노이탑

n = int(input())

count = 0
movements = []


def hanoi(n, a, b):
    if n == 1:
        movements.append((a, b))
        return
    hanoi(n-1, a, 6-a-b)
    movements.append((a, b))
    hanoi(n-1, 6-a-b, b)


hanoi(n, 1, 3)
print(len(movements))
for move in movements:
    print(*move)
