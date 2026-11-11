# 1. initiate the grid, result[], openings, nested for loops to go each index
# 1.5 we need to define the pacific/atlantic edges
# 2. def helper: with a param of start which will take for loop going through all pacific/atlantic edges
# 3. base case if  atlantic == pacific then append that to result
# 4. if up/down/rihgt/left.value higher than current then return 
# 5.  if up/down/rihgt/left.value lower than current then update that cell to be atlantic/pacific

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])

        result = []         
        openings = []

        #[0,0][0,1][0,2][0,3]
        #[1,0][1,1][1,2][1,3]
        #[2,0][2,1][2,2][2,3]

        pacific = []
        atlantic = []
        for i in range(rows):
            for j in range(columns):
                if j == 0 or i == 0:
                    pacific.append([i,j])
                if i == rows - 1 or j == columns - 1:
                    atlantic.append([i,j])

        a_visited = set()
        p_visited = set()

        def helper(row, column, visited):
            if row < 0 or row >= rows or column < 0 or column >= columns:
                return
            
            if (row,column) in visited:
                return

            visited.add((row,column))
            
            if row > 0 and heights[row-1][column] >= heights[row][column]:
                helper(row-1,column,visited)
            
            if row < rows - 1 and heights[row+1][column] >= heights[row][column]:
                helper(row+1, column, visited)
            
            if column < columns - 1 and heights[row][column+1] >= heights[row][column]:
                helper(row, column+1, visited)

            if column > 0 and heights[row][column-1] >= heights[row][column]:
                helper(row, column-1, visited)
        
        for row, column in pacific:
            helper(row, column, p_visited)
        
        for row, column in atlantic:
            helper(row, column, a_visited)

        for i in range(rows):
            for j in range(columns):
                if (i, j) in p_visited and (i, j) in a_visited:
                    result.append([i, j])

        return result

        