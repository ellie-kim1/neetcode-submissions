class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target: # need a larger number
                left = mid + 1
            
            else: # need a smaller number
                right = mid - 1
            
        return -1