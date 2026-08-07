class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            num2 = target - nums[i] 
            if num2 in map.keys():
                return [i, map[num2]]
            else:
                map[nums[i]] = i
        return []
