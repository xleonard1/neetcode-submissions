class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        final_array = []

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    final_array = [i, j]
                
        return final_array