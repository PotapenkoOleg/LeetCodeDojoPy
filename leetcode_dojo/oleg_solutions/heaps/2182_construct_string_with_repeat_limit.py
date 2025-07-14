# 2182. Construct String With Repeat Limit
# https://leetcode.com/problems/construct-string-with-repeat-limit/description/

import heapq
from typing import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapq.heapify(max_heap)
        ans = ''
        while max_heap:
            char_neg, count = heapq.heappop(max_heap)
            char = chr(-char_neg)
            rep_num = min(count, repeatLimit)
            ans+=char * rep_num
            if count > rep_num and max_heap:
                next_char_neg, next_count = heapq.heappop(max_heap)
                ans+=chr(-next_char_neg)
                if next_count > 1:
                    heapq.heappush(max_heap, (next_char_neg, next_count - 1))
                heapq.heappush(max_heap, (char_neg, count - rep_num))
        return ans
         
solution = Solution()
# s = "cczazcc"
# repeatLimit = 3
s = "aababab" 
repeatLimit = 2
ans = solution.repeatLimitedString(s, repeatLimit)
print(ans)
