class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for i in range(k):
            most_freq = max(count, key=count.get)
            result.append(most_freq)
            del count[most_freq]
        
        return result