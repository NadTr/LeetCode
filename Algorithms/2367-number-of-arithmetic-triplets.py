class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets_count = 0
        n = set(nums)
        for i in n:
            if i - diff in n and i - 2*diff in n:
                triplets_count += 1
        return triplets_count