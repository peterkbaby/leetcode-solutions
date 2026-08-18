class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = nums[0]
        max_so_far = nums[0]
        for num in nums[1:]:
            running_sum = max(num, (running_sum+num))
            new_max_so_far = max(max_so_far, running_sum)
            max_so_far = new_max_so_far

        return max_so_far
        