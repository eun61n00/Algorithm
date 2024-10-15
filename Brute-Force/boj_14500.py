# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14500 테트로미노

import sys
from typing import List

input = sys.stdin.readline

N, M = map(int, input().split())
answer = 0
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

tetrominoes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 1, 1], [0, 1, 0]]
]


def rotate(tetromino: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in zip(*tetromino[::-1])]


for tetromino in tetrominoes:
    for _ in range(4):
        tetromino = rotate(tetromino)
        n, m = len(tetromino), len(tetromino[0])
        for i in range(N - n + 1):
            for j in range(M - m + 1):
                s = 0
                for x in range(n):
                    for y in range(m):
                        s += board[i + x][j + y] * tetromino[x][y]
                answer = max(answer, s)

print(answer)
