# !/usr/bin/env python
# -*- coding: utf-8 -*-
# BOJ 1717 집합의 표현

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n + 1)]


def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
