from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        def find_row(matrix: List[List[int]], target: int) -> int:
            low, high = 0, len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][0] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return -1
        
        def binary_search(arr: List[int], target: int) -> bool:
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return False
        
        row_index = find_row(matrix, target)
        if row_index == -1:
            return False
        
        return binary_search(matrix[row_index], target)