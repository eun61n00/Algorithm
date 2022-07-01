# -*- coding: utf-8 -*-
# boj 4195 친구 네트워크

import sys
input = sys.stdin.readline

test_case = int(input())

def find(x):
	if x != parent[x]:
		parent[x] = find(parent[x])
		return parent[x]
	return parent[x]


def union(x, y):
	x = find(x)
	y = find(y)
	if x != y:
		parent[y] = x
		network_size[x] += network_size[y]


for _ in range(test_case):
	parent = dict()
	network_size = dict()

	f = int(input())
	for __ in range(f):
		x, y = input().strip().split(' ')

		if x not in parent:
			parent[x] = x
			network_size[x] = 1
		if y not in parent:
			parent[y] = y
			network_size[y] = 1

		union(x, y)
		print(network_size[find(x)])