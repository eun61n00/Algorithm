# -*- coding: utf-8 -*-
# 산업공학과 코딩대회 2022년 9월 2일

# #1
def solution1(v):

	result = []

	x = [pnt[0] for pnt in v]
	y = [pnt[1] for pnt in v]

	for pnt_x in x:
		if x.count(pnt_x) < 2:
			result.append(pnt_x)
			break

	for pnt_y in y:
		if y.count(pnt_y) < 2:
			result.append(pnt_y)
			break

	return result


def solution2(N, works):

	works.sort(reverse = True)
	idx = 0

	while N > 0:

		if idx >= len(N) or works[idx] == 0:
			idx = 0

		works[idx] -= 1
		idx += 1
		N -= 1

	return sum([num * num for num in works])


def solution3():
	return False


def solution4(s):

	from collections import deque

	result = [1]

	for i in range(len(s) - 1):
		idxs = [j for j in range(i, len(s)) if s[i] == s[j]]
		flag = 0

		for idx in idxs[::-1]:

			string = deque(s[i: idx + 1])
			front, back = deque([]), deque([])

			if flag == 1:
				break

			while len(string) > 1:
				front.append(string.popleft())
				back.append(string.pop())

			if front == back:
				result.append(idx - i + 1)

	return max(result)