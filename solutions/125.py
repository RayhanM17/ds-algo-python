class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
#         s = s.lower()
#         clean = ""

#         for char in s:
#             if char in alphabet:
#                 clean += char
        
#         return clean == clean[::-1]