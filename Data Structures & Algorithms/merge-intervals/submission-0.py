class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda interval:interval) # efficient sort --> O(nlogn)
        merged = []

        for interval in intervals: # loop over intervals --> O(n)
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [min(merged[-1][0], interval[0]), max(merged[-1][1], interval[1])]
        return merged

# Time: O(nlogn) + O(n) = O(nlogn)
# Space: O(n)