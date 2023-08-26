import heapq


def solution(N, road, K):
    answer = 0

    # 인접 리스트 그래프 생성
    graph = {}
    for i in range(1, N + 1):
        graph[i] = {}

    for start_node, end_node, edge in road:
        if end_node in graph[start_node]:
            current_edge = graph[start_node][end_node]
            if edge < current_edge:
                graph[start_node][end_node] = edge
                graph[end_node][start_node] = edge
        else:
            graph[start_node][end_node] = edge
            graph[end_node][start_node] = edge

    # 각 노드의 가중치를 무한대로 초기화
    distances = {node: float('infinity') for node in graph}
    distances[1] = 0
    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    for key, value in distances.items():
        if value <= K:
            answer += 1

    return answer


N = 5
road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
K = 3
print(solution(N, road, K))

N1 = 6
read1 = [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
K1 = 4
print(solution(N1, read1, K1))
