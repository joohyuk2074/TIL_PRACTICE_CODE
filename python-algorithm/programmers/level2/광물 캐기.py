from collections import deque
from itertools import permutations


def solution(picks, minerals):
    answer = 0

    tools = []
    tools.extend(["diamond" for _ in range(picks[0])])
    tools.extend(["iron" for _ in range(picks[1])])
    tools.extend(["stone" for _ in range(picks[2])])

    min_score = 2 ** 31 - 1
    p = list(set(permutations(tools)))
    for tools in p:
        tools_queue = deque(tools)

        use_count = 0
        score = 0
        tool = tools_queue.popleft()

        for mineral in minerals:
            use_count += 1
            if (tool == mineral) or (tool == 'diamond'):
                score += 1
            elif tool == 'iron':
                if mineral == 'diamond':
                    score += 5
                else:
                    score += 1
            elif tool == 'stone':
                if mineral == 'diamond':
                    score += 25
                elif mineral == 'iron':
                    score += 5

            if use_count == 5:
                if len(tools_queue) == 0:
                    break
                tool = tools_queue.popleft()
                use_count = 0

        if min_score > score:
            min_score = score

    answer = min_score

    return answer


# picks = [1, 3, 2]
# minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# print(solution(picks, minerals))

picks1 = [0, 1, 1]
minerals1 = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks1, minerals1))
