class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #find product of all then divide by i
        #if i == 0 return 0
        total_product = 1
        zero_count = 0
        for n in nums:
            if n != 0:
                total_product *= n
            else:
                zero_count += 1    
        results = []
    
        for n in nums:
            if zero_count > 1:
                results.append(0)
            elif zero_count == 1:
                if n == 0:
                    results.append(total_product)
                else:
                    results.append(0)
            else:
                results.append(total_product // n)
    
        return results