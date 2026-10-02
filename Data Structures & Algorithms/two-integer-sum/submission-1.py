class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            want = target - nums[i]

            if want in seen:
                return [seen[want], i]
            
            seen[nums[i]] = i