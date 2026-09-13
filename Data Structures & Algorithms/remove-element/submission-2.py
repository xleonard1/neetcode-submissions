class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        els_in_nums_not_equal_to_val = []
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
               del nums[i]
            else:
                 els_in_nums_not_equal_to_val.append(nums[i])
        
        return len(els_in_nums_not_equal_to_val)