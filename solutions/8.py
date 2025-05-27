class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Use strip() to remove leadingwhitespace
        if not s:  # Handle empty string after stripping
            return 0

        i = 0
        sign = 1
        num = 0
        
        # Handle sign
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        # Process digits
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before adding the digit
            # For positive numbers: num * 10 + digit > 2^31 - 1
            # For negative numbers: num * 10 + digit (with original sign) < -2^31
            
            # Integer limits
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31

            if sign == 1:
                if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                    return INT_MAX
            else: # sign == -1
                if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 8):
                    return INT_MIN
            
            num = num * 10 + digit
            i += 1
            
        return sign * num
        