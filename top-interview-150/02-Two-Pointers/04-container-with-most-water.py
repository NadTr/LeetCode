class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area= 0
        while end > start:
                area = (end - start) * min(height[start], height[end])
                max_area = max_area if max_area >= area else area
                if height[start] >= height[end]:
                    end -= 1
                else:
                    start += 1
        return max_area