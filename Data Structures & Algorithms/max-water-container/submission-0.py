from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # width is distance between indices
            width = right - left
            # height is the min of the two bars
            h = min(height[left], height[right])
            # compute area
            area = width * h
            max_area = max(max_area, area)

            # move the pointer at the shorter bar
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
