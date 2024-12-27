class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        store = set(nums)

        for num in store:
            if not num - 1 in store:
                length = 1
                while (num + length) in store:
                    length += 1
                longest = max(longest, length)

        return longest





# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) == 0:  # Fix: Check length of the list
#             return 0

#         numbers = set(nums)  # Use set to eliminate duplicates and for O(1) lookups
#         best = 1

#         while numbers:
#             starting_num = next(iter(numbers))
#             curr_num = starting_num
#             numbers.remove(curr_num)

#             curr_streak = 1

#             while curr_num + 1 in numbers:  # Continue the sequence
#                 numbers.remove(curr_num + 1)
#                 curr_num += 1
#                 curr_streak += 1

#             curr_num = starting_num

#             while curr_num - 1 in numbers:  # Continue the sequence
#                 numbers.remove(curr_num  - 1)
#                 curr_num -= 1
#                 curr_streak += 1

#             best = max(best, curr_streak)  # Update the best streak

#         return best