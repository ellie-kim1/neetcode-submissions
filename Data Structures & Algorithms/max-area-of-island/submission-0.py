class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        visited = set()

        # edge case:
        if len(grid) == 0:
            return 0
        
        def dfs(row, col):

            # out of bounds
            if row < 0 or row >= len(grid):
                return 0
            if col < 0 or col >= len(grid[0]):
                return 0
            # already visited
            if (row, col) in visited:
                return 0
            # water
            if grid[row][col] == 0:
                return 0
            
            visited.add((row, col))
            
            area = 1
            
            area += dfs(row-1, col)
            area += dfs(row+1, col)
            area += dfs(row, col -1)
            area += dfs(row, col + 1)

            return area
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1 and (row, col) not in visited:
                    area = dfs(row, col)
                    max_area = max(area, max_area)

        return max_area
        