# -*- coding: utf-8 -*-
# 프로그래머스 올바른 괄호

from math import ceil

def solution(progresses, speeds):
	completion = 0
	result = []

	idx = [i for i in range(len(progresses))]
	durations = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]

	for i in range(len(durations)):

		if len(idx) == 0:
			break

		if i not in idx:
			continue

		completion += 1
		idx.remove(i)

		for j in range(i + 1, len(durations)):
			if durations[i] >= durations[j]:
				completion += 1
				idx.remove(j)
			else:
				break

		result.append(completion)
		completion = 0

	return result