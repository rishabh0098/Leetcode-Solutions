def containsDuplicate(self, nums: List[int]) -> bool:
    hashmap = {}
    for num in nums:
        if num in hashmap: return True
        else: hashmap[num] = True
    return False
