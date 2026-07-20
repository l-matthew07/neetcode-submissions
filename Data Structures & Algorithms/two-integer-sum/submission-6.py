class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        before = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in before:
                return[before[diff], i]
            before[n] = i
        return