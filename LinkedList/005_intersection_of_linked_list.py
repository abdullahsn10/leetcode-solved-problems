from typing import Optional
from LinkedList.utils import ListNode, create_test_list, print_list


def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    # find the length
    size1, size2 = 0, 0
    itr1, itr2 = headA, headB
    while itr1:
        size1 += 1
        itr1 = itr1.next
    while itr2:
        size2 += 1
        itr2 = itr2.next

    first, second = headA, headB

    if size2 > size1:
        diff = size2 - size1
        count = 0
        while count < diff:
            second = second.next
            count += 1
    else:
        diff = size1 - size2
        count = 0
        while count < diff:
            first = first.next
            count += 1

    while first and second:
        if first == second:
            return first
        first = first.next
        second = second.next
