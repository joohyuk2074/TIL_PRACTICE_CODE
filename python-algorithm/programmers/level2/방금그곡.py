def solution(m, musicinfos):
    answer = ''

    music_name_to_orders = {}
    global_orders = {}
    for musicinfo in musicinfos:
        split = musicinfo.split(",")
        start_time = get_time_to_minute(split[0])
        end_time = get_time_to_minute(split[1])

        orders = get_list_order(split[3])
        music_name = split[2]

        music_name_to_orders[music_name] = orders
        global_orders[music_name] = []

        index = 0
        duration = end_time - start_time
        while duration >= 0:
            global_orders[music_name].append(orders[index])

            if index == len(orders) - 1:
                index = 0
            else:
                index += 1

            duration -= 1



        # global_orders와 music_name_to_orders의 각 name에 해당하는 부분이 몇개인지 비교

    return answer


def get_time_to_minute(time):
    split = time.split(":")
    hour = int(split[0])
    minute = int(split[1])
    return hour * 60 + minute


def get_list_order(order):
    result = []
    index = 0
    while index < len(order):
        if index + 1 < len(order) and order[index + 1] == '#':
            result.append(order[index] + order[index + 1])
            index += 1
        else:
            result.append(order[index])
        index += 1

    return result


m = "CC#BCC#BCC#BCC#B"
musicionfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicionfos))
