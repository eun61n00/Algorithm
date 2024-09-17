# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 16724 피리 부는 사나이

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(str, input().rstrip())))

# 방향 설정
movements = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
visited = [[False] * m for _ in range(n)]

def dfs(board, x, y, visited):
    global idx
    if x < 0 or y < 0 or x > n - 1 or y > m - 1:
        return 0

    if visited[x][y] != False:
        if visited[x][y] == idx:
            safe_zone.append((x, y))
        return 1

    visited[x][y] = idx
    dx, dy = movements[board[x][y]]
    nx, ny = x + dx, y + dy
    dfs(board, nx, ny, visited)

safe_zone = []
idx = 1
for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(board, i, j, visited)
            idx += 1

print(len(safe_zone))