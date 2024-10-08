from typing import Optional
from LinkedList.utils import ListNode, create_test_list, print_list


def has_cycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
