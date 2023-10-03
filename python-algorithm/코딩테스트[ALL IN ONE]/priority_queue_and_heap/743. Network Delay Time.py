import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, n, k):
        # 그래프 생성
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))

        costs = {}
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            cur_cost, cur_v = heapq.heappop(pq)
            if cur_v not in costs:
                costs[cur_v] = cur_cost
                for cost, next_v in graph[cur_v]:
                    next_cost = cur_cost + cost
                    heapq.heappush(pq, (next_cost, next_v))

        if len(costs) != n:
            return -1

        return max(costs.values())


solution = Solution()
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
print(solution.networkDelayTime(times, n, k))
