# !/usr/env/bin
# -*- coding: utf-8 -*-
# boj 14503

import sys
from collections import deque

input = sys.stdin.readline
dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

answer = 0
queue = deque([(r, c)])

while queue:
    y, x = queue.popleft()
    if board[y][x] == 0:
        answer += 1
        board[y][x] = 2

    # 4방향 확인
    cleaned = True
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if ny < 0 or nx < 0 or ny > n - 1 or nx > m - 1:
            continue
        if board[ny][nx] == 0:
            cleaned = False
            break

    if cleaned == True:
        ny, nx = y + dy[(d + 2) % 4], x + dx[(d + 2) % 4]  # 후진
        if ny > -1 or nx > -1 or ny < n or nx < m:
            if board[ny][nx] != 1:
                queue.append((ny, nx))

    else:
        find = False
        while not find:
            d = (d - 1) % 4
            ny, nx = y + dy[d], x + dx[d]
            if ny > -1 or nx > -1 or ny < n or nx < m:
                if board[ny][nx] == 0:
                    queue.append((ny, nx))
                    find = True

print(answer)


dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

queue = deque([(r, c)])   # 시작점
answer = 0


def out_of_range(y, x):
    # global N, M
    if y < 0 or x < 0 or y >= N or x > M:
        return True
    else:
        return False


while queue:
    y, x = queue.popleft()  # 현재 위치
    if board[y][x] == 0:     # 청소되지 않았다면
        board[y][x] = -1
        answer += 1

    # 주변에 청소되지 않은 칸이 있는지 검사
    for _ in range(4):
        d = (d - 1) % 4  # 반시계 방향으로 90도 회전
        ny, nx = y + dy[d], x + dx[d]
        if out_of_range(ny, nx):
            continue
        if board[ny][nx] == 0:
            queue.append((ny, nx))
            break

    if not queue:  # 주변이 모두 청소된 경우
        ny, nx = y + dy[(d - 2) % 4], x + dx[(d - 2) % 4]
        if not out_of_range(ny, nx) and board[ny][nx] == 1:  # 벽이면
            break
        else:
            queue.append((ny, nx))

print(answer)
