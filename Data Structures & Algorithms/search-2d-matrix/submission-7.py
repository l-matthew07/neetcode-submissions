from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        def findRow(matrix, target):
            min, max = 0, len(matrix) - 1
            while min <= max:
                mid = (min + max) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif matrix[mid][0] > target:
                    max = mid-1
                else:
                    min = mid + 1
            return -1

        def binSearch(list, target):
            min, max = 0, len(list) - 1
            while min <= max:
                mid = (min + max) // 2
                if list[mid] == target:
                    return True
                elif list[mid] < target:
                    min = mid + 1
                else:
                    max = mid - 1
            return False

        row_index = findRow(matrix, target)
        if row_index == -1:
            return False
        return binSearch(matrix[row_index], target)                    

