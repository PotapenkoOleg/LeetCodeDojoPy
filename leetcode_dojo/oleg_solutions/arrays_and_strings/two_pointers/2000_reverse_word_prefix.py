# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word

        def reverse_list(word_list):
            left = 0
            right = len(word_list) - 1
            while left < right:
                temp = word_list[left]
                word_list[left] = word_list[right]
                word_list[right] = temp
                left += 1
                right -= 1
            return word_list

        word_list = list(word)
        res = reverse_list(word_list[0: index + 1])
        return ''.join(res) + ''.join(word_list[index + 1:])


solution = Solution()
word = "abcdefd"
ch = "d"
ans = solution.reversePrefix(word, ch)
pass
