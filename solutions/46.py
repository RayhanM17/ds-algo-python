class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        #Helper function that contains recursion
        def helper(choices, current_permutation=[]):
            #parameters - choices (list of nums), array for each individual perm
            #base case - when the choices list is empty, then append to res
            if not choices:
                res.append(list(current_permutation))
                return

            #For loop that iterates thru choices
            for i in range(len(choices)):
                choice = choices[i]

                #Add the current choice to the permutation
                current_permutation.append(choice)

                #Explore: Recursively call helper with remaining choices
                #Create new_choices by excluding the current choice
                new_choices = choices[:i] + choices[i+1:]
                helper(new_choices, current_permutation)

                #Unchoose (Backtrack): Remove the current choice to explore other branches
                current_permutation.pop()

        #Call helper func w/ choices set and empty array
        helper(nums)
        #Return res
        return res