# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15651 N과 M(3)

from itertools import product

n, m = map(int, input().split())


# product 모듈을 이용한 풀이
for prod in product(range(1, n + 1), repeat=m):
    print(*prod)


# backtracking을 이용한 풀이
def backtracking(sequence):
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(1, n + 1):
        sequence.append(i)
        backtracking(sequence)
        sequence.pop()


backtracking([])
