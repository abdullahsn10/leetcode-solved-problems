from typing import Optional
from LinkedList.utils import ListNode, create_test_list, print_list


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


# Test Cases
list = create_test_list()
print_list(list)
reversed_list = reverse_list(list)
print_list(reversed_list)
"S"
