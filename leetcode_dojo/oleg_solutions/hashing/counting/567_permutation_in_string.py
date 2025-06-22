# 567. Permutation in String
# https://leetcode.com/problems/permutation-in-string/description/

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        WIN_SIZE = len(s1)
        cnt1 = Counter(s1)
        cnt2 = Counter(s2[:WIN_SIZE])
        if cnt1 == cnt2:
            return True
        left = 0
        for right in range(WIN_SIZE, len(s2)):
            cnt2[s2[left]]-=1
            cnt2[s2[right]]+=1
            if cnt1 == cnt2:
                return True
            left+=1
        return False


solution = Solution()

s1 = "ab" 
s2 = "eidbaooo"
result = solution.checkInclusion(s1, s2)
print(result)

s1 = "ab" 
s2 = "eidboaoo"
result = solution.checkInclusion(s1, s2)

s1 = "hello"
s2 = "ooolleoooleh"
result = solution.checkInclusion(s1, s2)

s1 = "adc"
s2 = "dcda"
result = solution.checkInclusion(s1, s2)

pass