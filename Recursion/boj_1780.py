# !/usr/bin/env python
# -*- coding: utf-8 -*-
# boj 1780 종이의 개수

def recursion(paper):
    global answer
    n = len(paper)
    if n == 1:
        answer += 1
        return
    same = True
    first_element = paper[0][0]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != first_element:
                same = False
                break
    if same == True:
        answer += 1
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
answer = 0
paper = [list(map(int, input().split())) for _ in range(N)]
recursion(paper)
print(answer)
