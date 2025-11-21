from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        res = 0
        for row in range(len(grid)):
            for index in range(len(grid[row])):
                if grid[row][index] == "1" and visited[row][index] == False:
                    self.checkCurrent(grid, visited, res, row, index)
                    res += 1

        #for element in visited:
            #print(element)
        
        return res

    def checkCurrent(self, grid, visited, res, row, index):
        if visited[row][index] == True:
            return
        visited[row][index] = True
    
        # Go to top
        if row-1 >= 0 and grid[row-1][index] == '1':
            self.checkCurrent(grid, visited, res, row-1, index)

        # Go to bottom
        if row+1 < len(grid) and grid[row+1][index] == '1':
            self.checkCurrent(grid, visited, res, row+1, index)

        # Check left
        if index-1 >= 0 and grid[row][index-1] == '1':
            self.checkCurrent(grid, visited, res, row, index-1)

        # Check right
        if index+1 < len(grid[0]) and grid[row][index+1] == '1':
            self.checkCurrent(grid, visited, res, row, index+1)


my_grid=[["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]

solution = Solution()

print(solution.numIslands(my_grid))