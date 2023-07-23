def solution(numbers):
    answer = [-1] * (len(numbers))
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)

    return answer


arr1 = [9, 1, 5, 3, 6, 2]
print(solution(arr1))
