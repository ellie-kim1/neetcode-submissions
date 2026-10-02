class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        from collections import deque

        queue = deque()
        fresh = 0
        minutes = 0
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
            
        while queue and fresh > 0:
            level_size = len(queue)

            directions = {
                (-1, 0), #up
                (1, 0), #down
                (0, -1), #left
                (0, 1) #right
            }

            for i in range(level_size):

                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (0 <= new_row < len(grid)) and (0 <= new_col < len(grid[0])):
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            fresh -= 1
                            queue.append((new_row, new_col))
                
            minutes += 1
        
        if fresh > 0:
            return -1
        
        return minutes

