class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        count = 1
        for i in range(1, len(arr)):
            if i == 1:
                diff = arr[i] - arr[0]
            else:
                another_diff = arr[i] - arr[i - 1]
            if i == 1:
                pass
            else:
                if diff == another_diff:
                    count += 1
        if count == len(arr) - 1:
            return True
        else:
            return False