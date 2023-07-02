def maxSubArray(self, nums: List[int]) -> int:
    if max(nums) < 0:
        return max(nums)
    maxsum = 0
    cursum = 0
    for num in nums:
        cursum += num
        if cursum < 0:
            cursum = 0
        else:
            maxsum = max(cursum, maxsum)
    return maxsum
