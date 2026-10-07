class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        k = len(s1)
        right = k
        target_counts = {}
        window_counts = {}
        current_sub_string = s2[left:right]

        for char in s1:
            if char not in target_counts:
                target_counts[char] = 1
            else:
                target_counts[char] += 1
        
        for char in current_sub_string:
            if char not in window_counts:
                window_counts[char] = 1
            else:
                window_counts[char] += 1

        if window_counts == target_counts:
            return True
        
        while right < len(s2):

            if s2[right] not in window_counts:
                window_counts[s2[right]] = 1
            else: 
                 window_counts[s2[right]] += 1
            
            left_char = s2[left]

            window_counts[left_char] -= 1
            if window_counts[left_char] == 0:
                window_counts.pop(left_char)
            
            if window_counts == target_counts:
                return True
            
            right += 1
            left += 1
        return False

            
           


            
      
            



