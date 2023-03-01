# usr/bin/env python
# -*- coding: utf8 -*-
# boj 5585 거스름돈

pay = int(input())

money = [500, 100, 50, 10, 5, 1]
n = 1000 - pay

cnt = 0
for m in money:
    cnt += n // m
    n = n % m

    if n == 0:
        break

print(cnt)