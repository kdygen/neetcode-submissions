# 1. counter = 0 nested for loops looking for land:
# 2. if land found then counter +=1 and call helper()
# 3. helper should go 4 directions and mark explored parts

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        land = "1"
        water = "0"
        rows = len(grid)
        columns = len(grid[0])

        def helper(row, column):
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return False

            if grid[row][column] != "1":
                return False
            
            original = grid[row][column]
            grid[row][column] = "#"

            up = helper(row-1, column)
            down = helper(row+1, column)
            right = helper(row, column+1)
            left = helper(row, column-1)
        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == land:
                    counter +=1
                    helper(i,j)
        
        return counter
                    