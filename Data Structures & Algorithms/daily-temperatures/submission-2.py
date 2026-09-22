class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperature > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                days_passed = result[stack_index] = i - stack_index
            stack.append((temperature,i))

        return result

            