# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15656


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()


def backtracking(sequence):
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(n):
        sequence.append(num_list[i])
        backtracking(sequence)
        sequence.pop()


backtracking([])
