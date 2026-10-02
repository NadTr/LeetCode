class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = len(nums) + 1
        right = 0
        sum_val = 0

        for left in range(len(nums)):           
            while sum_val < target and right < len(nums): 
                sum_val += nums[right] 
                right += 1
            if sum_val >= target:                
                min_len = min(min_len, right - left)
            sum_val -= nums[left]
        return min_len if min_len <= len(nums) else 0