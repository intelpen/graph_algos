"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
"""

class Solution:
    def mergeArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        merged = [0] * (len(nums1) + len(nums2))
        index1, index2 = 0, 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                merged[index1 + index2] = nums1[index1]
                index1 += 1
            else:
                merged[index1 + index2] = nums2[index2]
                index2 += 1

        if index1 < len(nums1):
            merged[index1 + index2:] = nums1[index1:]
        else:
            merged[index1 + index2:] = nums2[index2:]
        return merged

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.mergeArrays(nums1, nums2)
        if len(merged) % 2 == 1:
            return merged[len(merged) // 2]
        else:
            return ((merged[len(merged) // 2] + merged[len(merged) // 2 - 1])) / 2


if __name__ == "__main__":
    nums1 = [2]
    nums2 = []
    s = Solution()
    print(s.mergeArrays(nums1, nums2))
