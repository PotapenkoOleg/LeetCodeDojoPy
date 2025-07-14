# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/description/

from typing import Counter, List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        for word, count in cnt.items():
            heapq.heappush(heap,(-count, word))
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
        

solution = Solution()
words = ["i","love","leetcode","i","love","coding"]
k=2
#words = ["the","day","is","sunny","the","the","the","sunny","is","is"] 
#k=4
solution.topKFrequent(words, k)