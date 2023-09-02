from collections import OrderedDict

def solution(m, musicinfos):
    answer = ''

    memory_orders = replace_orders(m)

    music_orders_str = ''
    music_order_list = []

    for music_info in musicinfos:
        split = music_info.split(",")

        start_minute = time_to_long(split[0])
        end_minute = time_to_long(split[1])
        music_name = split[2]
        music_orders = replace_orders(split[3])

        music_order_idx = 0
        duration = end_minute - start_minute
        while duration > 0:
            music_orders_str += music_orders[music_order_idx]
            music_order_list.append((music_orders[music_order_idx], music_name))
            duration -= 1

            music_order_idx += 1
            if music_order_idx == len(music_orders):
                music_order_idx = 0

    index = music_orders_str.find(memory_orders)

    if index == -1:
        return "(None)"

    result_map = OrderedDict()
    for i in range(index, index + len(memory_orders)):
        music_name_key = music_order_list[i][1]
        if music_name_key in result_map:
            result_map[music_name_key] += 1
        else:
            result_map[music_name_key] = 1

    max = 0
    for key in result_map:
        if max < result_map[key]:
            max = result_map[key]
            answer = key

    return answer


def time_to_long(time):
    split = time.split(":")
    hour = int(split[0])
    minute = int(split[1])
    return hour * 60 + minute


def replace_orders(orders):
    return orders.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a').replace('E#', 'e')


# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# print(solution(m, musicinfos))
#
# m1 = "CC#BCC#BCC#BCC#B"
# musicinfos1 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# print(solution(m1, musicinfos1))
#
# m2 = "ABC"
# musicinfos2 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
# print(solution(m2, musicinfos2))
#
# print(solution("C", ["13:00,13:01,WORLD,F"]))

m = "C#C"
musicinfos = ["12:00,12:06,HELLO,C#C#CC#"]
print(solution(m, musicinfos))
