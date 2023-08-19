def solution(n, wires):
    answer = -1

    graph = {}

    # 1. Graph 생성하기
    for wire in wires:
        start = wire[0]
        end = wire[1]

        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = []
            graph[start].append(end)

        if end in graph:
            graph[end].append(start)
        else:
            graph[end] = []
            graph[end].append(start)

    # 2. 각 start - end 를 끊어서 vertex의 수를 비교하기
    min_vertex_count = 100
    for start in range(1, len(graph) + 1):
        for end in range(start + 1, len(graph) + 1):
            # 연결 끊기
            if end in graph[start]:
                graph[start].remove(end)
                graph[end].remove(start)

                # 각 정점에서 부터 정점의 수를 세기
                visited = [False for _ in range(len(graph) + 1)]
                start_vertex_num = dfs(start, graph, visited)
                end_vertex_num = dfs(end, graph, visited)

                if min_vertex_count > abs(end_vertex_num - start_vertex_num):
                    min_vertex_count = abs(end_vertex_num - start_vertex_num)

                # 다시 연결하기
                graph[start].append(end)
                graph[end].append(start)

    answer = min_vertex_count

    return answer


def dfs(node, graph, visited):
    visited[node] = True
    count = 1

    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, graph, visited)

    return count


n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))
