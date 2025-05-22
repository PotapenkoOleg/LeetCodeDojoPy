# 82. Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def list_to_linked_list(nums):
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



# 0,1,1,1,2,3
# 0,1,1,1,2,2,2
# 0,2,3,4,5,6 
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
                
solution = Solution()
head = list_to_linked_list([1,2,3,3,4,4,5])
x = solution.deleteDuplicates(head)
print(x)
