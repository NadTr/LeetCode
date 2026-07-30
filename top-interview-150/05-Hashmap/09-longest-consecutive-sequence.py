class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len_seq = 0
        len_seq  = 0
        nums.sort()
        for i in range(len(nums)):
            if i == 0:
                len_seq = 1
            elif nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                len_seq += 1
            else:
                max_len_seq = max(max_len_seq, len_seq)
                len_seq = 1
        max_len_seq = max(max_len_seq, len_seq)
        return max_len_seq