# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 18511 큰 수 구성하기

n, k = map(int, input().split())
element = list(map(int, input().split()))
element.sort()

n_str = str(n)
answer = ["0"] * len(n_str)

for idx, ch in enumerate(n_str):
    for ele in element:
        if ele <= int(ch):
            answer[idx] = str(ele)
    if answer[idx] == n_str[idx]:
        continue
    else:
        break


for i in range(idx + 1, len(n_str)):
    answer[i] = str(element[-1])

print(''.join(answer))
