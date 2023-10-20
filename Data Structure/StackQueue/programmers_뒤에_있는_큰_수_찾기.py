def solution(numbers):
    answer = [0] * len(numbers)
    stack = []

    # 자기 자신이 뒷 큰수가 될 수 있는지 확인
    for idx, n in enumerate(numbers):
        while stack:
            if stack[-1][1] < n:  # 자기 자신이 stack의 제일 뒤에 있는 애보다 큰 애니까 뒷 큰수가 됨
                answer[stack[-1][0]] = n
                stack.pop()

            else:
                break
        stack.append((idx, n))

    answer = [ans if ans > 0 else -1 for ans in answer]

    return answer
