# -*- coding: utf-8 -*-
# boj 1427 소트 인사이드

import sys
input = sys.stdin.readline

num = input().strip()
num_arr = []
for chr in num:
    num_arr.append(int(chr))

num_arr.sort(reverse=True)
for num in num_arr:
    print(num, end='')

# -*- coding: utf-8 -*-
# boj 1427 소트 인사이드

input = sys.stdin.readline

array = input().strip()
for i in range(9, -1, -1):
    for num in array:
        if i == int(num):
            print(num, end='')
