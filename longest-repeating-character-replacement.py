def characterReplacement(self, s: str, k: int) -> int:
    left, right = 1, len(s) + 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if self._checkforlength(mid, s, k): left = mid
        else: right = mid
    return left

def _checkforlength(self, l, s, k):
    hashmap = {}
    ans = 0
    i = 0
    for j in range(len(s)):
        hashmap[s[j]] = hashmap.get(s[j], 0) + 1
        if j - i + 1 > l:
            hashmap[s[i]] -= 1
            i += 1
        ans = max(ans, hashmap[s[j]])
        if l - ans <= k: return True
    return False
