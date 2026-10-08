class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        start = 0
        end = len(nums) - 1 
        
        while start < end:
            middle = start + (end - start) // 2
            print(start, middle, end)
            print('nums', nums[start], nums[middle], nums[end])
            if nums[middle] < nums[middle + 1]:
                start = middle + 1
            else:
                end = middle

        return start