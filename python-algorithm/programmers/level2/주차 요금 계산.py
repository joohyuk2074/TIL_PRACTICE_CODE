import math


def solution(fees, records):
    answer = []

    d_time = fees[0]  # 기본 시간
    d_fee = fees[1]  # 기본 요금
    e_time = fees[2]  # 초과 시간
    e_fee = fees[3]  # 초과 요금

    car_num_to_time_map = {

    }
    for text in records:
        columns = text.split(" ")
        time = columns[0]
        car_num = columns[1]
        type = columns[2]

        if car_num not in car_num_to_time_map and type == 'IN':  # 처음 in인 경우
            car_num_to_time_map[car_num] = (time, 0, type)
        elif car_num in car_num_to_time_map and type == 'OUT':
            tuple = car_num_to_time_map[car_num]

            prev_time = tuple[0]
            prev_duration = tuple[1]
            current_time = time
            temp_duration = getMinusMinute(prev_time, current_time)

            car_num_to_time_map[car_num] = (current_time, prev_duration + temp_duration, type)
        elif car_num in car_num_to_time_map and type == 'IN':
            tuple = car_num_to_time_map[car_num]
            car_num_to_time_map[car_num] = (time, tuple[1], 'IN')

    # print(car_num_to_time_map)

    for key in car_num_to_time_map:
        tuple = car_num_to_time_map[key]
        if tuple[2] == 'IN':
            duration = getMinusMinute(tuple[0], "23:59")
            car_num_to_time_map[key] = (tuple[0], tuple[1] + duration, 'OUT')

    sorted_dict = sorted(car_num_to_time_map.keys(), key=int)

    for key in sorted_dict:
        tuple = car_num_to_time_map[key]
        duration = tuple[1]

        if duration <= d_time:
            answer.append(d_fee)
        else:
            total_fee = d_fee + math.ceil((duration - d_time) / e_time) * e_fee
            answer.append(total_fee)

    return answer


def getMinusMinute(prev_time, current_time):
    prevs = prev_time.split(":")
    currents = current_time.split(":")

    prev_hour = int(prevs[0])
    prev_minute = int(prevs[1])
    prev_duration = prev_hour * 60 + prev_minute

    current_hour = int(currents[0])
    current_minute = int(currents[1])
    current_duration = current_hour * 60 + current_minute

    return current_duration - prev_duration


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
