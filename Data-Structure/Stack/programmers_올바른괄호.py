# -*- coding: utf-8 -*-
# 프로그래머스 올바른 괄호

def solution(s):

	if s[0] != '(' or s[-1] != ')':
		return False

	open_blanket = 0
	close_blanket = 0

	for i in s:
		if i == '(':
			open_blanket += 1
		else:
			close_blanket += 1
		if open_blanket < close_blanket:
			return False

	if open_blanket != close_blanket:
		return False

	return True