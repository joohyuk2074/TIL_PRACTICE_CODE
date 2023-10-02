class Solution:
    def canVisitAllRooms(self, rooms):
        room_num = len(rooms)
        checking_rooms = [False] * room_num

        def dfs(start):
            keys = rooms[start]

            for key in keys:
                if checking_rooms[key] is False:
                    checking_rooms[key] = True
                    dfs(key)

        dfs(0)
        checking_rooms[0] = True

        for result in checking_rooms:
            if result is False:
                return "false"

        return "true"


solution = Solution()

rooms1 = [[1], [2], [3], []]
print(solution.canVisitAllRooms(rooms1))

rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
print(solution.canVisitAllRooms(rooms2))
