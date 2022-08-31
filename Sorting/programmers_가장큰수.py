# -*- coding: utf-8 -*-
# 프로그래머스 가장 큰 수

from itertools import permutations

def solution(numbers):
	numbers = [str(num) for num in numbers]

	num_list = list(permutations(numbers, len(numbers)))
	num_list = [int(''.join(num)) for num in num_list]

	return str(max(num_list))

def solution2(numbers):

	if sum(numbers) == 0:
		return "0"

	numbers = list(map(str, numbers))
	numbers.sort(key = lambda x: x * 3, reverse = True)

	return (''.join(numbers))

