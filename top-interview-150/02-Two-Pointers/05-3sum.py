class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        start = 0
        for start in range(len(nums) - 2):
            if start > 0 and nums[start] == nums[start -1]:
                continue
            i = start +1
            end = len(nums) - 1
            while i < end:
                sum_three = nums[start] + nums[i] + nums[end]
                if  sum_three > 0:
                    end -= 1
                elif sum_three < 0:
                    i += 1
                else:
                    triplets.append([nums[start], nums[i], nums[end]])
                    i += 1
                    while nums[i] == nums[i-1] and i < end:
                        i += 1
        return triplets