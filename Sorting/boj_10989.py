# -*- coding: utf-8 -*-
# boj 10989 수 정렬하기3

import sys
input = sys.stdin.readline

n = int(input())
table = [0] * 10001

for _ in range(n):
	num = int(input())
	table[num] += 1

for i in range(len(table)):
	for j in range(table[i]):
		print(i)