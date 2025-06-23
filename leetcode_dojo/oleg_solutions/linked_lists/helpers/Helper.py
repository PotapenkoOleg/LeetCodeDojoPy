from oleg_solutions.linked_lists.helpers.list_node import ListNode

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
    