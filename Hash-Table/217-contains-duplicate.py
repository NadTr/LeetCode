class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_no_duplicate = set(nums)
        return len(nums_no_duplicate) != len(nums)