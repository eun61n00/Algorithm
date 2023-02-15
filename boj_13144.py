# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 13144 List of Unique Numbers

import sys
from collections import defaultdict

num_dict = defaultdict(list)
input = sys.stdin.readline
n = int(input().rstrip())

num_list = list(map(int, input().split()))
for idx, num in enumerate(num_list):
    num_dict[num].append(idx)

result = 0

# 각 자리에서 가능한 곳까지 count
for idx, num in enumerate(num_list):
    i = num_dict[num].index(idx)

    # num이 나오는 곳이 현재 인덱스가 마지막일 때, 끝까지 가능한 경우의 수 count
    if i + 1 == len(num_dict[num]):
        result += (len(num_list) - idx)

    # 다음 num이 나오는 곳까지 count
    else:
        result += num_dict[num][i + 1] - num_dict[num][i]

print(result)

# ! 첫 문자와 마지막 문자가 중복될 때 뿐만 아니라 중간 글자와 마지막 글자가 중복될 때도 고려해야 함