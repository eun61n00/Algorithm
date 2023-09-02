# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 17269 이름 궁합

n, m = map(int, input().split())
name1, name2 = input().split()

alphabet_dict = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1
}

# 1. 이름 합치기
string = ''
if n >= m:
    for i in range(m):
        string += name1[i] + name2[i]
    string += name1[m:]
else:
    for i in range(n):
        string += name1[i] + name2[i]
    string += name2[n:]

# 2. 궁합 계산하기
answer = []
for char in string:
    answer.append(alphabet_dict[char])
while len(answer) != 2:
    tmp = []
    for i in range(len(answer) - 1):
        tmp.append((answer[i] + answer[i + 1]) % 10)
    answer = tmp
print(f"{answer[0] * 10 + answer[1]}%")