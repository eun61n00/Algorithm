# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1074

n, r, c = map(int, input().split())


def visit(n, r, c):
    if n == 0:
        return 0

    half = 2**(n-1)

    if r < (2**n // 2) and c < (2**n // 2):
        return visit(n - 1, r, c)
    elif r < (2**n // 2) and c >= (2**n // 2):
        return half**2 * 1 + visit(n - 1, r, c - half)
    elif r > (2**n // 2) and c < (2**n // 2):
        return half**2 * 2 + visit(n - 1, r - half, c)
    else:
        return half**2 * 3 + visit(n - 1, r - half, c - half)


print(visit(n, r, c))
