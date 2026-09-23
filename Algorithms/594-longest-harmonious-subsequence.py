from collections import Counter
class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums_counter = Counter(nums)

        longest_seq = 0
        for n in nums_counter:
            if n + 1 in nums_counter:
                longest_seq = max(longest_seq, nums_counter[n] + nums_counter[n+1])

        return longest_seq