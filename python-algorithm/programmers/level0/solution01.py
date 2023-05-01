# https://school.programmers.co.kr/learn/courses/30/lessons/181941

# my solution
def my_solution(arr):
    answer = ''
    for c in arr:
        answer += c
    return answer

# other solution
def other_solution(arr):
    return ''.join(arr)


print(other_solution(["a", "b", "c"]))