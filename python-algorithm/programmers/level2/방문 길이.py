def solution(dirs):
    answer = 0

    direction = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1)
    }

    trace_set = set()
    start_x = 0
    start_y = 0
    for command in dirs:
        tuple = direction[command]
        end_x = start_x + tuple[0]
        end_y = start_y + tuple[1]

        if -5 <= end_x <= 5 and -5 <= end_y <= 5:
            text = command + str(start_x) + str(start_y) + str(end_x) + str(end_y)
            if text not in trace_set:
                trace_set.add(text)
                if command == 'U':
                    trace_set.add('D' + str(end_x) + str(end_y) + str(start_x) + str(start_y))
                elif command == 'R':
                    trace_set.add('L' + str(end_x) + str(end_y) + str(start_x) + str(start_y))
                elif command == 'D':
                    trace_set.add('U' + str(end_x) + str(end_y) + str(start_x) + str(start_y))
                elif command == 'L':
                    trace_set.add('R' + str(end_x) + str(end_y) + str(start_x) + str(start_y))
                answer += 1

            start_x = end_x
            start_y = end_y

    return answer



# query1 = "ULURRDLLU"
# print(solution(query1))
query2 = "LRLRL"
print(solution(query2))
