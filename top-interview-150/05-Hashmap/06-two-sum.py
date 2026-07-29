class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            other_num = target - nums[i]
            if other_num in nums[i + 1:]:
                index = i + 1 + nums[i + 1 :].index(other_num)
                return [i, index]