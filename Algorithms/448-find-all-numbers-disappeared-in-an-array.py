class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        disappeared = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set: 
                disappeared.append(i)
        return disappeared