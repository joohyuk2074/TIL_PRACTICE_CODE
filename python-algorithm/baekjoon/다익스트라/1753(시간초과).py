import heapq

n, m = map(int, input().split())
start = int(input())
links = [[] for _ in range(n + 1)]
dist = [1e9 for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    links[a].append([b, c])

q = []
heapq.heappush(q, [0, start])
dist[start] = 0

while q:
    w, v = heapq.heappop(q)

    for nxt, weight in links[v]:
        if dist[v] + weight < dist[nxt]:
            dist[nxt] = dist[v] + weight
            heapq.heappush(q, [dist[nxt], nxt])

for i in range(1, n + 1):
    if dist[i] == 1e9:
        print("INF")
    else:
        print(dist[i])
