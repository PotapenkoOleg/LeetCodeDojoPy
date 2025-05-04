# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(s: str) -> str:
            str_1 = list(s)
            left = 0
            right = len(s) - 1
            while left < right:
                temp = str_1[left]
                str_1[left] = str_1[right]
                str_1[right] = temp
                left += 1
                right -= 1
            return "".join(str_1)

        words = s.split(" ")
        ans = []
        for word in words:
            ans.append(reverse_word(word))

        return " ".join(ans)


solution = Solution()
result = solution.reverseWords("Let's take LeetCode contest")
pass
