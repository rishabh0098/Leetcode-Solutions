def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    most_freq = [key for key, value in sorted(hashmap.items(), key = lambda item: item[1], reverse=True)]
    return most_freq[:k]
