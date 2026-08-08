class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index_zero = 0
        for index_digit in range(len(nums)):
            if nums[index_digit] != 0 :
                nums[index_zero], nums[index_digit] = nums[index_digit], nums[index_zero]
                index_zero += 1