class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # one thing I will need to do is a regular binary search, but the array could be rotated. I think I can check that the array is ordered in aschending by checking if left <= right if it is then it is ordered and I can say 

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]:
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
                    
            else:
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return - 1