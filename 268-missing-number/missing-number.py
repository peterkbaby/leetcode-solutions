class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sum=0
        expected_sum= n*(n+1)//2
        for num in nums:
            sum+=num
        
        return expected_sum - sum


        
        