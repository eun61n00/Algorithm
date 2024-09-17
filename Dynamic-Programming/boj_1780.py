# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1780 종이의 개수

def recursion(paper):
    global cnt_zero, cnt_one, cnt_minus
    n = len(paper)
    same = True
    first_element = paper[0][0]
    if n == 1:
        if first_element == 0:
            cnt_zero += 1
        elif first_element == 1:
            cnt_one += 1
        else:
            cnt_minus += 1
        return

    for i in range(n):
        for j in range(n):
            if paper[i][j] != first_element:
                same = False
                break
    if same == True:
        if first_element == 0:
            cnt_zero += 1
        elif first_element == 1:
            cnt_one += 1
        else:
            cnt_minus += 1
        return
    else:
        recursion([paper[i][0:n//3] for i in range(0, n//3)])
        recursion([paper[i][0:n//3] for i in range(n//3, n//3*2)])
        recursion([paper[i][0:n//3] for i in range(n//3*2, n)])
        recursion([paper[i][n//3:n//3*2] for i in range(0, n//3)])
        recursion([paper[i][n//3:n//3*2] for i in range(n//3, n//3*2)])
        recursion([paper[i][n//3:n//3*2] for i in range(n//3*2, n)])
        recursion([paper[i][n//3*2:n] for i in range(0, n//3)])
        recursion([paper[i][n//3*2:n] for i in range(n//3, n//3*2)])
        recursion([paper[i][n//3*2:n] for i in range(n//3*2, n)])


N = int(input())
cnt_zero, cnt_one, cnt_minus = 0, 0, 0
paper = [list(map(int, input().split())) for _ in range(N)]
recursion(paper)
print(cnt_minus)
print(cnt_zero)
print(cnt_one)
