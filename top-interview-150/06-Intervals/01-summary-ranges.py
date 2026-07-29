class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) < 2:
            return [] if len(nums) == 0 else [str(nums[0])]
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                ranges += [str(start) + "->" +str(nums[i-1])] if start != nums[i-1] else [str(start)]
                start = nums[i]
        ranges += [str(start) + "->" +str(nums[-1])] if start != nums[-1] else [str(start)]
        return ranges
