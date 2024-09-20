class ListNode:
    """
    Definition for singly-linked list node
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_test_list():
    """
    Create a test list
    """
    head = ListNode(10, None)
    second = ListNode(20, None)
    third = ListNode(30, None)
    fourth = ListNode(40, None)
    head.next = second
    second.next = third
    third.next = fourth
    return head


def print_list(head: ListNode):
    """
    Print the linked list
    """
    if head is None:
        print("Empty List")

    itr: ListNode = head
    llstr = ""

    while itr:
        llstr += f"{itr.val} --> "
        itr = itr.next

    print(llstr)
