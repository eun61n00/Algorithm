# -*- coding: utf-8 -*-

import sys
input = sys.stdin.readline

n = int(input())
lines = list()

for _ in range(n):
	lines.append(input().strip())

n_research = int(input())
for _ in range(n_research):
	research = input().strip()
	cnt_dict = dict()
	for line in lines:
		if line[:len(research)] == research:
			if line in cnt_dict.keys():
				cnt_dict[line] += 1
			else:
				cnt_dict[line] = 1

	cnt_dict = dict(sorted(cnt_dict.items(), key = lambda item: (-item[1], item[0]), reverse=False))

if len(cnt_dict) == 0:
	print(0)
else:
	print(list(cnt_dict.keys())[0], list(cnt_dict.values())[0])