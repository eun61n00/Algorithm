# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15684 사다리 조작

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
    # num번째 세로선 사다리 타기
    # if num == 0:
    #     return True
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
        print_ladders(ladders)
        return
    for c in range(j, n):
        for r in range(1, h + 1):
            # if i == 1 and j == 3:
            #     print_ladders(ladders)
            if ride(ladders, c - 1) != c - 1:
                return
            if ladders[r][c] == 0 and ladders[r][c + 1] == 0:
                tmp = deepcopy(ladders)
                tmp[r][c], tmp[r][c + 1] = (1, 0), (1, 1)
                dfs(tmp, depth + 1, r, c)
                tmp = deepcopy(ladders)

    # for r in range(i, h + 1):
    #     if r == i:
    #         for c in range(j, n):
    #             if ladders[r][c] == 0 or ladders[r][c + 1] == 0 and ladders[r][c - 1] == 0:
    #                 tmp = deepcopy(ladders)
    #                 tmp[r][c], tmp[r][c + 1] = (1, 0), (1, 1)
    #                 dfs(tmp, depth + 1, r, c)
    #                 tmp = deepcopy(ladders)
    #     else:
    #         for c in range(1, n):
    #             if ladders[r][c] == 0 or ladders[r][c + 1] == 0 and ladders[r][c - 1] == 0:
    #                 tmp = deepcopy(ladders)
    #                 tmp[r][c], tmp[r][c + 1] = (1, 0), (1, 1)
    #                 dfs(tmp, depth + 1, r, c)
    #                 tmp = deepcopy(ladders)


dfs(ladders, 0, 1, 1)
print(-1)
