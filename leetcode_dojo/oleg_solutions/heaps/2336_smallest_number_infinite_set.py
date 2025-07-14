# 2336. Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/description/

import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.__is_present = set()
        self.__current = 1
        self.__heap = []
        

    def popSmallest(self) -> int:
        if len(self.__heap):
            ans = heapq.heappop(self.__heap)
            self.__is_present.remove(ans)
            return ans
        ans = self.__current
        self.__current+=1
        return ans
        

    def addBack(self, num: int) -> None:
        if self.__current <= num or num in self.__is_present:
            return
        self.__is_present.add(num)
        heapq.heappush(self.__heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)