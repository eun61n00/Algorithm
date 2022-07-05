# -*- coding: utf-8 -*-
# boj 1976 여행 가자

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i+1 for i in range(n)]

def find(x):
	if x != parent[x]:
		parent[x] = find(parent[x])
		return parent[x]
	return parent[x]