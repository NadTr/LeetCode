from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersect = []
        for num, nb in counter1.items():
            count = min(nb, counter2[num])
            for i in range(count):
                intersect.append(num)
        return intersect        