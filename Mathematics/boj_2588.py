#2588

a = int(input())
b = input()
b_reverse = b[::-1]
for i in b_reverse:
    print (a * int(i))
print(a * int(b))
