def maxProfit(self, prices: List[int]) -> int:
    maxp, cur_min = 0, prices[0]
    for price in prices:
        if price > cur_min:
            maxp = max(maxp, price - cur_min)
        else:
            cur_min = price
    return maxp
