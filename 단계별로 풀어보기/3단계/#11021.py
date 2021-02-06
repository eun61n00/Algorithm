#11021 A+B - 7

#https://www.acmicpc.net/problem/11021

import sys

read = sys.stdin.readline

n = int(read())
for i in range(n):
    a, b = map(int, input().split())
    print("Case #", int(i+1), ": ", int(a+b))
