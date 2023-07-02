def threeSum(self, nums: List[int]) -> List[List[int]]:
    ans = []
    hashset = set()
    nums.sort()
    for k in range(len(nums)):
        i, j = k + 1, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] + nums[k] == 0:
                if not (nums[k], nums[i], nums[j]) in hashset:
                    ans.append([nums[k], nums[i], nums[j]])
                    hashset.add((nums[k], nums[i], nums[j]))
                i += 1
                j -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                i += 1
            else:
                j -= 1
    return list(ans)
