# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

from typing import Optional

from oleg_solutions.linked_lists.helpers.Helper import Helper


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# 0,1,1,1,2,3
# 0,1,1,1,2,2,2
# 0,2,3,4,5,6 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0, head)
        prev = sentinel
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                prev.next = cur.next
            else:
                prev = prev.next
            cur = cur.next
        return sentinel.next

solution = Solution()

head = Helper.list_to_linked_list([1,2,3,3,4,4,5])
head = solution.deleteDuplicates(head)
Helper.print_linked_list(head)
