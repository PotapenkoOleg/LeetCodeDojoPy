# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if l[left].isalpha() and l[right].isalpha():
                temp = l[left]
                l[left] = l[right]
                l[right] = temp
                left += 1
                right -= 1
                continue
            if not l[left].isalpha():
                left += 1
                continue
            if not l[right].isalpha():
                right -= 1
                continue
        ans = "".join(l)
        return ans


solution = Solution()
s = "Test1ng-Leet=code-Q!"
result = solution.reverseOnlyLetters(s)
pass
