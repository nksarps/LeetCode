class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        result = []

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        counter = 0
        while counter < len(pos):
            result.append(pos[counter])
            result.append(neg[counter])
            counter += 1
            
        return result

# link, https://leetcode.com/problems/rearrange-array-elements-by-sign/