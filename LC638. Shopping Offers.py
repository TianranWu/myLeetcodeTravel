class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        filter_special = []
        for element in special:
            real_p = sum(price[i] * element[i] for i in range(n))
            if element[-1] < real_p and sum(price[i] for i in range(n))>0:
                filter_special.append(element)
        
        def dfs(cur_needs):
            min_cur = sum(price[i] * need for i,need in enumerate(cur_needs))
            for cur_special in filter_special:
                special_price = cur_special[-1]
                nxt_needs = []
                for i in range(n):
                    if cur_special[i] > cur_needs[i]: break
                    nxt_needs.append(needs[i] - cur_special[i])
                if len(nxt_needs) == n:
                    min_cur = min(min_cur, dfs(tuple(nxt_needs)) + special_price)
            return min_cur
            
        # dp[needs] = special + dp[cur_needs]
        return dfs(tuple(needs))
