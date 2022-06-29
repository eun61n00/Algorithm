# -*- coding: utf-8 -*-
# boj 2750 수 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
num_array = list()
for _ in range(n):
	num_array.append(int(input()))

for i in range(n):
	min_idx = i
	for j in range(i + 1, n):
		if num_array[j] < num_array[min_idx]:
			min_idx = j
	num_array[i], num_array[min_idx] = num_array[min_idx], num_array[i]

for num in num_array:
	print(num)