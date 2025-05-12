# 1456. Maximum Number of Vowels in a Substring of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        cur = 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        ans = cur
        length = len(s)
        for i in range(k, length):
            if s[i] in vowels:
                cur += 1
            if s[i - k] in vowels:
                cur -= 1
            ans = max(ans, cur)
        return ans
