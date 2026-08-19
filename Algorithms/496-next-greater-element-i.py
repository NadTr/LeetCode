class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_elements = []
        for i in nums1:
            start = nums2.index(i)
            greater = -1
            for j in range(start, len(nums2)):
                if nums2[j] > i:
                    greater = nums2[j]
                    break
            greater_elements.append(greater)
        return greater_elements
