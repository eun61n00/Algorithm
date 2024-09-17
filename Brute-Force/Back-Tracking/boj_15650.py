# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15650 N과 M(2)

from itertools import combinations

# 라이브러리를 이용한 풀이
n, m = map(int, input().split())
for combination in combinations(range(1, n + 1), m):
    print(*combination)


# backtracking을 이용한 풀이
def backtracking(sub_sequence, idx):
    # print(f"back_tracking({sub_sequence}, {idx})")
    if len(sub_sequence) == m:
        print(*sub_sequence)
        return
    for i in range(idx + 1, n + 1):
        sub_sequence.append(i)
        backtracking(sub_sequence, i)
        sub_sequence.pop()


backtracking([], 0)
