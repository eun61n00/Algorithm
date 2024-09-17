# !/usr/bin/env python
# -*- coding: utf-8
# boj 14888 연산자 끼워넣기

import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))

add, subtract, multiple, divide = map(int, input().split())


# 완전탐색 풀이
operator_list = ["+" for _ in range(add)] + ["-" for _ in range(subtract)] + [
    "*" for _ in range(multiple)] + ["/" for _ in range(divide)]

results = []

for p in permutations(operator_list, n - 1):
    result = sequence[0]
    for idx, op in enumerate(p):
        if op == "+":
            result += sequence[idx + 1]
        elif op == "-":
            result -= sequence[idx + 1]
        elif op == "*":
            result *= sequence[idx + 1]
        else:
            if result < 0:
                result = (result * -1 // sequence[idx + 1]) * -1
            else:
                result = result // sequence[idx + 1]
    results.append(result)

print(max(results))
print(min(results))


maximum = -1000000001
minimum = 1000000001


# DFS 풀이
def dfs(res, depth, add, subtract, multiple, divide):
    global maximum, minimum

    if depth == n:
        maximum = max(maximum, res)
        minimum = min(minimum, res)
        return

    if add:
        dfs(res + sequence[depth], depth + 1,
            add - 1, subtract, multiple, divide)
    if subtract:
        dfs(res - sequence[depth], depth + 1,
            add, subtract - 1, multiple, divide)
    if multiple:
        dfs(res * sequence[depth], depth + 1,
            add, subtract, multiple - 1, divide)
    if divide:
        if res > 0:
            dfs(res//sequence[depth], depth + 1,
                add, subtract, multiple, divide - 1)
        else:
            dfs((res * (-1) // sequence[depth]) * (-1),
                depth + 1, add, subtract, multiple, divide - 1)


dfs(sequence[0], 1, add, subtract, multiple, divide)
print(maximum)
print(minimum)
