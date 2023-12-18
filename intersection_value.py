class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        
        count_nums1_in_nums2 = 0
        count_nums2_in_nums1 = 0
        
        for num in nums1:
            if num in set_nums2:
                count_nums1_in_nums2 += 1
        
        for num in nums2:
            if num in set_nums1:
                count_nums2_in_nums1 += 1
        
        return [count_nums1_in_nums2, count_nums2_in_nums1]

# link to question, https://leetcode.com/problems/find-common-elements-between-two-arrays