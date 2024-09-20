from typing import Optional
from LinkedList.utils import ListNode, create_test_list, print_list


def merge_two_lists(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode()
    temp = dummy

    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            temp = l1
            l1 = l1.next
        else:
            temp.next = l2
            temp = l2
            l2 = l2.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return dummy.next


list = create_test_list()
print_list(list)
list2 = create_test_list()
print_list(list2)
merged_list = merge_two_lists(list, list2)
print_list(merged_list)
