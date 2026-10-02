class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for i in range(k):
            most_frequent = max(count, key=count.get)
            result.append(most_frequent)
            del count[most_frequent]
        
        return result