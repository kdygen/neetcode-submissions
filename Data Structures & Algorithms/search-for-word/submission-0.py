class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        columns = len(board[0])
        
        def helper(row, column, index):
            if index == len(word):
                return True
            
            if row < 0 or column < 0 or row >= rows or column >= columns:
                return False
            
            if board[row][column] != word[index]:
                return False
            
            original = board[row][column]
            board[row][column] = "#"

            up = helper(row-1, column, index+1)
            down = helper(row+1, column, index+1)
            right = helper(row, column+1, index+1)
            left = helper(row, column-1, index+1)

            board[row][column] = original

            return up or down or right or left

        for i in range(rows):
            for j in range(columns):
                if board[i][j] == word[0]:
                    if helper(i,j,0):
                        return True
        return False