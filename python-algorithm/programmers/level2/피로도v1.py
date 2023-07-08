from itertools import permutations


def solution_v1(k, dungeons):
    answer = 0

    all_dungeons = []
    for i in permutations(dungeons, len(dungeons)):
        all_dungeons.append(list(i))

    possible = []
    i = 0
    while i < len(all_dungeons):
        stamina = k
        count = 0
        for j in all_dungeons[i]:
            if stamina >= j[0]:
                stamina -= j[1]
                count += 1
            elif stamina < j[0]:
                break

        possible.append(count)
        i += 1

    answer = max(possible)
    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution_v1(k, dungeons))
