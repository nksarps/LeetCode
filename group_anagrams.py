class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            k = ''.join(sorted(s))

            if not k in d:
                d[k] = [s]
            else:
                d[k].append(s)

        return list(d.values())
        
        
# link https://leetcode.com/problems/group-anagrams