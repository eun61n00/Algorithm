num = int(input())
cnt = 0

for i in range(num):
    word = input()
    word = list(word)
    for j in range(len(word)):
        checking_char = word[0]
        del word[0]
        if len(word) == 0:
            break
        if checking_char in word:
            if checking_char != word[0]:
                cnt += 1
                break
            else: #checking_cahr == word[0]
                continue
print(num-cnt)
