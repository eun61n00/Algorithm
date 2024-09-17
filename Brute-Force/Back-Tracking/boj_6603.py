# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 6603 로또


def backtracking(lst, idx):
    global sequence

    if len(lst) == 6:
        print(*lst)
    for i in range(idx + 1, len(sequence)):
        lst.append(sequence[i])
        backtracking(lst, i)
        lst.pop()


while True:
    sequence = list(map(int, input().split()))
    if sequence == [0]:
        break
    k = sequence.pop(0)
    backtracking([], -1)
    print()
