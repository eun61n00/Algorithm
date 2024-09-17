# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15652 N과 M(4)

n, m = map(int, input().split())


def backtracking(sequence, idx):
    global n, m

    if len(sequence) == m:
        print(*sequence)
        return

    for i in range(idx, n + 1):
        sequence.append(i)
        backtracking(sequence, i)
        sequence.pop()


backtracking([], 1)
