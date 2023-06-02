class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        nums2 = []
        for num in nums:
            count = nums.count(num)
            if count> len(nums) / 3 and num not in nums2:
                nums2.append(num)
        return nums2

        #MajorityElement2