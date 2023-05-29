def solution(absolutes, signs):
    answer = 0

    for num, boolean in zip(absolutes, signs):
        if boolean:
            answer += num
        else:
            answer += -num

    return answer


def other_solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
