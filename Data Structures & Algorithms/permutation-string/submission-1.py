class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # I need to use string 1 as the length that we iterate
        # So we loop through lecabee.. we get k = len(s1)
        # k = 3, we check the first three strings
        # left = 0 right = 0..right always moves up the length of k
        # we compare the substring to abc..if we find that the letters in the substring are the same as the letters in s1 we return true, otherwise we return false
        left = 0
        k = len(s1)
        right = k
        sub_string = sorted(s2[left:right])
        sorted_s1 = sorted(s1)

        while right <= len(s2):

            if sorted_s1 != sub_string:
                left += 1
                right += 1
                sub_string = sorted(s2[left:right])
            else:
                return True
        return False
            
      
            



