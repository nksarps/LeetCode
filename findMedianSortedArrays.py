class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        merged_array = nums1 + nums2
        merged_array.sort()
        if (m + n) % 2 == 0:
            median = merged_array[(m + n) // 2] + merged_array[((m + n) // 2) - 1]
            median /= 2
        else:
            median = merged_array[(m + n) // 2]
        return median
