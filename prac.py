# !/usr/bin/env python
# -*- coding: utf8 -*-
# practice

def init(n):
    parent = [i for i in range(n + 1)]
    return parent

def find(x):
    global parent
    if parent[x] != x:
        return find(parent[x])
    else:
        return x

def union(x, y):
    global parent
    x = find(x)
    y = find(y)
    if x > y:
        parent[x] = y
        parent = [y if i == x else i for i in parent]
    else:
        parent[y] = x
        parent = [x if i == y else i for i in parent]

parent = init(6)
union(1, 2)
union(3, 4)
union(2, 3)
print(parent)