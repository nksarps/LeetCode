class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrence_counts = {}
        for num in arr:
            if num in occurrence_counts:
                occurrence_counts[num] += 1
            else:
                occurrence_counts[num] = 1
        occurrence_set = set()
        for count in occurrence_counts.values():
            if count in occurrence_set:
                return False
            else:
                occurrence_set.add(count)
        return True

# link, https://leetcode.com/problems/unique-number-of-occurrences/