class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                if not num in result:
                    result.append(num)
        for num in nums2:
            if num in nums1:
                if not num in result:
                    result.append(num)
        return result 
        
# link to question, https://leetcode.com/problems/intersection-of-two-arrays/