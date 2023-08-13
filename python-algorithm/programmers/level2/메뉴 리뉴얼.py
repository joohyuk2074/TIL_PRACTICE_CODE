import itertools


def solution(orders, course):
    answer = []

    for kind_num in course:
        combo_to_num = {}
        for order in orders:
            combinations = list(itertools.combinations(order, kind_num))
            for combo in combinations:
                combo_candidate = ''.join(sorted(combo))
                if combo_candidate in combo_to_num:
                    combo_to_num[combo_candidate] += 1
                else:
                    combo_to_num[combo_candidate] = 1

        # print(combo_to_num)

        max_count = 0
        for key in combo_to_num:
            if max_count < combo_to_num[key]:
                max_count = combo_to_num[key]

        for key in combo_to_num:
            if combo_to_num[key] > 1 and combo_to_num[key] == max_count:
                answer.append(key)

    answer.sort()
    return answer


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))

# orders1 = ["XYZ", "XWY", "WXA"]
# course1 = [2, 3, 4]
# print(solution(orders1, course1))
