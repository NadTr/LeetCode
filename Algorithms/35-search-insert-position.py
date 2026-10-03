class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1

        while start_index <= end_index:
            middle = (end_index + start_index) // 2
            if nums[middle] < target:
                start_index = middle + 1 
            else:
                end_index = middle - 1
                
        return start_index