def solution(data, ext, val_ext, sort_by):
    answer = []

    ext_to_idx = {
        "code": 0,
        "date": 1,
        "maximum": 2,
        "remain": 3
    }

    filter_idx = ext_to_idx[ext]
    for row in data:
        if row[filter_idx] < val_ext:
            answer.append(row)

    sorted_idx = ext_to_idx[sort_by]
    answer = sorted(answer, key=lambda x: x[sorted_idx])

    return answer


data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
ext = "date"
val_ext = 20300501
sort_by = "remain"

result = solution(data, ext, val_ext, sort_by)
print(result)
