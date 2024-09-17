# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 15663

from copy import deepcopy

n, m = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort()
sequences = []


def backtracking(sequence, visited):
    global sequences
    if len(sequence) == m:
        print(*sequence)
        return

    for i in range(n):
        if not visited[num_list[i]]:  # 자식 노드들을 생성할 때 같은 자식이 생기지 않도록 검사
            sequence.append(num_list[i])
            visited[num_list[i]] = True
            backtracking(sequence, visited)
            sequence.pop()
            visited[i] = False


for num in sorted(list(set(num_list))):
    visited = [False] * 10001
    visited[num] = True
    backtracking([num], visited)
