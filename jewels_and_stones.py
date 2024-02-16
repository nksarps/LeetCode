class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = [jewel for jewel in jewels]
        stones = [stone for stone in stones]
        checked_jewels = []
        total_jewels = 0

        for jewel in jewels:
            if not jewel in checked_jewels:
                num_jewels = stones.count(jewel)
                total_jewels += num_jewels
            checked_jewels.append(jewel)
        
        return total_jewels

# link, https://leetcode.com/problems/jewels-and-stones/