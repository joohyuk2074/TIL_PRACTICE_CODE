def choose_n_from_list(elements, m, chosen=[]):
    if m == 0:
        return [chosen]
    if len(elements) == 0:
        return []

    results = []

    # 첫 번째 원소를 선택한 경우
    results.extend(choose_n_from_list(elements[1:], m - 1, chosen + [elements[0]]))

    # 첫 번째 원소를 선택하지 않은 경우
    results.extend(choose_n_from_list(elements[1:], m, chosen))

    return results

# 원래의 리스트
original_list = [1, 2, 3, 4, 5]

# m개를 선택 (예: m = 3)
m = 3

# 리스트에서 m개를 선택하는 모든 조합을 찾음
result = choose_n_from_list(original_list, m)
print(result)
