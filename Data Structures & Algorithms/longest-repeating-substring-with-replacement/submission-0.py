class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # need to use a hashmap as a frequency counter
        # string with the lowest frequency gets replaced
        # we need to keep up with the string within k though I think
        # we need to keep up with the index?

        hash_counter = {}
        left = 0
        right = 0
        max_len = 0
        max_frequency = 0

        for right in range(len(s)):
            char = s[right]

            hash_counter[char] = hash_counter.get(char, 0) + 1
            max_frequency = max(max_frequency, hash_counter[char])
            
            while (right - left + 1) - max_frequency > k:
                left_char = s[left]
                hash_counter[left_char] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len
                


