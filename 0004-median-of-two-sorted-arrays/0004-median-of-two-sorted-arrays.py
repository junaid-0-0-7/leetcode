class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = []
        for i in range(len(nums1)):
            median.append(nums1[i])
        for i in range(len(nums2)):
            median.append(nums2[i])
        median.sort()
        count = len(median)
        if count % 2 == 1:
            return median[count // 2]
        else:
            middle1 = median[count // 2 -1]
            middle2 = median[count // 2]
            return (middle1 + middle2) /2