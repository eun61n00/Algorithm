# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1041 주사위

n = int(input())
a, b, c, d, e, f = map(int, input().split())

# 3개 조합
# 주사위의 꼭짓점을 기준으로 8개의 조합이 나옴
face3 = min(
    a + d + e,
    a + c + e,
    a + b + d,
    a + b + c,
    d + e + f,
    d + f + b,
    b + c + f,
    c + e + f
)

# 2개 조합
# 모서리를 기준으로 12개가 조합이 나옴
face2 = min(
    a + b, a + c, a + e, a + d,
    b + c, b + d, b + f, c + f,
    c + e, d + e, d + f, e + f
)

face1 = min(a, b, c, d, e, f)

num_face3 = 4
num_face2 = (n - 1) * 4 + (n - 2) * 4
num_face1 = (n - 2) * (n - 1) * 4 + (n - 2) * (n - 2)

if n == 2:
    num_face3 = 4
    num_face2 = 4
    num_face1 = 0
answer = num_face3 * face3 + num_face2 * face2 + num_face1 * face1

if n == 1:
    answer = a + b + c + d + e + f - max(a, b, c, d, e, f)

print(answer)
