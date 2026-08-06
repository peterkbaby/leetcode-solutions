class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit=0

        for price in prices:
            if price < smallest :
                smallest = price
            
            current_profit = price -  smallest 

            if current_profit > max_profit:
                max_profit = current_profit
            
        return max_profit
        


        
        

            
