# 2130. Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def find_middle(head):
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head):
            previous = None
            current = head
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous
        ans = 0
        left = head
        middle = find_middle(head)
        right = reverse(middle)
        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next
        return ans
        