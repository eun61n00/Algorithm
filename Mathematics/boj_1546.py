#1546 평균

n = int(input())
new_score = []
original_score = list(map(int, input().split()))
max = max(original_score)
for i in range(n):
    new_score.append(original_score[i]/max*100)
print(sum(new_score)/n)
