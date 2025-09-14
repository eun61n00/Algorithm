# !/usr/bin/env python
# -*- coding: utf-8 -*-
# programmers 택배상자 꺼내기

from collections import deque
import math

# 시뮬레이션으로 풀이


def solution(n, w, num):
    answer = 0
    board = [[0] * w for _ in range(n // w + 1)]

    direction = 0
    i = 1
    for r in range(0, n // w + 1):
        if i > n:
            break
        if direction == 0:
            for c in range(0, w):
                board[r][c] = i
                if i == num:
                    answer = (c, r)
                i += 1
                if i > n:
                    break
        else:
            for c in range(w - 1, -1, -1):
                board[r][c] = i
                if i == num:
                    answer = (c, r)
                i += 1
                if i > n:
                    break
        direction = (direction + 1) % 2  # 방향 전환

    # 행, 열 바꾸기
    board = list(zip(*board))
    r, c = answer
    # print(board)
    t = list(board[r])
    if 0 in t:
        t.remove(0)

    return len(t) - c


# 수학적 계산으로 풀이
def solution2(n, w, num):
    row = (num - 1) // w
    total_row = (n - 1) // w
    if row % 2 == 0:
        col = (num % w) - 1
        if col < 0:
            col = w - 1
    else:
        col = w - (num % w)
        if col >= w:
            col = 0

    # (total_row, col)에 있는 상자번호 구하기
    s = w * total_row + 1  # 가장 맨 위 row에서 가장 작은 택배 상자
    # print(f"row: {row}, col: {col}")
    if total_row % 2 == 0:
        top_box_num = s + col
    else:
        top_box_num = s + (w - col - 1)
    # print("top_box_num: ", top_box_num)
    # print("total_row, row: ", total_row, " ", row)
    if top_box_num <= n:  # 맨 꼭대기까지 상자가 차있음
        answer = total_row - row + 1
    else:
        answer = total_row - row
    return answer
