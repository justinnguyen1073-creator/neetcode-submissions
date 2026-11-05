from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict(Counter(nums))
        sorted_values = sorted(map, key = map.get)
        return sorted_values[len(sorted_values) - k:]
