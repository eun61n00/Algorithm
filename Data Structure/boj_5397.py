# -*- coding: utf-8 -*-
# boj 5397 키로거

import sys
input = sys.stdin.readline

"""
아래 코드는 시간 초과 (insert의 느린 연산)

def keylogger(key):
	stack = list()
	stack_idx = 0

	while len(key) > 0:
		char = key.pop(0)
		if char == '<':
			if stack_idx > 0:
				stack_idx -= 1
		elif char == '>':
			if stack_idx <= len(stack):
				stack_idx += 1
		elif char == '-':
			if len(stack) > 0:
				stack_idx -= 1
				stack.pop()
		else:
			stack.insert(stack_idx, char)
			stack_idx += 1

	print(''.join(stack))


if __name__ == '__main__':
	test_case = int(input())
	for _ in range(test_case):
		key = []
		key[:0] = input()[:-1]
		keylogger(key)
"""


test_case = int(input())

for _ in range(test_case):
	left_stack = []
	right_stack = []
	data = input()[:-1]
	for char in data:
		if char == '<':
			if left_stack:
				right_stack.append(left_stack.pop())
		elif char == '>':
			if right_stack:
				left_stack.append(right_stack.pop())
		elif char == '-':
			if left_stack:
				left_stack.pop()
		else:
			left_stack.append(char)

	print(''.join(left_stack + right_stack))
