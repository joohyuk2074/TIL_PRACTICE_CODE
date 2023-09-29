class Solution:
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        stack.append((temperatures[0], 0))

        for day_idx in range(1, len(temperatures)):
            temperature = temperatures[day_idx]

            while stack and stack[-1][0] < temperature:
                tuple = stack.pop()
                prev_temperature = tuple[0]
                prev_day_idx = tuple[1]

                if answer[prev_day_idx] == 0:
                    answer[prev_day_idx] = day_idx - prev_day_idx

            stack.append((temperature, day_idx))

        return answer


solution = Solution()
print(solution.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
