class Solution:
    def isValid(self, s: str) -> bool:
        char_storage = []
        mapping = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for char in s:
            if char in mapping.values():
                char_storage.append(char)
            else:
                if not char_storage or char_storage.pop() != mapping[char]:
                    return False
        return len(char_storage) == 0
        

 
            
    
        