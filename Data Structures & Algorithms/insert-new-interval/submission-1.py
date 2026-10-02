class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        merged = []

        for interval in intervals:

            # after
            if newInterval[0] > interval[1]:
                merged.append(interval)

            # before
            elif newInterval[1] < interval[0]:
                merged.append(newInterval)
                newInterval = interval

            # overlap
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]
            
        merged.append(newInterval)
        return merged