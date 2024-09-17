# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 12100 2048(Easy)

from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# up, right, down, left
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)


def move(board, merged, direction, y, x):
    if board[y][x] == 0:  # 옮길게 없음
        return board, merged
    ny, nx = y, x
    while True:
        ny += dy[direction]
        nx += dx[direction]
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            break
        elif board[ny][nx] == board[y][x] and not merged[ny][nx]:  # 합쳐짐
            board[ny][nx] += board[y][x]
            board[y][x] = 0
            merged[ny][nx] = True
            break
        elif board[ny][nx] == 0:  # 옮겨감
            board[ny][nx] = board[y][x]
            board[y][x] = 0
            y, x = ny, nx
        elif board[ny][nx] != board[y][x]:
            break
    return board, merged


def discover(board, direction):
    merged = [[False] * n for _ in range(n)]
    if direction == 0 or direction == 3:
        for y in range(n):
            for x in range(n):
                board, merged = move(board, merged, direction, y, x)
    elif direction == 1:
        for y in range(0, n):
            for x in range(n - 1, -1, -1):
                board, merged = move(board, merged, direction, y, x)
    elif direction == 2:
        for y in range(n - 1, -1, -1):
            for x in range(n):
                board, merged = move(board, merged, direction, y, x)


def dfs(board, depth):
    global answer
    if depth == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    for direction in range(4):
        tmp = deepcopy(board)
        discover(tmp, direction)
        # print(f"depth: {depth}, direction: {direction}")
        # for i in range(n):
        #     print(tmp[i])
        # print()
        # if depth == 1:
        #     break
        dfs(tmp, depth + 1)
        tmp = deepcopy(board)


answer = 0
dfs(board, 0)
print(answer)
