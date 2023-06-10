def solution(name, yearning, photo):
    answer = []

    nameToYearningMap = dict(zip(name, yearning))

    for i in range(len(photo)):
        sum = 0
        for name in photo[i]:
            if name in nameToYearningMap:
                sum += nameToYearningMap[name]
        answer.append(sum)

    return answer


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))
