def trap_sol1(self, height: List[int]) -> int:
    ans = 0
    lmax, rmax = height[0], height[-1]
    i, j = 0, len(height) - 1
    while i < j:
        lmax = max(lmax, height[i])
        rmax = max(rmax, height[j])
        if lmax <= rmax:
            ans += lmax - height[i]
            i += 1
        else:
            ans += rmax - height[j]
            j -= 1
    return ans

def trap_sol2(self, height: List[int]) -> int:
    ans = 0
    lmax, rmax = height[0], height[-1]
    i, j = 0, len(height) - 1
    while i < j:
        if lmax <= rmax:
            ans += lmax - height[i]
            i += 1
            lmax = max(lmax, height[i])
        else:
            ans += rmax - height[j]
            j -= 1
            rmax = max(rmax, height[j])
    return ans
