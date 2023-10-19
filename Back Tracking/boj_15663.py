# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15663

from copy import deepcopy

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
sequences = []


def backtracking(sequence):
    global sequences
    if len(sequence) == m:
        print(*sequence)
        return

    lst = []
    for i in range(n):
        if num_list[i] not in lst and num_list[i] not in sequence:
            lst.append(num_list[i])
            sequence.append(num_list[i])
            backtracking(sequence)
            sequence.pop()


backtracking([])
