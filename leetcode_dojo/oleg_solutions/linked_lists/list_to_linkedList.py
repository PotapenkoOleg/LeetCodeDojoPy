from oleg_solutions.linked_lists.list_node import ListNode


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