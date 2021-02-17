#3052 나머지

list = []
for i in range(10):
    n = int(input())
    list.append(n%42)

arr = set(list)
print(len(arr))
