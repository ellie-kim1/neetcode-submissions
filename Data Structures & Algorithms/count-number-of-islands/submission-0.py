class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        islands = 0


        def dfs(row, col):

            # cond1: within bound
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return
            # cond2: must be land and not visited
            if grid[row][col] != "1" or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            dfs(row-1, col) #down
            dfs(row+1, col) #up
            dfs(row, col-1) #left
            dfs(row, col+1) #right

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    islands += 1
    
        return islands
                