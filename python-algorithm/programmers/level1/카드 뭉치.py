def solution(cards1, cards2, goal):
    answer = 'No'

    result = []
    cards1_idx = 0
    cards2_idx = 0
    for s in goal:
        while cards1_idx < len(cards1) and cards1[cards1_idx] == s:
            result.append(cards1[cards1_idx])
            cards1_idx += 1

        while cards2_idx < len(cards2) and cards2[cards2_idx] == s:
            result.append(cards2[cards2_idx])
            cards2_idx += 1

    if ''.join(goal) == ''.join(result) and len(goal) == len(result):
        return 'Yes'

    return answer


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))
