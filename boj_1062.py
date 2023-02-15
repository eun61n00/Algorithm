# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1062 가르침

import sys
from itertools import combinations

input = sys.stdin.readline

n, k = map(int, input().split())
words = []
for i in range(n):
    words.append(input().rstrip()[4:-4])

learned = ['a', 'n', 't', 'i', 'c']
alphabets = [chr(97 + i) for i in range(26)]


result = 0
if k < 5:
    result = 0
    exit(0)

for i in range(len(words)):
    for ch in learned:
        words[i].replace(ch, '')

cnt = k - 5