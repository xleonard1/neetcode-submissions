class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k - 1])
        total = 0
        
        
        for l in range(len(arr) - k + 1):
            current_sum += arr[l + k - 1]

            if (current_sum / k) >= threshold:
                total += 1
            
            current_sum -= arr[l]

        return total

