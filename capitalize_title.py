class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr_title = title.split()
        return_arr = []
        return_sentence = ''
        n = 0
        for word in arr_title:
            if len(word) > 2:
                word = word.capitalize()
            else:
                word = word.lower()
                pass
            return_arr.append(word)
        while n < len(return_arr):
            if not n == len(return_arr) - 1:
                return_sentence += return_arr[n]
                return_sentence += ' '
            else:
                return_sentence += return_arr[n]
            n += 1
        return return_sentence

# link to question, https://leetcode.com/problems/capitalize-the-title