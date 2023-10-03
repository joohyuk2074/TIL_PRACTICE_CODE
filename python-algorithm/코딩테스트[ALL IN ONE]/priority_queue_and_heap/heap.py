import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]
heapq.heapify(min_heap)
heappop = heapq.heappop(min_heap)   # dequeue
print(heappop)
print(min_heap)
