class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_count = 0
        left = 0
        right = 0
        has_seen_map = {}
        
        while right < len(s):
            current_char = s[right]
                
            if current_char in has_seen_map and has_seen_map[current_char] >= left:
                left = has_seen_map[current_char] + 1
            
    
            has_seen_map[current_char] = right

            max_count = max(max_count, right - left + 1)
            right += 1
        return max_count
