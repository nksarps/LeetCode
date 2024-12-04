class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        if len(nums1) <= len(nums2):
            for num in nums1:
                if num in nums2:
                    result.append(num)
                    nums2.remove(num)
        else:
            for num in nums2:
                if num in nums1:
                    result.append(num)
                    nums1.remove(num)
        return result
        
# link to question, https://leetcode.com/problems/intersection-of-two-arrays/