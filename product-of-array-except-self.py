def productExceptSelf(self, nums: List[int]) -> List[int]:
    leftprod, rightprod = [nums[0]], [nums[-1]]
    for i in range(1, len(nums)):
        leftprod.append(leftprod[-1] * nums[i])
    for i in reversed(range(0, len(nums) - 1)):
        rightprod.append(rightprod[-1] * nums[i])
    output = []
    for i in range(len(nums)):
        if i == 0:
            output.append(rightprod[-2])
        elif i == len(nums) - 1:
            output.append(leftprod[-2])
        else:
            output.append(leftprod[i - 1] * rightprod[len(nums) - 2 - i])
    return output
