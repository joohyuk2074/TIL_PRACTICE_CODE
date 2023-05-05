def solution(num_list):
    answer = 0

    even = ''
    odd = ''
    for i in range(len(num_list)):
        num = num_list[i]
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)

    answer = int(even) + int(odd)

    return answer