class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # go find the min(nums)
        # increment by one and see if it exists (curr_length += 1)
        # if it exists, potentially update: max_length = max(max_length, curr_length)

        # if it does not exist, find the next largest number after the number we are currently on
        # # no need to repeat the process

        # alternatively, we can also sort the list but this would require O(nlogn) complexity
        # let's see if my solution can be more efficient -- 2

        # alternatively, we can also use a hash map (key:value --> nums:count) -- 1
        # search in hash map has time complexity of O(1)

        # brute force method would be to use two for loops (O(n^2)) -- 3

        count = {}
        curr_length = 1
        max_length = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        while len(count) > 0:


            # we want to fix this line because min() makes the time complexity O(n)
            curr_num = min(count)
            curr_length = 1
            del count[curr_num]

            while (curr_num + 1) in count:
                curr_length += 1
                curr_num += 1
                del count[curr_num]
            max_length = max(curr_length, max_length)
        
        return max_length
