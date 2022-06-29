# -*- coding: utf-8 -*-
# boj 10814 나이순 정렬

import sys
input = sys.stdin.readline

n = int(input())
user_info = []
for _ in range(n):
	age, name = input().split()
	user_info.append((int(age), name.strip()))

user_dict = sorted(user_info, key = lambda item: item[0])
for age, name in user_dict:
	print(age, name)
