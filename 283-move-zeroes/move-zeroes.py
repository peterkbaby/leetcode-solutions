class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        inserted_pos=0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[inserted_pos], nums[i] = nums[i], nums[inserted_pos]
                inserted_pos+=1
