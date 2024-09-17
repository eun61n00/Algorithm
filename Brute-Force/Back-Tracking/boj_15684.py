# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15684 사다리 조작

import sys
from copy import deepcopy


def print_ladders(ladders):
    for i in range(1, h + 1):
        print(ladders[i][1:])
    print()


n, m, h = map(int, input().split())
ladders = [[0] * (n + 1) for _ in range(h + 1)]

for i in range(m):  # 이미 그려진 가로선 정보
    a, b = map(int, input().split())
    ladders[a][b], ladders[a][b + 1] = (1, 0), (1, 1)


def ride(ladders, num):
    for i in range(1, h + 1):
        if ladders[i][num] == 0:
            continue
        else:
            if num == 1:  # 1번 사다리
                num += 1
            elif num == n:  # 끝 사다리
                num -= 1
            else:
                if ladders[i][num][1] == 0:
                    num += 1
                else:
                    num -= 1
    return num


def complete(ladders):
    for i in range(1, n + 1):
        if i != ride(ladders, i):
            return False
    return True


def dfs(ladders, depth, i, j):
    if complete(ladders):
        print(depth)
        exit(0)
    if depth == 3:  # 3개 모두 탐색 완료
        # print_ladders(ladders)
        return
    for c in range(j, n):
        for r in range(1, h + 1):
            if ride(ladders, c - 1) != c - 1:
                print(i, j, r, c)
                print_ladders(ladders)

                return
            if ladders[r][c] == 0 and ladders[r][c + 1] == 0:
                tmp = deepcopy(ladders)
                tmp[r][c], tmp[r][c + 1] = (1, 0), (1, 1)
                dfs(tmp, depth + 1, r, c)
                tmp = deepcopy(ladders)


dfs(ladders, 0, 1, 1)
print(-1)


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15684


input = sys.stdin.readline

N, M, H = map(int, input().split())

ladders = [[[0, 0] for _ in range(N + 1)] for _ in range(H + 1)]


def print_ladders(ladders):
    for i in range(len(ladders)):
        print(ladders[i])


def ride_ladder(ladders, n):
    for i in range(1, H + 1):
        if ladders[i][n][1] == 1:  # 오른쪽으로 옮기기
            n += 1
        elif ladders[i][n][0] == 1:
            n -= 1
    return n


def complete(ladders):
    for i in range(1, N + 1):
        if i != ride_ladder(ladders, i):
            return False
    return True


def dfs(ladders, y, x, cnt):
    if complete(ladders):
        print(cnt)
        exit
    if cnt >= 3:
        return -1
    for i in range(1, H + 1):
        for j in range(1, N):
            # (i, j)에서 가로선 그을 수 있음
            if ladders[i][j] == [0, 0] and ladders[i][j + 1] == [0, 0]:
                ladders[i][j][1], ladders[i][j + 1][0] = 1, 1
                dfs(ladders, i, j, cnt + 1)
    return cnt


for _ in range(M):
    a, b = map(int, input().split())
    ladders[a][b][1], ladders[a][b + 1][0] = 1, 1

print(dfs(ladders, 1, 1, 0))
