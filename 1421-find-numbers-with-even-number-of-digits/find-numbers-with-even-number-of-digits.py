class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            digits = 0
            while i > 0:
                digits+=1
                i//=10
            
            if digits%2==0:
                count+=1
        return count
        