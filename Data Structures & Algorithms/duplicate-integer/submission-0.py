class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for val in nums:
            if val in seen:
                return True
            else:
                seen.append(val)
        return False
        