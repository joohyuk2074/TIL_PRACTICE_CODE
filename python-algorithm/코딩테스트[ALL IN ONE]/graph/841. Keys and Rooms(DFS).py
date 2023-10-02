from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms):
        room_num = len(rooms)
        checking_rooms = [False] * room_num

        def bfs(start):
            queue = deque()

            queue.append(start)
            checking_rooms[start] = True

            while queue:
                key = queue.popleft()

                for other_key in rooms[key]:
                    if checking_rooms[other_key] is False:
                        checking_rooms[other_key] = True
                        queue.append(other_key)

        bfs(0)

        for result in checking_rooms:
            if result is False:
                return False

        return True


solution = Solution()

rooms1 = [[1], [2], [3], []]
print(solution.canVisitAllRooms(rooms1))

rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
print(solution.canVisitAllRooms(rooms2))
