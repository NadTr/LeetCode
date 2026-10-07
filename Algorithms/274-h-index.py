class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse = True)
        
        count = 0
        for c in citations:
            if c <= count and c > 0:
                return count
            count += 1 if c > 0 else 0

        return count