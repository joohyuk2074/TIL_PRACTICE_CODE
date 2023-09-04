from collections import deque


def solution(players, callings):
    answer = []

    players_deque = deque()
    for player in players:
        players_deque.append(player)

    calling_stack = []
    for calling in callings:

        while players_deque[-1] != calling:
            calling_stack.append(players_deque.pop())

        current_element = players_deque.pop()
        calling_stack.append(players_deque.pop())
        calling_stack.append(current_element)

        while calling_stack:
            players_deque.append(calling_stack.pop())

    return list(players_deque)


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))
