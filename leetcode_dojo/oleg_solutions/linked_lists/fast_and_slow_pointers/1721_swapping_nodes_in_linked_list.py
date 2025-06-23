# 1721. Swapping Nodes in a Linked List
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Helper():
    @classmethod
    def list_to_linked_list(cls, nums):
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
    def print_linked_list(cls, head):
            if not head:
                return
            curr = head
            while curr:
                print(str(curr.val))
                if curr.next:
                    print(" -> ")
                curr = curr.next
    

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = head
        second = head 
        third = head
        count = 1
        while first and first.next:
            first = first.next
            if count >= k:
                second = second.next
            if count < k:
                third = third.next
            count+=1
        temp = second.val
        second.val = third.val
        third.val = temp
        return head


        
solution = Solution()

head = Helper.list_to_linked_list([1,2,3,4,5]) 
solution.swapNodes(head, k = 3)

head = Helper.list_to_linked_list([7,9,6,6,7,8,3,0,9,5])
solution.swapNodes(head,k = 5)