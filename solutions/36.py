class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r / 3, c / 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if  (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True






# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         sub_freq = {}
#         row_freq = {}
#         col_freq = {}

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
                
#                 if r not in row_freq:
#                     row_freq[r] = set()
#                 if board[r][c] in row_freq[r]:
#                     return False
#                 row_freq[r].add(board[r][c])

#                 if c not in col_freq:
#                     col_freq[c] = set()
#                 if board[r][c] in col_freq[c]:
#                     return False
#                 col_freq[c].add(board[r][c])

#                 sub = (r // 3, c // 3)
#                 if sub not in sub_freq:
#                     sub_freq[sub] = set()
#                 if board[r][c] in sub_freq[sub]:
#                     return False
#                 sub_freq[sub].add(board[r][c])

#         return True