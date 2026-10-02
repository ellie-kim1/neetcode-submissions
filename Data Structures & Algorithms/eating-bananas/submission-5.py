class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        hours = 0
        result = right

        while left < right:
            k = (left+right) // 2
            hours = 0

            for p in piles:
                hours += (p + k - 1) // k # ceiling division
            
            if hours <= h:
                result = min(result, k)
                right = k
            else:
                left = k + 1
        
        return result

