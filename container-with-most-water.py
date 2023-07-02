def maxArea(self, height: List[int]) -> int:
    max_area = 0
    i, j = 0, len(height) - 1
    while i < j:
        if height[i] <= height[j]:
            max_area = max(height[i] * (j - i), max_area)
            i += 1
        else:
            max_area = max(height[j] * (j - i), max_area)
            j -= 1
    return max_area
