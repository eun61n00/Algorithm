#11021 A+B - 7

#https://www.acmicpc.net/problem/11021

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    ans = a+b
    print("Case #%s: %s"%(i+1, ans ))
