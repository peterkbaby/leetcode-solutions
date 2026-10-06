class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum = float("-inf")
        secondMaximum = float("-inf")
        thirdMaximum = float("-inf")

        for num in nums:
            if num == maximum or num == secondMaximum or num == thirdMaximum:
                continue
            if num > maximum:
                thirdMaximum = secondMaximum
                secondMaximum = maximum
                maximum = num

            elif num > secondMaximum:
                thirdMaximum = secondMaximum
                secondMaximum = num
            elif num > thirdMaximum:
                thirdMaximum = num
            
        return thirdMaximum if thirdMaximum != float("-inf") else maximum