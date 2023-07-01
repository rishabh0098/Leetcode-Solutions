def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = []
    hashmap = {}
    for s in strs:
        t = ''.join(sorted(s))
        if t in hashmap:
            hashmap[t].append(s)
        else:
            hashmap[t] = [s]
    for value in hashmap.values():
        res.append(value)
    return res
