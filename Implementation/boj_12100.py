# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 12100 2048(Easy)

from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# up, right, down, left
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def move(board, direction):
    y_start, x_start = 0, 0
    if direction == 0 or direction == 3:
        y_start, x_start, y_d, x_d, s = 0, 0, 1, 1, n
    elif direction == 1:
        y_start, x_start, y_d, x_d, s = 0, n - 1, 1, -1, n - 2
    elif direction == 2:
        y_start, x_start, y_d, x_d, s = n - 1, 0, -1, 1, n - 2
    for y in range(y_start, s - y_start, y_d):
        for x in range(x_start, s - x_start, x_d):
            ny, nx = y + dy[direction], x + dx[direction]  # 옮겨지거나 합쳐질 위치
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            elif board[ny][nx] == board[y][x]:  # 합쳐짐
                board[ny][nx] += board[y][x]
                board[y][x] = 0
            elif board[ny][nx] == 0:  # 옮겨감
                board[ny][nx] = board[y][x]
                board[y][x] = 0


def dfs(board, depth):
    global answer
    if depth == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    for direction in range(4):
        tmp = deepcopy(board)
        move(tmp, direction)
        print(f"depth: {depth}, direction: {direction}")
        for i in range(n):
            print(tmp[i])
        print()
        if depth == 1:
            break
        dfs(tmp, depth + 1)
        tmp = deepcopy(board)


answer = 0
dfs(board, 0)
print(answer)
