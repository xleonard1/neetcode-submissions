class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
                hash_map[num] = i
        
        for i, num in enumerate(nums):
            target_complement = target - num
            if target_complement in hash_map and hash_map[target_complement] != i:
                return [i, hash_map[target_complement]]

        return []