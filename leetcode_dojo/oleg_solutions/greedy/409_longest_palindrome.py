# 409. Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/description/

from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans_even = 0
        ans_odd = 0
        flag = False
        for k, v in cnt.items():
            if v%2 == 0:
                ans_even += v
            else:
                ans_odd += v-1
                flag = True
        return ans_even + ans_odd + (1 if flag else 0);
    

solution = Solution()
s = "abccccdd"
#s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
ans = solution.longestPalindrome(s)                

print(ans)