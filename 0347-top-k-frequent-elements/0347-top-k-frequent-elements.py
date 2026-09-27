from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        counts = sorted(count.items() , key=lambda x:x[1] , reverse=True)
        print(counts)
        return [val[0] for val in counts][:k]
        