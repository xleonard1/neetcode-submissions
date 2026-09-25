class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1

        min_ = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                min_ = min(min_, nums[left])
                break

            current_min_index = (left + right) // 2

            if nums[current_min_index] >= nums[left]:
                left = current_min_index + 1
            else:
                right = current_min_index - 1

        return min_
