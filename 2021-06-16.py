import sys

n = int(input())
stack = []

for _ in range(n):
    order = sys.stdin.readline().strip()
    
    if 'push' in order:
        order = order.replace("push ", '')
        stack.append(order)
    elif 'pop' in order:
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif 'size' in order:
        print(len(stack))
    elif 'empty' in order:
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    else:
        if stack:
            print(stack[-1])
        else:
            print('-1')