class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for start in range(len(heights)):
            for end in range(1, len(heights)):
                areas.append(min(heights[start], heights[end]) * (end - start))

        areas.sort(reverse = True)
        return areas[0]
