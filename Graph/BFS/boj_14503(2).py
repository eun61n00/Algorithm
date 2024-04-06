# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 14503 로봇청소기

from collections import deque

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
