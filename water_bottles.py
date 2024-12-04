class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            drunk += new_bottles
            empty_bottles = (empty_bottles % numExchange) + new_bottles
        
        return drunk

#link: https://leetcode.com/problems/water-bottles/description/