from typing import Optional

from LinkedList.utils import ListNode, create_test_list, print_list


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        return None

    slow, fast = head, head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next
    return head


list = create_test_list()
print_list(list)
list = delete_middle(list)
print_list(list)
