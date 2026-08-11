class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        while nums != []:
            mini = min(nums)
            maxi = max(nums)
            avg.add(float(mini + maxi) / 2.0)
            nums.remove(mini)
            nums.remove(maxi)
        return len(avg)