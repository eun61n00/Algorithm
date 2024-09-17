# -*- coding: utf-8 -*-
# Union Find Algorithm


def init(n):
	parent = [i for i in range(n)]
	return parent

def find(x):
	if x != parent[x]:
		parent[x] = find(parent[x])
		return parent[x]
	return x

def union(x, y):
	x = find(x)
	y = find(y)

	if x > y:
		parent[x] = y
	else:
		parent[y] = x

parent = init(10)

union(1, 2)
union(2, 3)
union(3, 4)

print(parent)