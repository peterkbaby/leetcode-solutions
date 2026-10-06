class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = 0

        for current in range(1, len(nums)):
            if nums[current] != nums[unique]:
                unique += 1
                nums[unique] = nums[current]

        return unique + 1