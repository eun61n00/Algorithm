# !/usr/bin/python
# -*- coding: utf-8 -*-
# boj 10830 행렬제곱

import sys

input = sys.stdin.readline


def multiply_matrix(A, B):
    """
    두 행렬 A, B를 곱하는 함수
    """
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = sum(
                [(a * b) for a, b in zip(A[i], [b[j] for b in B])]) % 1000
    return result


def pow_matrix(matrix, B):
    """
    행렬 matrix를 B 제곱하는 함수
    """
    if B == 1:
        return [[element % 1000 for element in row] for row in matrix]

    if B == 2:
        return multiply_matrix(matrix, matrix)

    if B % 2 == 0:
        matrix = pow_matrix(pow_matrix(matrix, B//2), 2)
    else:
        matrix = multiply_matrix(pow_matrix(
            pow_matrix(matrix, B//2), 2), matrix)
    return matrix


N, B = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

result = pow_matrix(matrix, B)

for row in result:
    print(' '.join(map(str, row)))
