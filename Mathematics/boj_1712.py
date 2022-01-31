#시간초과
a, b, c = map(int, input().split())
x = 0

if c < b:
    print ("-1")
else: 
    while a+b*x >= c*x:
        x += 1
    print (x)
