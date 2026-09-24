class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # think I need to get the middle array, check the beginning of the array, and the end of the array, and the end of the array in front of it and the beginning of the array behind it.
        # first array
        left = 0
        #  last array
        right = len(matrix) - 1

        # middle array
      

        while left <= right:
            middle = (left + right) // 2
            first_value_of_middle = matrix[middle][0]
            last_value_of_middle = matrix[middle][-1]

            if target > first_value_of_middle:
                left = middle + 1
            elif target < last_value_of_middle:
                right = middle - 1
                
            
            array_to_search = matrix[middle]
            left_middle = 0
            right_middle = len(array_to_search) - 1

            while left_middle <= right_middle:
                mid = (left_middle + right_middle) // 2

                if target == array_to_search[mid]:
                    return True
                elif target > array_to_search[mid]:
                    left_middle = mid + 1
                else: 
                    right_middle = mid - 1
        return False
            