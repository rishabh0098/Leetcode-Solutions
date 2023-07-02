def lengthOfLongestSubstring(self, s: str) -> int:
    maxlen, start = 0, 0
    found = {}
    for end in range(len(s)):
        ch = s[end]
        if ch in found and found[ch] >= start:
            start = found[ch] + 1
        else:
            maxlen = max(maxlen, end - start + 1)
        found[ch] = end
    return maxlen
