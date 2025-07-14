# 1845. Seat Reservation Manager
# https://leetcode.com/problems/seat-reservation-manager/description/

import heapq


class SeatManager:

    def __init__(self, n: int):
        self.__heap = []
        for i in range(n):
            self.__heap.append(i+1)
        heapq.heapify(self.__heap)
        

    def reserve(self) -> int:
        return heapq.heappop(self.__heap)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.__heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)