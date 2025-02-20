class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        res = 0

        while l < r:
            curr = min(height[l], height[r]) * (r - l)

            if curr > res:
                res = curr
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1

        return res