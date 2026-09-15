class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency_counter = {}
        t_frequency_counter = {}

        for char in s:
            if char not in s_frequency_counter: 
                s_frequency_counter[char] = 1
            else:
                s_frequency_counter[char] += 1
        
        for char in t:
            if char not in t_frequency_counter: 
                t_frequency_counter[char] = 1
            else:
                t_frequency_counter[char] += 1
        
        if s_frequency_counter == t_frequency_counter:
            return True

        return False


        