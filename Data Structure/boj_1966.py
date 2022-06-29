# -*- coding: utf-8 -*-
# boj 1874 스택 수열

import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
	n, m = map(int, input().split())
	queue = list(map(int, input().split()))
	queue = [item for item in enumerate(queue)]

	ans = 0

	while queue:
		if queue[0][1] == max([doc[1] for doc in queue]):
			doc_idx, _ = queue.pop(0)
			ans += 1
			if doc_idx == m:
				break
		else:
			queue.append(queue.pop(0))

	print(ans)