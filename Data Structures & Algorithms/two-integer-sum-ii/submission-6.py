class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            
            for x in range(1, len(numbers)):
                if numbers[x] == target - numbers[i]:
                    return [i+1, x + 1]
        

        