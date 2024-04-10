# !/usr/bin/env python
# -*-coding: utf-8-*-
# boj 21609 상어중학교

from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
answer = 0


def bfs(y, x):
    rainbow, common = 0, 0
    visited = [[False] * N for _ in range(N)]
    if board[y][x] == None or board[y][x] == -1:
        return ([], 0)
    queue = deque([(y, x)])
    visited[y][x] = True
    group = []
    origin_number = board[y][x]
    while queue:
        cy, cx = queue.popleft()
        group.append((cy, cx))
        if board[cy][cx] == 0:
            rainbow += 1
        elif board[cy][cx] > 0:
            common += 1
        for d in range(4):
            ny, nx = cy + dy[d], cx + dx[d]
            if ny < 0 or nx < 0 or ny >= N or nx >= N or visited[ny][nx] == True:
                continue
            if board[ny][nx] == origin_number or board[ny][nx] == 0:
                queue.append((ny, nx))
                visited[ny][nx] = True

    if len(group) < 2:
        return ([], rainbow)
    elif common < 1:
        return ([], rainbow)
    else:
        return (group, rainbow)


def gravity(board):
    for x in range(N):
        for y in range(N - 2, -1, -1):
            if board[y][x] is not None and board[y][x] >= 0:
                down = 1
                while y + down < N and board[y + down][x] == None:
                    down += 1
                board[y][x], board[y + down -
                                   1][x] = board[y + down - 1][x], board[y][x]
    return board


def rotate(board):
    rotated_board = [[] for _ in range(N)]
    for i in range(N):
        rotated_board[N - i - 1] = [board[x][i] for x in range(N)]
    return rotated_board


def find_block_groups(board):
    groups = []
    for y in range(N):
        for x in range(N):
            # group = sorted(bfs(y, x))
            group, rainbow = bfs(y, x)
            if group and group not in groups:
                groups.append([rainbow, group])
    return groups


# 모든 칸을 돌면서 블록 그룹을 찾는다
groups = find_block_groups(board)
while groups:
    groups.sort(key=lambda x: (len(x[1]), x[0],
                x[1][0], x[1][1]), reverse=True)
    answer += len(groups[0][1]) ** 2
    for y, x in groups[0][1]:
        board[y][x] = None  # 블록 제거

    board = gravity(rotate(gravity(board)))
    groups = find_block_groups(board)


print(answer)
