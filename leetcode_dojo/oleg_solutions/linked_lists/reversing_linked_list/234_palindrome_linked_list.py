# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Helper():
    @classmethod
    def to_linked_list(cls, nums):
        prev = None
        head = None
        for num in nums:
            node = ListNode(num)
            if not prev:
                head = node
            else:
                prev.next = node
            prev = node
        return head

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def find_middle(head):
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def reverse(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        def compare(left, right):
            while right:
                if left.val != right.val:
                    return False
                left = left.next
                right = right.next
            return True
        
        left = head
        middle = find_middle(head)
        right = reverse(middle)
        ans = compare(left, right)
        return ans
    
    
solution = Solution()

input = Helper.to_linked_list([1, 2, 3, 2, 1])
result = solution.isPalindrome(input)

print(result)
