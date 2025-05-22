# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
from typing import Optional

from oleg_solutions.linked_lists.list_node import ListNode


        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or head.next:
            return None
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
            if not fast:
                return head
        while fast and fast.next:
            fast=fast.next
            slow=slow.next
        slow=slow.next
        return head