class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            if num not in hash_map:
                hash_map[num] = True
            else:
                return num
        