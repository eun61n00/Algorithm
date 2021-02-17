# #1101 더하기 사이클

# n = input()
# count = 0
# new_num = []
# if len(n) == 1:
#     n = "0" + n
# new_num.append(str(int(n[0]) + int(n[1])))

# while n != new_num[-1]:
#     if len(new_num[-1]) == 1:
#         new_num[-1] = "0" + new_num[-1]
#     if count == 0:
#         new_num.append(str(int(n[1]) + int(new_num[-1][1])))
#     else:
#         new_num.append(str(int(new_num[-2][1]) + int(new_num[-1][1])))
#     count += 1
# print(count)

# ▽ 메모리 초과
# n = input()
# count = 1
# new_num = [] #새롭게 만든 숫자들을 저장해놓을 리스트 생성
# making = [] #숫자를 만드는데에 필요한 숫자들을 저장해놓을 리스트

# if len(n) == 1:
#     n = "0" + n
# making.append(str(int(n[0]) + int(n[1])))
# new_num.append(n[-1] + making[-1])

# while n != new_num[-1]:
#     making.append(str(int(new_num[-1][0])+int(new_num[-1][1])))
#     new_num.append(new_num[-1][-1]+making[-1][-1])
#     count += 1
# print(count)

n = input()
count = 1
new_num = []

if len(n) == 1:
    n = "0" + n
making_num = str(int(n[0]) + int(n[1]))
new_num.append(n[-1] + making_num[-1])

while n != new_num[-1]:
    making_num = str(int(new_num[-1][0])+int(new_num[-1][1]))
    new_num.append(new_num[-1][-1]+making_num[-1])
    count += 1
print(count)
