class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        t = m * n
        
        left = 0
        right = t - 1

        while left <= right: # binary search --> O(log(m*n))
            mid = (left + right) // 2

            i = mid // n
            j = mid % n

            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False

# Time: O(log(m*n))
# Space: O(1)
            
        