class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_index = 0
        for non_zero_index in range(len(nums)):
            if nums[non_zero_index] != 0:
                nums[zero_index] = nums[non_zero_index]
                zero_index += 1
        while zero_index < len(nums):
            nums[zero_index] = 0
            zero_index += 1 

        