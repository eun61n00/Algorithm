# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14500

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
max_value = 0
for i in range(n):
    board.append(list(map(int, input().split())))
    max_value = max(max_value, max(board[i]))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

start = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == max_value:
            start.append((i, j))


def dfs(board, y, x, visited, values, lst):
    global answer

    if len(values) == 4:
        answer = max(answer, sum(values))
        return

    if len(values) == 3 and lst[0][0] == lst[1][0] == lst[2][0]:
        ny, nx = lst[1][0] + 1, lst[1][1]
        if not (ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1) and not visited[ny][nx]:
            visited[ny][nx] = True
            values.append(board[ny][nx])
            lst.append((ny, nx))
            print(lst)
            dfs(board, ny, nx, visited, values, lst)
            visited[ny][nx] = False
            values.pop()
            lst.pop()

        ny, nx = lst[1][0] - 1, lst[1][1]
        if not (ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1) and not visited[ny][nx]:
            visited[ny][nx] = True
            values.append(board[ny][nx])
            lst.append((ny, nx))
            print(lst)
            dfs(board, ny, nx, visited, values, lst)
            visited[ny][nx] = False
            values.pop()
            lst.pop()

    elif len(values) == 3 and lst[0][1] == lst[1][1] == lst[2][1]:
        ny, nx = lst[1][0], lst[1][1] + 1
        if not (ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1) and not visited[ny][nx]:
            visited[ny][nx] = True
            values.append(board[ny][nx])
            lst.append((ny, nx))
            print(lst)
            dfs(board, ny, nx, visited, values, lst)
            visited[ny][nx] = False
            values.pop()
            lst.pop()

        ny, nx = lst[1][0], lst[1][1] - 1
        if not (ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1) and not visited[ny][nx]:
            visited[ny][nx] = True
            values.append(board[ny][nx])
            lst.append((ny, nx))
            print(lst)
            dfs(board, ny, nx, visited, values, lst)
            visited[ny][nx] = False
            values.pop()
            lst.pop()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1:
            continue
        if not visited[ny][nx]:
            visited[ny][nx] = True
            values.append(board[ny][nx])
            lst.append((ny, nx))
            dfs(board, ny, nx, visited, values, lst)
            visited[ny][nx] = False
            values.pop()
            lst.pop()


answer = 0
for s in start:
    y, x = s
    visited = [[False] * m for _ in range(n)]
    visited[y][x] = True
    dfs(board, y, x, visited, [board[y][x]], [(y, x)])

print(answer)

shape = [[[1, 1, 1], [0, 1, 0]], [[0, 1, 0], [1, 1, 1]],
         [[1, 0], [1, 1], [1, 0]], [[0, 1], [1, 1], [0, 1]]]
