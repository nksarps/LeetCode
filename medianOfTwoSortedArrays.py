class Solution:
    # def __init__(self, nums1, nums2):
    #     self.nums1 = nums1
    #     self.nums2 = nums2

    def findMedianSortedArrays(self, nums1, nums2):
        merged_array = nums1 + nums2
        merged_array.sort()

        m = len(nums1)
        n = len(nums2)

        if (m + n) % 2 == 0:
            median = (merged_array[(m + n) // 2] + merged_array[((m + n) // 2) - 1]) / 2
        else:
            median = merged_array[(m + n) // 2]
        print(median)


nums1 = list(map(int, input("Enter the first array: ").strip().split()))
nums2 = list(map(int, input("Enter the second array: ").strip().split()))

solution = Solution()
solution.findMedianSortedArrays(nums1, nums2)
