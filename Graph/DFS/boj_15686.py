# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15686 치킨 배달

from collections import deque

answer = 101 * 13


def chicken_distance(house, chickens):
    d = 101
    r1, c1 = house
    for chicken in chickens:
        r2, c2 = chicken
        d = min(abs(r1 - r2) + abs(c1 - c2), d)
    return d


def dfs(comb, depth, M):
    global answer
    if len(comb) == M:
        tmp = 0
        for house in houses:
            tmp += chicken_distance(house, comb)
        answer = min(tmp, answer)
        return comb
    elif depth == len(chickens):
        return

    comb.append(chickens[depth])
    dfs(comb, depth + 1, M)

    comb.pop()
    dfs(comb, depth + 1, M)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

chickens = [(i, j) for j in range(N) for i in range(N) if board[i][j] == 2]
houses = [(i, j) for j in range(N) for i in range(N) if board[i][j] == 1]

for i in range(1, M + 1):
    dfs(deque(), 0, i)  # 여기서 골라진 치킨집을 폐업시켜야 함

print(answer)
