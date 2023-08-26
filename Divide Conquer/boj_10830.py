# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 행렬제곱

import sys

input = sys.stdin.readline
n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
squared_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]
stored_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix))]

# 제곱할 column 저장하기
column = []
for i in range(len(matrix)):
    column.append([row[i] for row in matrix])

# 행렬 곱 구현하기
while b:
    for i, row in enumerate(matrix): # row만 꺼내주면 됨
        for j, col in enumerate(column):
            v = sum([row[_] * col[_] for _ in range(len(row))])
            stored_matrix[i][j], squared_matrix[i][j] = v, v
    print(squared_matrix)
    matrix = squared_matrix
    b -= 1

# 행렬 곱 구현하기
# while b:
# for i, row in enumerate(matrix):
#     for j in range(len(matrix)):
#         col = [r[j] for r in matrix]
#         v = sum([row[_] * col[_] for _ in range(len(row))])
#         stored_matrix[i][j], squared_matrix[i][j] = v, v
# print(squared_matrix)
# b -= 1
