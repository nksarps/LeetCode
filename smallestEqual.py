class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        smallest_num = len(nums)
        count = 0

        for i in range(len(nums)):
            if i % 10 == nums[i]:
                count += 1
                if i <= smallest_num:
                    smallest_num = i
        if count > 0:
            return smallest_num
        else:
            return -1

# link, https://leetcode.com/problems/smallest-index-with-equal-value/