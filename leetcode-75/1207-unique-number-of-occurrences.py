class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        nums = set(arr)
        counter = set()
        for n in nums:
            count = arr.count(n)
            if count in counter: return False
            counter.add(count)
        return True