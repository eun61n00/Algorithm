# -*- coding: utf-8 -*-
# boj 1874 스택 수열

import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
stack = list()
ans = list()

for i in range(1, n + 1):
	data = int(input())

	while cnt <= data:
		stack.append(cnt)
		cnt += 1
		ans.append('+')

	if stack[-1] == data:
		stack.pop()
		ans.append('-')

	else:
		print('NO')
		exit(0)

print('\n'.join(ans))
