# -*- coding: utf-8 -*-
# Union Find Algorithm


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x, y):
	x = find(x)
	y = find(y)

	if x > y:
		parent[x] = y
	else:
		parent[y] = x

parent = []
for i in range(5):
	parent.append(i)

union(1, 4)
union(4, 2)

print(parent)