class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        combination_sum_helper(candidates, target, 0, [], result)
        return result

    def combination_sum_helper(candidates, target, start, current, result):
        if target == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break

            current.append(candidates[i])
            combination_sum_helper(candidates, target - candidates[i], i, current, result)
            current.pop()


# link, https://leetcode.com/problems/combination-sum/