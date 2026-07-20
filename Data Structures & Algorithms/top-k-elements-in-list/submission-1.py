class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}

        for i in nums:
            tracker[i] = 1 + tracker.get(i, 0)
        sorted_keys = sorted(tracker, key=lambda n: tracker[n], reverse=True)[:k]

        return sorted_keys