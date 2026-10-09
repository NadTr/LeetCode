class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_k_sum = k_sum = sum(nums[:k])

        for i in range(1, len(nums) - k + 1):
            k_sum += (nums[i + k - 1] - nums[i-1])
            max_k_sum = max(max_k_sum, k_sum)
            
        return max_k_sum / k