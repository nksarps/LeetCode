class Solution:
    def majorityElement(self, nums):
        nums.sort()
        max_num = nums.count(nums[0])
        for i in range(len(nums)):
            n = nums.count(nums[i])
            print(n, nums[i])
            if n >= nums.count(nums[i-1]):
                num = nums[i]
        return num
            

nums =[6,5,5]
soln = Solution()
print(soln.majorityElement(nums))