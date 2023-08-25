def solution(book_time):
    answer = 0

    use_room_time_count = [0 for _ in range(0, 2000)]

    for start_time, end_time in book_time:
        start_int_time = time_to_minutes("start", start_time)
        end_int_time = time_to_minutes("end", end_time)
        for i in range(start_int_time, end_int_time):
            use_room_time_count[i] += 1

    for num in use_room_time_count:
        if answer < num:
            answer = num

    return answer


def time_to_minutes(flag, time):
    split = time.split(":")
    if flag == "start":
        hour = int(split[0])
        minute = int(split[1])
        return hour * 60 + minute
    else:
        hour = int(split[0])
        minute = int(split[1]) + 10
        return hour * 60 + minute


book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]
print(solution(book_time))

book_time1 = [["09:10", "10:10"], ["10:20", "12:20"]]
print(solution(book_time1))

book_time2 = [["05:57", "06:02"], ["04:00", "06:59"], ["03:56", "07:57"], ["06:12", "08:55"], ["07:09", "07:11"]]
print(solution(book_time2))

book_times3 = [["00:01", "00:10"], ["00:19", "00:29"]]
print(solution(book_times3))
