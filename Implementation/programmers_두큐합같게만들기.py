# -*- coding: utf-8 -*-
# 프로그래머스 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):

	answer = 0
	queue1 = deque(queue1)
	queue2 = deque(queue2)

	s1 = sum(queue1)
	s2 = sum(queue2)

	while s1 != s2:

		if answer >= (len(queue1) + len(queue2))/2*3:
			return -1

		if s1 > s2:
			n = queue1.popleft()
			queue2.append(n)
			s1 -= n
			s2 += n
			answer += 1
		else:
			n = queue2.popleft()
			queue1.append(n)
			s1 += n
			s2 -= n
			answer += 1

	return answer

print(solution([1, 2, 1, 2], [1, 10, 1, 2]))