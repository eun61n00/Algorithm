#2439 별 찍기 - 2

n = int(input())

for i in range(1, n+1):
    str = '*'*i
    print(str.rjust(n))
