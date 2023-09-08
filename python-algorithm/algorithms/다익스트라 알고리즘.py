import heapq

def dijkstra(graph, start):
    # 거리를 저장할 딕셔너리를 초기화하고, 시작점의 거리는 0으로 설정
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # 우선순위 큐를 초기화하고, 시작점만을 넣는다. (거리, 노드)
    priority_queue = [(0, start)]

    while priority_queue:
        # 가장 거리가 짧은 노드 선택
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드는 무시
        if distances[current_node] < current_distance:
            continue

        # 현재 노드를 경유하여 다른 노드로 가는 모든 경로를 확인
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 시작 노드부터 현재 노드를 경유하여 가는 거리가 더 짧은 경우
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 인접 리스트로 그래프를 표현: {노드: [(인접 노드, 가중치), ...], ...}
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graph, 'A'))  # 출력: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
