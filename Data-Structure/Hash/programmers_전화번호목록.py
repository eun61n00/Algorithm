# -*- coding: utf-8 -*-
# 프로그래머스 전화번호 목록

def solution(phone_book):

	phone_book.sort()
	min_len = len(phone_book[0])

	prefix = [phone for phone in phone_book if len(phone) == min_len]
	others = [phone for phone in phone_book if phone not in prefix]

	for other in others:
		for pre in prefix:
			if other[:len(pre)] == pre:
				return False
	return True

def solution2(phone_book):

	phone_book.sort()
	min_len = len(phone_book[0])

	for i in range(len(phone_book) - 1):
		if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
			return False
	return True

def solution3(phone_book):
	phone_book = sorted(phone_book)

	for p1, p2 in zip(phone_book, phone_book[1:]):
		if p2.startswith(p1):
			return False
	return True