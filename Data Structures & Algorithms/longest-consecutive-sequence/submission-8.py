class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        count = set(nums)
        max_length = 0
        
        for num in count:
            
            if num - 1 not in count:
                curr_length = 1
                
                while num + 1 in count:
                    curr_length += 1
                    num += 1
                
                max_length = max(curr_length, max_length)
            
            num += 1
        
        return max_length