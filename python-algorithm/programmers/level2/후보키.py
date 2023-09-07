from itertools import combinations


def solution(relation):
    answer = 0

    column_to_data = {}
    for columns in relation:
        for i in range(len(columns)):  # i는 컬럼 인덱스
            if i in column_to_data:
                column_to_data[i].append(columns[i])
            else:
                column_to_data[i] = [columns[i]]

    index_arr = []
    for i in range(len(relation[0])):
        index_arr.append(i)

    # n개 중에 m개를 조합해서 unique한지 판단
    combo_box = set()
    for cnt in range(1, len(relation[0]) + 1):  # 후보키 개수
        for combo in combinations(index_arr, cnt):  # (1,2), (1,3), (1,2,3)

            arr = [[] for _ in range(len(relation))]
            for i in range(len(relation)):
                for idx in list(combo):
                    arr[i].append(column_to_data[idx][i])

            # unique 판별
            unique = set()
            for tuple in arr:
                join = ''.join(tuple)
                unique.add(join)

            if len(unique) == len(relation):
                is_unique = True
                for element in combo_box:
                    combos = list(element)

                    is_contains = True
                    for combo_element in combos:
                        if combo_element not in list(combo):
                            is_contains = False
                            break
                    if is_contains is True:
                        is_unique = False
                        break

                if is_unique:
                    combo_box.add(combo)

    answer = len(combo_box)

    return answer


relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
print(solution(relation))
