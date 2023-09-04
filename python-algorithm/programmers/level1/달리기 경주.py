def solution(players, callings):
    answer = []

    order_to_player_map = {}
    for i in range(len(players)):
        order_to_player_map[players[i]] = i

    for calling in callings:
        idx = order_to_player_map[calling]
        player = players[idx - 1]

        prev_idx = order_to_player_map[player]

        players[idx], players[prev_idx] = player, calling
        order_to_player_map[player] = idx
        order_to_player_map[calling] = prev_idx

    answer = players

    return answer


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))
