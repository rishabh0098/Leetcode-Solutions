def isPalindrome(self, s: str) -> bool:
    st = ''
    for ch in s:
        if ch.isalpha() or ch.isnumeric(): st += ch
    st = st.lower()
    l = len(st)
    for i in range(l):
        if st[i] != st[l - 1 - i]: return False
    return True
