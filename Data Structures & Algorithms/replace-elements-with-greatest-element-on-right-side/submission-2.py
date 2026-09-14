class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        final_arr = []
        for i in range(len(arr) - 1):
            max_number = arr[i + 1]
            for j in range(i + 1, len(arr)):
                if arr[j] > max_number:
                    max_number = arr[j]
            arr[i] = max_number
            final_arr.append(arr[i])
        final_arr.append(-1)
        
        return final_arr
            
                

        