class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxP=0
        while r < len(prices):
            #profit?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if maxP < profit:
                    maxP = profit


            else:
                l=r
            r=r+1
        return maxP

        
        

            
