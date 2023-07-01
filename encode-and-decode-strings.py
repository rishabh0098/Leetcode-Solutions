def encode(strs):
    encoded = ''
    for st in strs:
        for char in st:
            encoded += str(ord(char) + 100)
        encoded += '-'
    return encoded[:-1]

def decode(st):
    res = []
    ind_strs = st.split('-')
    for st in ind_strs:
        i = 0
        ans = ''
        while i < len(st):
            subst = st[i:i + 3]
            ans += chr(int(subst) - 100)
            i += 3
        res.append(ans)
    return res
