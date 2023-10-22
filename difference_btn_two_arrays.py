class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        first_array = []
        second_array = []
        result = []
        for num in nums1:
            if not num in nums2:
                if not num in first_array:
                    first_array.append(num)
        for num in nums2:
            if not num in nums1:
                if not num in second_array:
                    second_array.append(num)
        result.append(first_array)
        result.append(second_array)
        return result 

# link to question, https://leetcode.com/problems/find-the-difference-of-two-arrays/