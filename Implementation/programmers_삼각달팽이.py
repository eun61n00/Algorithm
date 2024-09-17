# !/usr/bin/env python
#  -*- coding: utf-8 -*-
# programmers 삼각달팽이

dy = (1, 0, -1)
dx = (0, 1, -1)


def solution(n):
    answer = [[0] * n for _ in range(n)]
    y, x, d, cnt = 0, 0, 0, 0  # 현재 위치

    # 일단 한번은 n만큼 밑으로 내려가면서 숫자 채우기
    for i in range(1, n + 1):
        answer[y][x] = i
        y, x = y + dy[d], x + dx[d]
    cnt += (n + 1)
    y -= 1

    # n -> n - 1 -> ... -> 1 까지 방향 바꾸면서 채우기
    for i in range(n, 0, -1):
        d = (d + 1) % 3
        for j in range(i):
            print(f"d : {d}")
            y, x = y + dy[d], x + dx[d]
            print(f"y: {y}, x: {x}")
            answer[y][x] = cnt
            cnt += 1

    return answer


print(solution(4))
