def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))

    while storey:
        floor = storey.pop()
        if (floor == 5 and ((storey and storey[-1] < 5) or not storey)) or floor < 5:
            answer += floor
        else:
            answer += (10 - floor)
            if storey:
                storey.append(storey.pop() + 1)
            else:
                answer += 1

    return answer


storey = 16
print(solution(storey))

storey1 = 2554
print(solution(storey1))

storey2 = 1
print(solution(storey2))
