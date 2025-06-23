# 2074. Reverse Nodes in Even Length Groups
# https://leetcode.com/problems/reverse-nodes-in-even-length-groups/description/

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
    
    @classmethod
    def get_node_by_value(cls, head, val):
        curr = head
        while curr:
            if curr.val == val:
                return curr
            curr = curr.next
        return None
        
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_group(head, last_node):
            previous = None
            current = head
            while current and not previous is last_node:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous
        
        def get_next_group(node_before, group_number):
            node_count = 0
            head = node_before
            while True:
                head = head.next
                node_count+=1
                if not head.next or node_count == group_number:
                    break
            return head, node_count
            
        sentinel = ListNode(0, head)
        current_head = sentinel
        current_group_number = 1
        while True:
            last_node_in_group, group_len = get_next_group(current_head, current_group_number)
            a = current_head
            b = current_head.next
            c = last_node_in_group
            d = last_node_in_group.next
            if group_len % 2 == 0:
                reverse_group(b,c)
                a.next = c
                b.next = d
                current_head = b
            else:
                current_head = last_node_in_group
            current_group_number += 1 
            if not d:
                break
        return sentinel.next
        
        
solution = Solution()
head = Helper.to_linked_list([1,2,3,4,5,6,7,8])
hea2 = Helper.to_linked_list([1,3,2,4,5,6,8,7])
head = solution.reverseEvenLengthGroups(head)
print(head.val)