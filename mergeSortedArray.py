class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while not len(nums1) == m:
            nums1.pop()
        while not len(nums2) == n:
            nums2.pop()
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        
# link to question, https://leetcode.com/problems/merge-sorted-array/