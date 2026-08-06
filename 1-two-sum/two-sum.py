class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}
        for i, num in enumerate(nums):
            MinValue = target - num

            if MinValue in seen:
                return [seen[MinValue],i]
            seen[num] = i