# <이것이 코딩 테스트다>(나동빈, 한빛미디어) 예제 4-2. 시각
n = int(input())
h, m, s = 0, 0, 0
cnt = 0

while h <= n:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            if '3' in str(s) or '3' in str(m) or '3' in str(h):
                cnt += 1
            s += 1
        m += 1
    h += 1

print(cnt)