def solution(today, terms, privacies):
    answer = []

    term_map = {}
    for term in terms:
        split = term.split(" ")
        type = split[0]
        type_days = split[1]
        term_map[type] = int(type_days) * 28

    for i in range(len(privacies)):
        privacy = privacies[i]
        privacy_split = privacy.split(" ")
        privacy_date = privacy_split[0]
        type = privacy_split[1]

        start_date = to_days(privacy_date)
        current_date = to_days(today)

        duration_days = current_date - start_date

        if duration_days >= term_map[type]:
            answer.append(i + 1)

    return answer


def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day


#
#
# def to_days1(expired_date, today_date):
#     expired_split = expired_date.split(".")
#     expired_year = int(expired_split[0])
#     expired_month = int(expired_split[1])
#     expired_day = int(expired_split[2])
#
#     split = today_date.split(".")
#     today_year = int(split[0])
#     today_month = int(split[1])
#     today_day = int(split[2])
#
#     expired_days = (expired_year * 12 * 28) + (expired_month * 28) + expired_day
#     today_days = (today_year * 12 * 28) + (today_month * 28) + today_day
#
#     return expired_days - today_days


today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))
