class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_index = {}
        for i in range(len(nums)) :
            num  = nums[i]
            if num in nums_index and i-nums_index[num] <= k:
                return True
            else: 
                nums_index[num] = i      
        return False