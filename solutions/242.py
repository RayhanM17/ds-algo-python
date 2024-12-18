class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case
        if len(s) != len(t):
            return False
        
        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1
            

        for char in t:
            if char not in counter or counter.get(char) == 0:
                return False
            counter[char] -= 1

        return True